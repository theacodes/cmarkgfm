from setuptools import setup

# Minimal setup.py for CFFI configuration
# All other metadata is in pyproject.toml
setup(
    cffi_modules=["src/cmarkgfm/build_cmark.py:ffibuilder"],
)
