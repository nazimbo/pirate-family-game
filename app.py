from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/characters')
def character_creation():
    return render_template('characters.html')


@app.route('/combat')
def combat():
    return render_template('combat.html')


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


if __name__ == '__main__':
    app.run()
