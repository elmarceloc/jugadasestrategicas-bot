#!/usr/bin/env python3

from chess import Board # https://python-chess.readthedocs.io/en/latest/
from chess.uci import popen_engine, InfoHandler
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

engine = popen_engine('./stockfish_10_x64')
engine.uci()

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#methods = dir(engine)
#print(methods)

@app.route('/best', methods=['GET'])
@cross_origin()
def make_move():
    try:
        board = Board(request.args.get('fen'))
    except (ValueError, KeyError):
        return '', 400

    # Register a standard info handler.
    info_handler = InfoHandler()
    engine.info_handlers.append(info_handler)

    #sets the engine at the fiven position using fen
    engine.ucinewgame()
    engine.position(board)
    engine.debug(True)
    
    #methods = dir(board)
    #print(methods)
    
    #retrives the elo from the parameters
    difficulty = int(request.args.get('difficulty'))

    #sets the elo to the engine
    #engine.setoption({"UCI_LimitStrength": True})
    #engine.setoption({"UCI_Elo": "2850"})
    move_ms = 300
    depth = 40    

    if difficulty == 0:
        move_ms = 200
        depth = 5
    elif difficulty == 1:
        move_ms = 1000
        depth = 40
    elif difficulty == 2:
        move_ms = 3000
        depth = 100

    #get the best move
    best_move = engine.go(movetime=move_ms, depth=depth)[0]
    board.push(best_move)

    print('move_ms',move_ms)
    print('depth',depth)

    best_move_uci = best_move.uci()
    best_move_from = best_move_uci[:2]
    best_move_to = best_move_uci[2:4] 
    best_move_promotion = best_move_uci[4:]
    
    score = info_handler.info["score"][1].cp

    print('BEST MOVE:',best_move)
    print('score:', score)
    # send all the information to the client
    return jsonify({
        'best_move': {
            'move' : best_move_uci,
            'from': best_move_from,
            'to': best_move_to,
            'promotion': best_move_promotion,
        },
        'score': score
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(port=port)
