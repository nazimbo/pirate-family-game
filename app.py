from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "pirate-family"

mysql = MySQL(app)

characters = [
    {
        "name": "Victor",
        "id": 1,
        "image": "static/images/victor.jpg",
        "description": "Le roi des pirates !",
        "stats": {"force": 8, "luck": 6, "intelligence": 7, "charisma": 9},
    },
    {
        "name": "Machicoulis",
        "id": 2,
        "image": "static/images/machicoulis.jpg",
        "description": "Le roi des pirates !",
        "stats": {"force": 8, "luck": 6, "intelligence": 7, "charisma": 9},
    },
    {
        "name": "La Sardine",
        "id": 3,
        "image": "static/images/sardine.jpg",
        "description": "Le roi des pirates !",
        "stats": {"force": 8, "luck": 6, "intelligence": 7, "charisma": 9},
    },
    {
        "name": "Dr. Spratt",
        "id": 4,
        "image": "static/images/spratt.jpg",
        "description": "Le roi des pirates !",
        "stats": {"force": 8, "luck": 6, "intelligence": 7, "charisma": 9},
    },
]

items = [
    {
        "name": "Sabre",
        "id": 1,
        "image": "static/images/sabre.jpg",
        "description": "Un sabre de pirate",
    },
    {
        "name": "Pistolet",
        "id": 2,
        "image": "static/images/pistolet.jpg",
        "description": "Un pistolet de pirate",
    },
    {
        "name": "Boulet de canon",
        "id": 3,
        "image": "static/images/boulet.jpg",
        "description": "Un boulet de canon de pirate",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main-character")
def main_character():
    return render_template("create-character.html")


@app.route("/create-main-character", methods=["POST"])
def create_main_character():
    if request.method == "POST":
        data = request.form
        cursor = mysql.connection.cursor()

        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (data["name"], data["email"])

        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("choose_character"))


@app.route("/characters")
def choose_character():
    return render_template("characters.html", characters=characters)


@app.route("/playwith/<character>")
def play(character):
    character = [k for k in characters if k["name"] == character][0]["name"]
    return render_template("play.html", character=character)


if __name__ == "__main__":
    app.run(debug=True)
