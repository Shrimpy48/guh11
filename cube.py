class Cube:
    u = 0
    l = 1
    f = 2
    r = 3
    b = 4
    d = 5

    def __init__(self):
        self.data = [[[k for i in range(3)] for j in range(3)] for k in range(6)]


    # debugging function
    def print_net(self):
        for i in self.data[0]:
            print("      ", i)
        for i in range(3):
            for j in range(4):
                print(self.data[j+1][i], end="  ")
            print()
        for i in self.data[5]:
            print("      ", i)


    def turn_face(self, face):
        self.data[face][0][0], self.data[face][0][1], self.data[face][0][2], self.data[face][1][0], self.data[face][1][2], self.data[face][2][0], self.data[face][2][1], self.data[face][2][2] = self.data[face][2][0], self.data[face][1][0], self.data[face][0][0], self.data[face][2][1], self.data[face][0][1], self.data[face][2][2], self.data[face][1][2], self.data[face][0][2]

    def turn_layer(self, face):
        self.data[1] = [[1,2,3],[4,5,6],[7,8,9]]
        self.data[0] = [[11,0,"c"],[12,0,"b"],[13,0,"a"]]
        self.data[4] = [["d",0,22],["e",0,21],["f",0,20]]
        self.data[5] = [[17,0,"i"],[18,0,"h"],[19,0,"g"]]
        self.data[2] = [[14,0,"l"],[15,0,"k"],[16,0,"j"]]
        self.print_net()


        self.turn_face(face)

        if face == self.r:
            #self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[3][0][1], self.data[3][2][1], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0] = self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[3][1][0], self.data[3][1][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2]
            self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2], self.data[2][2][2], self.data[2][1][2], self.data[2][0][2] = self.data[2][2][2], self.data[2][1][2], self.data[2][0][2], self.data[0][2][2], self.data[0][1][2], self.data[0][0][2], self.data[4][0][0], self.data[4][1][0], self.data[4][2][0], self.data[5][2][2], self.data[5][1][2], self.data[5][0][2]

        if face == self.l:
            #self.data[1][0][0], self.data[1][0][1], self.data[1][0][2], self.data[1][1][0], self.data[1][1][2], self.data[1][2][0], self.data[1][2][1], self.data[1][2][2] = self.data[1][2][0], self.data[1][1][0], self.data[1][0][0], self.data[1][2][2], self.data[1][0][1], self.data[1][2][2], self.data[1][1][2], self.data[1][0][2]
            self.data[0][0][0], self.data[0][1][0], self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], self.data[2][2][0], self.data[5][0][0], self.data[5][1][0], self.data[5][2][0], self.data[4][2][2], self.data[4][1][2], self.data[4][0][2] = self.data[4][2][2], self.data[4][1][2], self.data[4][0][2], self.data[0][0][0], self.data[0][1][0], self.data[0][2][0], self.data[2][0][0], self.data[2][1][0], self.data[2][2][0], self.data[5][0][0], self.data[5][1][0], self.data[5][2][0]

        if face == self.u:
            #self.data[0][0][0], self.data[0][0][1], self.data[0][0][2], self.data[0][1][0], self.data[0][1][2], self.data[0][2][0], self.data[0][2][1], self.data[0][2][2] = self.data[0][2][0], self.data[0][1][0], self.data[0][0][0], self.data[0][2][2], self.data[0][0][1], self.data[0][2][2], self.data[0][1][2], self.data[0][0][2]
            self.data[1][0][0], self.data[1][0][1], self.data[1][0][2], self.data[2][0][0], self.data[2][0][1], self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[4][0][0], self.data[4][0][1], self.data[4][0][2] = self.data[2][0][0], self.data[2][0][1], self.data[2][0][2], self.data[3][0][0], self.data[3][0][1], self.data[3][0][2], self.data[4][0][0], self.data[4][0][1], self.data[4][0][2], self.data[1][0][0], self.data[1][0][1], self.data[1][0][2]

        if face == self.f:
            self.data[0][2][0], self.data[0][2][1], self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0], self.data[5][0][2], self.data[5][0][1], self.data[5][0][0], self.data[1][2][2], self.data[1][1][2], self.data[1][0][2] = self.data[1][2][2], self.data[1][1][2], self.data[1][0][2], self.data[0][2][0], self.data[0][2][1], self.data[0][2][2], self.data[3][0][0], self.data[3][1][0], self.data[3][2][0], self.data[5][0][2], self.data[5][0][1], self.data[5][0][0]

        if face == self.d:
            self.data[1][2][0], self.data[1][2][1], self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], self.data[2][2][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2], self.data[4][2][0], self.data[4][2][1], self.data[4][2][2] = self.data[4][2][0], self.data[4][2][1], self.data[4][2][2], self.data[1][2][0], self.data[1][2][1], self.data[1][2][2], self.data[2][2][0], self.data[2][2][1], self.data[2][2][2], self.data[3][2][0], self.data[3][2][1], self.data[3][2][2]

        if face == self.b:
            self.data[0][0][0], self.data[0][0][1], self.data[0][0][2], self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], self.data[5][2][0], self.data[1][2][0], self.data[1][1][0], self.data[1][0][0] = self.data[3][0][2], self.data[3][1][2], self.data[3][2][2], self.data[5][2][2], self.data[5][2][1], self.data[5][2][0], self.data[1][2][0], self.data[1][1][0], self.data[1][0][0], self.data[0][0][0], self.data[0][0][1], self.data[0][0][2]

        self.print_net()


cube = Cube()
cube.turn_layer(cube.b)
