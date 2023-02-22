from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/<nameOfPlanet>')
def show_simple_html_page(nameOfPlanet):
    return render_template("first_page.html", nameOfPlanet=nameOfPlanet)


@app.route('/choice/<placa>')
def show_choice_html(placa):
    return render_template("first_page.html", nameOfPlanet=placa)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
