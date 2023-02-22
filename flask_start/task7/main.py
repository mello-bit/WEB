from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/<nameOfPlanet>')
def show_simple_html_page(nameOfPlanet):
    return render_template("first_page.html", nameOfPlanet=nameOfPlanet)


@app.route('/choice/<placa>')
def show_choice_html(placa):
    return render_template("first_page.html", nameOfPlanet=placa)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_result_of_planet(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
