from __future__ import unicode_literals

import textwrap

from cmarkgfm import cmark


def _normalize_ws(html):
    return textwrap.dedent(html.strip("\n")).strip("\n")


def test_markdown_to_html():
    text = u"Hello, **world**!"
    result = cmark.markdown_to_html(text)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'


def test_render_html_with_extensions():
    text = u"Hello, https://pypa.io!"
    result = cmark.markdown_to_html_with_extensions(
        text, extensions=['autolink'])
    expected = """
        <p>Hello, <a href="https://pypa.io">https://pypa.io</a>!</p>
    """
    assert _normalize_ws(result) == _normalize_ws(expected)


def test_github_flavored_markdown_to_html():
    text = u"Hello, https://pypa.io!"
    result = cmark.github_flavored_markdown_to_html(text)
    expected = """
        <p>Hello, <a href="https://pypa.io">https://pypa.io</a>!</p>
    """
    assert _normalize_ws(result) == _normalize_ws(expected)


def test_github_flavored_markdown_to_html_pre_tag():
    text = u"```python\nprint('hello')\n```"
    result = cmark.github_flavored_markdown_to_html(text)
    expected = """
        <pre lang="python"><code>print('hello')
        </code></pre>
    """
    assert _normalize_ws(result) == _normalize_ws(expected)


def test_github_flavored_markdown_to_html_tasklist():
    text = u"- [X] Task 1 Done\n- [ ] Task 2 Incomplete"
    result = cmark.github_flavored_markdown_to_html(text)
    expected = """
        <ul>
        <li><input type="checkbox" checked="" disabled="" /> Task 1 Done</li>
        <li><input type="checkbox" disabled="" /> Task 2 Incomplete</li>
        </ul>
    """
    assert _normalize_ws(result) == _normalize_ws(expected)


def test_parse_document():
    text = u"Hello, **world**!"
    result = cmark.parse_document(text)
    assert result is not None


def test_render_html():
    text = u"Hello, **world**!"
    root = cmark.parse_document(text)
    result = cmark.render_html(root)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'


def test_parser_interface():
    text = u"Hello, **world**!"
    parser = cmark.parser_new()
    cmark.parser_feed(parser, text)
    root = cmark.parser_finish(parser)
    result = cmark.render_html(root)
    cmark.parser_free(parser)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'


def test_core_extensions_ensure_registered():
    cmark.core_extensions_ensure_registered()


def test_find_syntax_extension():
    extension = cmark.find_syntax_extension('table')
    assert extension is not None


def test_find_syntax_extension_doesnt_exist():
    extension = cmark.find_syntax_extension('notarealext')
    assert extension is None
