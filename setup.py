from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


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
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    cffi_modules=["src/cmarkgfm/build_cmark.py:ffibuilder"],
    python_requires='>=3.9',
    setup_requires=["cffi>=2.0.0", "pycparser>=2.06"],
    install_requires=["cffi>=2.0.0"],
    project_urls={
        'Bug Reports': 'https://github.com/theacodes/cmarkgfm/issues',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/theacodes/cmarkgfm',
    },
    zip_safe=False,
    include_package_data=True,
)
