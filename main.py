from flask import Flask, render_template, request

app = Flask(__name__)

translation_table : dict[str, int] = {
    'A': 1, 'B': 2, 'C': 3, 'Č': 4, 'D': 5, 'Ď': 6, 'E': 7, 'F': 8, 'G': 9,
    'H': 10, 'CH': 11, 'I': 12, 'J': 13, 'K': 14, 'L': 15, 'M': 16, 'N': 17, 'Ň': 18,
    'O': 19, 'P': 20, 'Q': 21, 'R': 22, 'Ř': 23, 'S': 24, 'Š': 25, 'T': 26, 'Ť': 27,
    'U': 28, 'V': 29, 'W': 30, 'X': 31, 'Y': 32, 'Z': 33, 'Ž': 34
}


def spocitej_hash(text: str) -> int:
    txet = text[::-1]
    acc = 0
    weight = 1
    for ch in txet:
        acc += translation_table[ch.upper()] * weight
        weight *= 35
    return acc


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    result = None
    if request.method == "POST":
        input_text = request.form.get("input_text")
        if input_text:
            # Example computation: Reverse the input string
            result = spocitej_hash(input_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
