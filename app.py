from flask import Flask, render_template, request
from translate_functions import get_translations
# from custom_filters import c_indent

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def translator_page():
    if request.method == "POST":
        print({**request.form})
        n_seq = request.form["dna_seq"]
        res = get_translations(n_seq)
        print(res)
        print(str(res))

        arguments = {**request.form, **res}
        print(arguments)

        return render_template("translator.html", **arguments)
    else:
        return render_template("translator.html")


if __name__ == '__main__':
    app.run()

# TODO: Protein output
# TODO: Protein translation
# TODO: All reading frames translation
# TODO: seq info
# TODO: Opmaak
# TODO Docstrings
# TODO: grouping sub-eiwitten
# TODO CHECK DNA/RNA
