from random import randint, choice
from itertools import islice

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
    """Produces a random list of moves to scramble the cube"""
    return list(islice(get_scramble_iterator(), n_moves))


def get_scramble_iterator():
    """Produces a random sequence of moves to scramble the cube"""
    next_moves = [choice(Cube.basic_moves) + choice(Cube.modifiers)]
    while True:
        if len(next_moves) > 3:
            move, next_moves = next_moves[-4], next_moves[-3:]
            yield move

        new_move = choice(Cube.basic_moves) + choice(Cube.modifiers)

        # Check moves do not cancel each other
        if len(next_moves) < 1:
            next_moves.append(new_move)
            continue
        prev_move = next_moves[-1]
        res = check_result(prev_move, new_move)
        if res != prev_move + " " + new_move:
            next_moves = next_moves[:-1] + res.split()
            continue
        if len(next_moves) < 2:
            next_moves.append(new_move)
            continue
        if Cube.opposite.get(new_move[0]) != prev_move[0] and Cube.opposite.get(prev_move[0]) != new_move[0]:
            next_moves.append(new_move)
            continue
        prev_prev_move = next_moves[-2]
        res = check_result(prev_prev_move, new_move).split()
        if len(res) < 1:
            next_moves = next_moves[:-2] + [prev_move]
        elif len(res) < 2:
            next_moves = next_moves[:-2] + [prev_move] + res
        else:
            next_moves = next_moves[:-2] + [res[0]] + [prev_move] + [res[1]]


def get_scrambled_cube_with_moves(cube=Cube(), n_moves=None):
    if n_moves is not None:
        moves = get_scramble(n_moves)
    else:
        moves = get_scramble()
    for move in moves:
        cube.parse_move(move)
    return cube, moves


def get_scrambled_cube(cube=Cube(), n_moves=None):
    return get_scrambled_cube_with_moves(cube, n_moves)[0]
