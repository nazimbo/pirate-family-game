import random

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
        "stats": {"force": 6, "luck": 0, "intelligence": 3, "charisma": 9}
    },
    {
        "name": "Machicoulis",
        "id": 2,
        "image": "static/images/machicoulis.jpg",
        "description": "Le plus bête des membres",
        "stats": {"force": 8, "luck": 3, "intelligence": 0, "charisme": 3}
    },
    {
        "name": "La Sardine",
        "id": 3,
        "image": "static/images/sardine.jpg",
        "description": "Un bras cassé au comportement mou",
        "stats": {"force": 0, "luck": 2, "intelligence": 5, "charisme": 1}
    },
    {
        "name": "Dr. Spratt",
        "id": 4,
        "image": "static/images/spratt.jpg",
        "description": "Expert quand il s'agit de tricher aux jeux",
        "stats": {"force": 2, "luck": 1, "intelligence": 7, "charisme": 4}
    },
]

items = [
    {
        "name": "Carte au Trésor Ancienne",
        "id": 1,
        "luck": random.randint(1, 10),
        "description": "Une carte détaillée qui indique les emplacements des indices et des obstacles sur le chemin du trésor."
    },
    {
        "name": "Clé du Capitaine",
        "id": 2,
        "luck": random.randint(1, 10),
        "description": "Une clé spéciale qui ouvre les portes verrouillées du repaire du capitaine pirate, où le trésor est gardé en sécurité."
    },
    {
        "name": "Longue-Vue Pirate",
        "id": 3,
        "luck": random.randint(1, 10),
        "description": "Une longue-vue puissante pour repérer les repaires pirates, les îles secrètes et les signes cachés qui mènent au trésor."
    },
    {
        "name": "Boussole Magique",
        "id": 4,
        "luck": random.randint(1, 10),
        "description": "Une boussole spéciale qui pointe toujours vers le trésor le plus proche, même s'il est caché."
    },
]

def getCharacterLuck(characterName):
    for character in characters:
        if character == characterName:
            return character["stats"]["luck"]
        else:
            return 0

def getItemLuck(itemName):
    for item in items:
        if item == itemName:
            return item["luck"]
        else:
            return 0

def winCondition(luck):
    if luck >= 80:
        return True
    else:
        return False

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
    character = next((c for c in characters if c["name"] == character), None)

    character = {
        "name": character["name"],
        "id": character["id"],
        "image": character["image"],
        "description": character["description"],
        "stats": character["stats"]
    }

    return render_template("play.html", character=character, items=items)\

@app.route("/playwithitem/<character>/<item>")
def play_with_item(character, item):
    selected_character = next((c for c in characters if c["name"] == character), None)
    selected_item = next((i for i in items if i["name"] == item), None)
    luck_rate = selected_character["stats"]["luck"] * selected_item["luck"]
    return render_template("play-with-item.html", character=selected_character, item=selected_item, luck_rate=luck_rate, is_win=winCondition(luck_rate))


if __name__ == "__main__":
    app.run(debug=True)
