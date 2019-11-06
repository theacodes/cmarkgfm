cmarkgfm - Python bindings to GitHub's cmark
============================================

Minimalist Python bindings to GitHub's fork of cmark.

Installation
------------

This package is published on PyPI as `cmarkgfm <https://pypi.org/project/cmarkgfm/>`__
and can be installed with `pip` or `pipenv`::

    pip install --user cmarkgfm
    pipenv install cmarkgfm

Wheels are provided for macOS, Linux, and Windows for Python 2.7, 3.5, and 3.6.

Usage
-----

High-level usage is really straightforward. To render normal CommonMark
markdown:

.. code-block:: python

    import cmarkgfm

    html = cmarkgfm.markdown_to_html(markdown_text)


To render GitHub-flavored markdown:

.. code-block:: python

    import cmarkgfm

    html = cmarkgfm.github_flavored_markdown_to_html(markdown_text)


Contributing
------------

Pull requests are welcome. :)


License
-------

This project is under the MIT License. It includes components under differing
copyright under the ``third_party`` directory in this source tree.
