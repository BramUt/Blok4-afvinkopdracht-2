# Eerste app is app.py, tweede is Flask.
import app


@app.template_filter("c_indent")
def c_indent(indent, text):
    return f"{' '*indent}text"
