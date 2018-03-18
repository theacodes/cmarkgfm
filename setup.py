from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cmarkgfm',
    version='0.1.0a1',
    description="Minimal bindings to GitHub's fork of cmark",
    long_description=long_description,
    url='https://github.com/jonparrott/cmarkgfm',
    author='The Python Packaging Authority',
    author_email='thea@skeletonbuddy.com, pypa-dev@googlegroups.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    cffi_modules=["src/cmarkgfm/build_cmark.py:ffibuilder"],
    setup_requires=["cffi>=1.0.0"],
    install_requires=["cffi>=1.0.0"],
    project_urls={
        'Bug Reports': 'https://github.com/jonparrott/cmarkgfm/issues',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/jonparrott/cmarkgfm',
    },
    zip_safe=False,
    include_package_data=True,
)
