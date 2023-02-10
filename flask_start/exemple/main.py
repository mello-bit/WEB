from flask import Flask, render_template

app = Flask(__name__)


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
    return '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Колонизация</title>
</head>

<body>
    <h1 class="">Жди нас Марс!</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/300px-OSIRIS_Mars_true_color.jpg"
        alt="Жди нас Марс">
    <p class="first">Человечество вырастет из детства.</p>
    <p class="sec">Человечеству мало одна планета.</p>
    <p class="thr">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="four">Мы начнем с марса!</p>
    <p class="five">Присоединяйся!</p>

    <style>
        h1 {
            color: red;
        }

        .first {
            background-color: red;
        }

        .sec {
            background-color: blue;
        }

        .thr {
            background-color: cornflowerblue;
        }

        .four {
            background-color: brown;
        }

        .five {
            background-color: chocolate;
        }
    </style>
</body>

</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
