from footy import footy_app
from flask import render_template

@footy_app.route('/')
@footy_app.route('/index')
def index():
    user = { 'username': 'tyrone' }
    watched_players = [
        {
            "name": "Sokratis Papastathopoulos",
            "position": "D",
            "age": 30,
            "height": "6'1",
            "weight": 181,
            "nationality": "Greece",
            "appearances": 16,
            "subs": 0,
            "assists":2,
            "shots": 0,
            "fouls_committed": 26,
            "fouls_suffered": 13,
            "yellow_cards": 7,
            "red_cardS": 0
        },
    ]
    return render_template('index.html', user=user, watched_players=watched_players, title="Welcome to FootyTown")