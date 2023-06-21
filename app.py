from flask import Flask, render_template

app = Flask(__name__)

characters = [
    {"name": "Victor", "luck": 10, "id": 1,
     "image": "static/images/victor.jpg", "description": "Le roi des pirates !"},
    {"name": "Machicoulis", "luck": 8, "id": 2,
     "image": "static/images/machicoulis.jpg"},
    {"name": "La Sardine", "luck": 5, "id": 3,
     "image": "static/images/sardine.jpg"},
    {"name": "Dr. Spratt", "luck": 2, "id": 4,
     "image": "static/images/spratt.jpg"},
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/characters')
def choose_character():
    return render_template('characters.html', characters=characters)


@app.route('/play/<int:id>')
def play(id):
    character = characters[id-1]
    return render_template('play.html', character=character)


if __name__ == '__main__':
    app.run(debug=True)
