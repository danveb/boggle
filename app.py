from boggle import Boggle

boggle_game = Boggle()
from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secretive'

boggle_game = Boggle()

# root route
@app.route('/')
def index():
    """Display game Board"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get('highscore', 0)
    playcount = session.get('playcount', 0)
    return render_template('index.html', board=board, highscore=highscore, playcount=playcount)

# check word route
@app.route('/check')
def check():
    word = request.args['guess']
    board = session['board']
    result = boggle_game.check_valid_word(board, word)
    return jsonify({"result": result})

# check score route
@app.route('/score', methods=["POST"])
def setscore():
    score = request.json['score']
    highest = session.get('highscore', 0)
    plays = session.get('playcount', 0)
    # check if score is greater than highest
    if score > highest:
        # set high score to be the new score
        session['highscore'] = score
    session['playcount'] = plays + 1
    return jsonify(newRecord=score > highest)
