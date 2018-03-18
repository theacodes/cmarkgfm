from cmarkgfm import _cmark


def markdown_to_html(text, options=0):
    encoded_text = text.encode('utf-8')
    raw_result = _cmark.lib.cmark_markdown_to_html(
        encoded_text, len(encoded_text), options)
    return _cmark.ffi.string(raw_result).decode('utf-8')


def parse_document(text, options=0):
    encoded_text = text.encode('utf-8')
    return _cmark.lib.cmark_parse_document(
        encoded_text, len(encoded_text), options)


def render_html(root, options=0):
    raw_result = _cmark.lib.cmark_render_html(
        root, options, _cmark.ffi.NULL)
    return _cmark.ffi.string(raw_result).decode('utf-8')
