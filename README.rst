cmarkgfm - Bindings to GitHub's cmark
=====================================

Minimalist bindings to GitHub's fork of cmark.

Installation
------------

This package is published as `cmarkgfm <https://pypi.org/project/cmarkgfm/>`__
and can be installed with `pip` or `pipenv`::

    pip install --user cmarkgfm
    pipenv install cmarkgfm

.. note:: We do not yet distribute wheels for cmarkgfm so you'll need a
    compiler handy. We want to get those up soon.


Usage
-----

High-level usage is really straightforward. To render normal CommonMark
markdown:

..code-block:: python

    import cmarkgfm

    html = cmarkgfm.markdown_to_html(markdown_text)


To render GitHub-flavored markdown:

..code-block:: python

    import cmarkgfm

    html = cmarkgfm.markdown_to_html(markdown_text)


Contributing
------------

Pull requests are welcome. :)


License
-------

This project is under the MIT License. It includes components under differing
copyright under the ``third_party`` directory in this source tree.


TODO
----

* Setup automatic wheel building.
* Add more tests.
