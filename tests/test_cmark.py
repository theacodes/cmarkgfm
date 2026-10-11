from __future__ import unicode_literals

import sys
import textwrap

import pytest

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
    cmark.node_free(result)


def test_render_html():
    text = u"Hello, **world**!"
    root = cmark.parse_document(text)
    result = cmark.render_html(root)
    cmark.node_free(root)
    assert result == '<p>Hello, <strong>world</strong>!</p>\n'


def test_parser_interface():
    text = u"Hello, **world**!"
    parser = cmark.parser_new()
    cmark.parser_feed(parser, text)
    root = cmark.parser_finish(parser)
    result = cmark.render_html(root)
    cmark.node_free(root)
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


def _peak_rss_mb():
    import resource

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # ru_maxrss is in bytes on macOS and kilobytes elsewhere.
    return peak / (1024 * 1024 if sys.platform == 'darwin' else 1024)


@pytest.mark.skipif(sys.platform == 'win32', reason='needs resource module')
@pytest.mark.parametrize('render', [
    cmark.markdown_to_html,
    lambda text: cmark.markdown_to_html_with_extensions(
        text, extensions=['table', 'strikethrough']),
], ids=['markdown_to_html', 'markdown_to_html_with_extensions'])
def test_rendering_releases_memory(render):
    # Each render used to leak its syntax tree and HTML output, roughly
    # 1-5x the input size, so 2000 renders of 64 KB grew by 100+ MB.
    text = '\n\n'.join(['Some *markdown* text, ~~struck~~.'] * 1800)
    for _ in range(50):
        render(text)
    before = _peak_rss_mb()
    for _ in range(2000):
        render(text)
    assert _peak_rss_mb() - before < 20
