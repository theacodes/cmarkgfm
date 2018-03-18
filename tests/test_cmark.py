# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

from cmarkgfm import cmark


def test_markdown_to_html():
    text = u"Hello, **world**!"
    result = cmark.markdown_to_html(text)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'


def test_parse_document():
    text = u"Hello, **world**!"
    result = cmark.parse_document(text)
    assert result is not None


def test_render_html():
    text = u"Hello, **world**!"
    root = cmark.parse_document(text)
    result = cmark.render_html(root)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'
