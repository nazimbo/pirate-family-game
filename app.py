from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

# import database

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pirate-family'

mysql = MySQL(app)

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


@app.route('/main-character')
def main_character():
    return render_template('create-character.html')


@app.route('/create-main-character', methods=['POST'])
def create_main_character():
    if request.method == 'POST':
        data = request.form
        cursor = mysql.connection.cursor()

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (data['name'], data['email'])

        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('choose_character'))


@app.route('/characters')
def choose_character():
    return render_template('characters.html', characters=characters)


@app.route('/playwith/<int:character_id>')
def play(character_id):
    character = characters[character_id-1]
    return render_template('play.html', character=character)


if __name__ == '__main__':
    app.run(debug=True)
