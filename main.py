#!/usr/bin/env python3

#from chess import Board
#from chess.uci import popen_engine
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

MOVE_MS = 1
DEPTH = 2

#engine = popen_engine('stockfish')
#engine.uci()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/best', methods=['GET'])
@cross_origin()
def make_move():
    #req = request.get_json(force=True)
    #try:
    #    board = Board(req['fen'])
    #except (ValueError, KeyError):
    #    return '', 400
    #engine.ucinewgame()
    #engine.position(board)
    #req['fen']
    #best_move = engine.go(movetime=MOVE_MS, depth=DEPTH)[0]
    #board.push(best_move)
    print('finding best move')
    return jsonify({
        'best_move': {
            'from': 'g7',
            'to': 'g6'
        }, #best_move.uci(),
        'trigger': 'the opening is a'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port, host='0.0.0.0')