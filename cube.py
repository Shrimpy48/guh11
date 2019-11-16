from random import randint, choice
from functools import reduce


class Cube:
    u = 0
    l = 1
    f = 2
    r = 3
    b = 4
    d = 5

    x = 7
    y = 8
    z = 9

    basic_moves = ["U", "D", "L", "R", "F", "B"]
    modifiers = ["", "2", "'"]
    extended_moves = ["u", "d", "l", "r", "f", "b", "M", "E", "S"]
    rotations = ["x", "y", "z"]

    opposite = {"U": "D", "L": "R", "F": "B"}

    def __init__(self):
        # array of faces, each of which is a 2d array of colours
        self.data = [[[k for i in range(3)] for j in range(3)] for k in range(6)]

    # debugging functions
    def print_net(self):
        for i in self.data[0]:
            print("      ", i)
        for i in range(3):
            for j in range(4):
                print(self.data[j + 1][i], end="  ")
            print()
        for i in self.data[5]:
            print("      ", i)

    def init_cube(self):
        self.data = [
            [[0, 0, 0],
             ["u", "u", "u"],
             [1, 2, 3]],
            [[1, 1, 1],
             ["l", "l", "l"],
             [1, 2, 3]],
            [[2, 2, 2],
             ["f", "f", "f"],
             [1, 2, 3]],
            [[3, 3, 3],
             ["r", "r", "r"],
             [1, 2, 3]],
            [[4, 4, 4],
             ["b", "b", "b"],
             [1, 2, 3]],
            [[5, 5, 5],
             ["d", "d", "d"],
             [1, 2, 3]],
        ]

    def turn_face(self, face):
        """Rotates the colours of a face clockwise"""
        self.data[face][0][0], self.data[face][0][1], self.data[face][0][2], self.data[face][1][0], \
            self.data[face][1][2], self.data[face][2][0], self.data[face][2][1], self.data[face][2][2] \
            = \
            self.data[face][2][0], self.data[face][1][0], self.data[face][0][0], self.data[face][2][1], \
            self.data[face][0][1], self.data[face][2][2], self.data[face][1][2], self.data[face][0][2]

    def turn_layer(self, face):
        """Rotates an outer layer clockwise"""
        self.turn_face(face)

        # HERE BE MAGIC
        if face == self.r:
            self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], \
                self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2], self.data[2][2][2], \
                self.data[2][1][2], self.data[2][0][2] \
                = \
                self.data[2][2][2], self.data[2][1][2], self.data[2][0][2], self.data[0][2][2], self.data[0][1][2], \
                self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], \
                self.data[5][1][2], self.data[5][0][2]

        elif face == self.l:
            self.data[0][0][0], self.data[0][1][0], self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], \
                self.data[2][2][0], self.data[5][0][0], self.data[5][1][0], self.data[5][2][0], self.data[4][2][2], \
                self.data[4][1][2], self.data[4][0][2]\
                = \
                self.data[4][2][2], self.data[4][1][2], self.data[4][0][2], self.data[0][0][0], self.data[0][1][0], \
                self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], self.data[2][2][0], self.data[5][0][0], \
                self.data[5][1][0], self.data[5][2][0]

        elif face == self.u:
            self.data[1][0][0], self.data[1][0][1], self.data[1][0][2], self.data[2][0][0], self.data[2][0][1], \
                self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[4][0][0], \
                self.data[4][0][1], self.data[4][0][2]\
                = \
                self.data[2][0][0], self.data[2][0][1], self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], \
                self.data[3][0][2], self.data[4][0][0], self.data[4][0][1], self.data[4][0][2], self.data[1][0][0], \
                self.data[1][0][1], self.data[1][0][2]

        elif face == self.f:
            self.data[0][2][0], self.data[0][2][1], self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], \
                self.data[3][2][0], self.data[5][0][2], self.data[5][0][1], self.data[5][0][0], self.data[1][2][2], \
                self.data[1][1][2], self.data[1][0][2] \
                = \
                self.data[1][2][2], self.data[1][1][2], self.data[1][0][2], self.data[0][2][0], self.data[0][2][1], \
                self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0], self.data[5][0][2], \
                self.data[5][0][1], self.data[5][0][0]

        elif face == self.d:
            self.data[1][2][0], self.data[1][2][1], self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], \
                self.data[2][2][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2], self.data[4][2][0], \
                self.data[4][2][1], self.data[4][2][2] \
                = \
                self.data[4][2][0], self.data[4][2][1], self.data[4][2][2], self.data[1][2][0], self.data[1][2][1], \
                self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], self.data[2][2][2], self.data[3][2][0], \
                self.data[3][2][1], self.data[3][2][2]

        elif face == self.b:
            self.data[0][0][0], self.data[0][0][1], self.data[0][0][2], self.data[3][0][2], self.data[3][1][2], \
                self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], self.data[5][2][0], self.data[1][2][0], \
                self.data[1][1][0], self.data[1][0][0] \
                = \
                self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], \
                self.data[5][2][0], self.data[1][2][0], self.data[1][1][0], self.data[1][0][0], self.data[0][0][0], \
                self.data[0][0][1], self.data[0][0][2]

    @staticmethod
    def reverse_face(face):
        """Reverses the order of the colours on a face"""
        return list(reversed([list(reversed(row)) for row in face]))

    def rotate(self, axis):
        """Rotates the cube"""
        if axis == self.x:
            # clockwise around R
            # r, l', f -> u -> b -> d
            self.turn_face(self.r)
            for i in range(3):
                self.turn_face(self.l)
            self.data[2], self.data[0], self.data[4], self.data[5] = self.data[5], self.data[2], self.reverse_face(
                self.data[0]), self.reverse_face(self.data[4])
        elif axis == self.y:
            # clockwise around U
            # u, d', f -> l -> b -> r
            self.turn_face(self.u)
            for i in range(3):
                self.turn_face(self.d)
            self.data[2], self.data[1], self.data[4], self.data[3] = \
                self.data[3], self.data[2], self.data[1], self.data[4]
        elif axis == self.z:
            # clockwise around F
            # f, b', l -> u -> r -> d
            # x' y' x
            for i in range(3):
                self.rotate(self.x)
            for i in range(3):
                self.rotate(self.y)
            self.rotate(self.x)

    def parse_move(self, move):
        """Performs the move described by the given notation"""
        if len(move) == 3:
            move = move.replace("'", "")
        if move[-1] == "'":
            move = move[:-1]
            self.parse_move(move + "2")
        elif move[-1] == "2":
            move = move[:-1]
            self.parse_move(move)

        if move == "U":
            self.turn_layer(self.u)
        elif move == "D":
            self.turn_layer(self.d)
        elif move == "L":
            self.turn_layer(self.l)
        elif move == "R":
            self.turn_layer(self.r)
        elif move == "F":
            self.turn_layer(self.f)
        elif move == "B":
            self.turn_layer(self.b)

        elif move == "x":
            self.rotate(self.x)
        elif move == "y":
            self.rotate(self.y)
        elif move == "z":
            self.rotate(self.z)

        elif move == "M":
            self.parse_move("x'")
            self.parse_move("L'")
            self.parse_move("R")
        elif move == "E":
            self.parse_move("y'")
            self.parse_move("U")
            self.parse_move("D'")
        elif move == "S":
            self.parse_move("z")
            self.parse_move("F'")
            self.parse_move("B")

        elif move == "u":
            self.parse_move("y")
            self.parse_move("D")
        elif move == "d":
            self.parse_move("y'")
            self.parse_move("U")
        elif move == "l":
            self.parse_move("x'")
            self.parse_move("R")
        elif move == "r":
            self.parse_move("x")
            self.parse_move("L")
        elif move == "f":
            self.parse_move("z")
            self.parse_move("B")
        elif move == "b":
            self.parse_move("z'")
            self.parse_move("F")

    def parse_moves(self, move_str):
        """Performs the sequence of moves described by the given notation"""
        moves = move_str.split()
        for move in moves:
            self.parse_move(move)

    @staticmethod
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

    def scramble(self, n_moves=randint(25, 35)):
        """Performs a random sequence of moves to scramble the cube"""
        moves = [choice(self.basic_moves) + choice(self.modifiers)]
        while len(moves) < n_moves:
            new_move = choice(self.basic_moves) + choice(self.modifiers)

            # Check moves do not cancel each other
            if len(moves) < 1:
                moves.append(new_move)
                continue
            prev_move = moves[-1]
            res = self.check_result(prev_move, new_move)
            if res != prev_move + " " + new_move:
                moves = moves[:-1] + res.split()
                continue
            if len(moves) < 2:
                moves.append(new_move)
                continue
            if self.opposite.get(new_move[0]) != prev_move[0] and self.opposite.get(prev_move[0]) != new_move[0]:
                moves.append(new_move)
                continue
            prev_prev_move = moves[-2]
            res = self.check_result(prev_prev_move, new_move).split()
            if len(res) < 1:
                moves = moves[:-2] + [prev_move]
            elif len(res) < 2:
                moves = moves[:-2] + [prev_move] + res
            else:
                moves = moves[:-2] + [res[0]] + [prev_move] + [res[1]]

        moves_str = reduce(lambda a, b: a + " " + b, moves)
        self.parse_moves(moves_str)
