from app import app
from models.player import *
from models.game import *
from flask import render_template

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("player 1", player_1_choice)
    player_2 = Player("player 2", player_2_choice)
    game = Game()
    winner = game.play(player_1, player_2)

    return render_template("game.html", player_1 = player_1, player_2 = player_2, winner = winner)


# @app.route('/play')
# def play():
#     return render_template()

