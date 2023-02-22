from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def show_simple_html_page():
    if request.method == "GET":
        return render_template("first_page.html")
    elif request.method == "POST":
        print(request.form["sername"])
        print(request.form["name"])
        print(request.form["pilot"])
        print(request.form["email"])

        print(request.form)

        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
