from flask import Flask, render_template, request
from stitcher import Stitcher

stitcher = Stitcher()

app = Flask(__name__)
stitcher = Stitcher()

@app.route("/", methods=["GET", "POST"])
def index():
    final_prompt = None

    if request.method == "POST":
        query = request.form.get("query")
        location = request.form.get("location")

        if query and location:
            final_prompt = stitcher.build_prompt(query, location)

    return render_template("index.html", final_prompt=final_prompt)

if __name__ == "__main__":
    app.run(debug=True)
