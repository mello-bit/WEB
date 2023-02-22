from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="./")


@app.route('/index')
def index():
    return "На марсе будут яблони цвести"


@app.route('/')
def clesh():
    return render_template("/index.html")


@app.route('/image_mars')
def show_img():
    return '''
            <title>Привет, Марс!</title>
            <h1>Жди нас, Марс!</h1>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/300px-OSIRIS_Mars_true_color.jpg"
            alt="Жди нас, Марс!">
'''


@app.route('/promotion_image')
def prm():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
