import jsbeautifier

def format_js(code: str):
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    return jsbeautifier.beautify(code, opts)