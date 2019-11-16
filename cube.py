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

    def __init__(self):
        self.data = [[[k for i in range(3)] for j in range(3)] for k in range(6)]

    # debugging functions
    def print_net(self):
        for i in self.data[0]:
            print("      ", i)
        for i in range(3):
            for j in range(4):
                print(self.data[j+1][i], end="  ")
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
        self.data[face][0][0], self.data[face][0][1], self.data[face][0][2], self.data[face][1][0], self.data[face][1][2], self.data[face][2][0], self.data[face][2][1], self.data[face][2][2] = self.data[face][2][0], self.data[face][1][0], self.data[face][0][0], self.data[face][2][1], self.data[face][0][1], self.data[face][2][2], self.data[face][1][2], self.data[face][0][2]

    def turn_layer(self, face):
        self.turn_face(face)

        if face == self.r:
            self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2], self.data[2][2][2], self.data[2][1][2], self.data[2][0][2] = self.data[2][2][2], self.data[2][1][2], self.data[2][0][2], self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2]

        elif face == self.l:
            self.data[0][0][0], self.data[0][1][0], self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], self.data[2][2][0], self.data[5][0][0], self.data[5][1][0], self.data[5][2][0], self.data[4][2][2], self.data[4][1][2], self.data[4][0][2] = self.data[4][2][2], self.data[4][1][2], self.data[4][0][2], self.data[0][0][0], self.data[0][1][0], self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], self.data[2][2][0], self.data[5][0][0], self.data[5][1][0], self.data[5][2][0]

        elif face == self.u:
            self.data[1][0][0], self.data[1][0][1], self.data[1][0][2], self.data[2][0][0], self.data[2][0][1], self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[4][0][0], self.data[4][0][1], self.data[4][0][2] = self.data[2][0][0], self.data[2][0][1], self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[4][0][0], self.data[4][0][1], self.data[4][0][2], self.data[1][0][0], self.data[1][0][1], self.data[1][0][2]

        elif face == self.f:
            self.data[0][2][0], self.data[0][2][1], self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0], self.data[5][0][2], self.data[5][0][1], self.data[5][0][0], self.data[1][2][2], self.data[1][1][2], self.data[1][0][2] = self.data[1][2][2], self.data[1][1][2], self.data[1][0][2], self.data[0][2][0], self.data[0][2][1], self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0], self.data[5][0][2], self.data[5][0][1], self.data[5][0][0]

        elif face == self.d:
            self.data[1][2][0], self.data[1][2][1], self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], self.data[2][2][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2], self.data[4][2][0], self.data[4][2][1], self.data[4][2][2] = self.data[4][2][0], self.data[4][2][1], self.data[4][2][2], self.data[1][2][0], self.data[1][2][1], self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], self.data[2][2][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2]

        elif face == self.b:
            self.data[0][0][0], self.data[0][0][1], self.data[0][0][2], self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], self.data[5][2][0], self.data[1][2][0], self.data[1][1][0], self.data[1][0][0] = self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], self.data[5][2][0], self.data[1][2][0], self.data[1][1][0], self.data[1][0][0], self.data[0][0][0], self.data[0][0][1], self.data[0][0][2]

    @staticmethod
    def reverse_face(face):
        return list(reversed([list(reversed(row)) for row in face]))

    def rotate(self, axis):
        if axis == self.x:
            # clockwise around R
            # r, l', f -> u -> b -> d
            self.turn_face(self.r)
            for i in range(3):
                self.turn_face(self.l)
            self.data[2], self.data[0], self.data[4], self.data[5] = self.data[5], self.data[2], self.reverse_face(self.data[0]), self.reverse_face(self.data[4])
        elif axis == self.y:
            # clockwise around U
            # u, d', f -> l -> b -> r
            self.turn_face(self.u)
            for i in range(3):
                self.turn_face(self.d)
            self.data[2], self.data[1], self.data[4], self.data[3] = self.data[3], self.data[2], self.data[1], self.data[4]
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
        if len(move) == 3:
            move = move.replace("'", "")
        if move[-1] == "'":
            move = move[:-1]
            self.parse_move(move + "2")
        elif move[-1] == "2":
            move = move[:-1]
            self.parse_move(move)
        # if move[0] != "2" and move[-1] != "'":
        
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
        moves = move_str.split()
        for move in moves:
            self.parse_move(move)



cube = Cube()
cube.init_cube()
cube.rotate(cube.x)
