from random import randint, choice
from functools import reduce

from cube import Cube


def check_result(move_1, move_2):
    """Determines the effective result of applying 2 moves in sequence"""
    if len(move_2) == 1:
        if move_1 == move_2:
            return move_2 + "2"
        elif move_1 == move_2 + "'":
            return ""
        elif move_1 == move_2 + "2":
            return move_2 + "'"
    elif move_2[-1] == "'":
        if move_1 == move_2:
            return move_2[0] + "2"
        elif move_1 == move_2[0]:
            return ""
        elif move_1 == move_2[0] + "2":
            return move_2[0]
    else:
        if move_1 == move_2:
            return ""
        elif move_1 == move_2[0]:
            return move_2[0] + "'"
        elif move_1 == move_2[0] + "'":
            return move_2[0]
    return move_1 + " " + move_2


def get_scramble(n_moves=randint(25, 35)):
    """Produces a random sequence of moves to scramble the cube"""
    moves = [choice(Cube.basic_moves) + choice(Cube.modifiers)]
    while len(moves) < n_moves:
        new_move = choice(Cube.basic_moves) + choice(Cube.modifiers)

        # Check moves do not cancel each other
        if len(moves) < 1:
            moves.append(new_move)
            continue
        prev_move = moves[-1]
        res = check_result(prev_move, new_move)
        if res != prev_move + " " + new_move:
            moves = moves[:-1] + res.split()
            continue
        if len(moves) < 2:
            moves.append(new_move)
            continue
        if Cube.opposite.get(new_move[0]) != prev_move[0] and Cube.opposite.get(prev_move[0]) != new_move[0]:
            moves.append(new_move)
            continue
        prev_prev_move = moves[-2]
        res = check_result(prev_prev_move, new_move).split()
        if len(res) < 1:
            moves = moves[:-2] + [prev_move]
        elif len(res) < 2:
            moves = moves[:-2] + [prev_move] + res
        else:
            moves = moves[:-2] + [res[0]] + [prev_move] + [res[1]]

    moves_str = reduce(lambda a, b: a + " " + b, moves)
    return moves_str
