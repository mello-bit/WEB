from flask import Flask, flash, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def show_simple_html_page():
    if request.method == "GET":
        return render_template("first_page.html")
    elif request.method == "POST":
        files = request.files.getlist("file")

        for file in files:
            if file.filename != "":
                file.save(os.path.join("flask_start", "task8",
                          "static", "img", file.filename))

        return redirect(url_for("show_form_with_img", filename=file.filename))


@app.route('/<filename>', methods=["POST", "GET"])
def show_form_with_img(filename):
    if request.method == "GET":
        return render_template("first_page.html", filename=filename)
    elif request.method == "POST":
        files = request.files.getlist("file")

        for file in files:
            if file.filename != "":
                file.save(os.path.join("flask_start", "task8",
                          "static", "img", file.filename))

        return redirect(url_for("show_form_with_img", filename=file.filename))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
