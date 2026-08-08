from flask import Flask, render_template
from Dataset import load_dataset

app = Flask(__name__)

@app.route("/")
def home():

    data = load_dataset()

    return render_template(
        "index.html",
        head=data["head"],
        describe=data["describe"],
        missing=data["missing"],
        dtypes=data["dtypes"],
        cgpa=data["cgpa"]
    )

if __name__ == "__main__":
    app.run(debug=True)