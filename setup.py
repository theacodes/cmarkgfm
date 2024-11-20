import platform
import sys
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


class custom_build_ext(build_ext):
    """Custom build_ext command that uses mingw32 when building on Python2.7
    in Windows."""

    def finalize_options(self):
        build_ext.finalize_options(self)
        is_windows = platform.system() == 'Windows'
        is_py2 = sys.version_info[0] < 3
        if self.compiler is None and is_windows and is_py2:
            self.compiler = 'mingw32'


setup(
    name='cmarkgfm',
    version='2024.11.20',
    description="Minimal bindings to GitHub's fork of cmark",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/theacodes/cmarkgfm',
    author='The Python Packaging Authority',
    author_email='me@thea.codes, pypa-dev@googlegroups.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    cffi_modules=["src/cmarkgfm/build_cmark.py:ffibuilder"],
    setup_requires=["cffi>=1.15.0"],
    install_requires=["cffi>=1.15.0"],
    project_urls={
        'Bug Reports': 'https://github.com/theacodes/cmarkgfm/issues',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/theacodes/cmarkgfm',
    },
    zip_safe=False,
    include_package_data=True,
    cmdclass={
        'build_ext': custom_build_ext,
    },
)
