from flask import Flask, render_template, abort, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from card import deck_bd_card_info, card_list


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Connecting to the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

deck = deck_bd_card_info()
answer = ""
for x in card_list:
    i = f"<h1>{x}:</h1>\n<h3>{deck[x]}.</h3>\n\n"
    answer = answer + i


@app.route("/")
def home():
    return f"{answer}"

# TODO 2. create class Deck with the class Card
# TODO 3. start the game
# TODO 4. create two player
# TODO 5. give each player two cards from the deck
# TODO 6. add additional cards to your hand, if needed
# TODO 7. flip cards and compare and declare the winner

if __name__ == "__main__":
    app.run(debug=True)
