import os
import glob
import io

import cffi


# Get the directory for the cmark source files. It's under the package root
# as /third_party/cmark/src
HERE = os.path.dirname(os.path.abspath(__file__))
PACKAGE_ROOT = os.path.abspath(os.path.join(HERE, '../../'))
SRC_DIR = os.path.join(PACKAGE_ROOT, 'third_party/cmark/src')
EXTENSIONS_SRC_DIR = os.path.join(PACKAGE_ROOT, 'third_party/cmark/extensions')
GENERATED_SRC_DIR = os.path.join(PACKAGE_ROOT, 'generated')

with io.open(os.path.join(HERE, 'cmark.cffi.h'), 'r', encoding='utf-8') as fh:
    CMARK_DEF_H = fh.read()

with io.open(os.path.join(HERE, 'cmark_module.h'), 'r', encoding='utf-8') as fh:
    CMARK_MODULE_H = fh.read()


def _get_sources(dir, exclude=set()):
    sources = glob.iglob(os.path.join(dir, '*.c'))
    return [
        os.path.relpath(path, start=PACKAGE_ROOT)
        for path in
        sources
        if os.path.basename(path) not in exclude
    ]


SOURCES = _get_sources(SRC_DIR, exclude=set(['main.c']))
SOURCES.extend(_get_sources(EXTENSIONS_SRC_DIR))

ffibuilder = cffi.FFI()
ffibuilder.cdef(CMARK_DEF_H)
ffibuilder.set_source(
    'cmarkgfm._cmark',
    CMARK_MODULE_H,
    sources=SOURCES,
    include_dirs=[SRC_DIR, EXTENSIONS_SRC_DIR, GENERATED_SRC_DIR]
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
