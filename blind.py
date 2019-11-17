from cube import Cube
from random import choice
from scrambler import get_scrambled_cube_with_moves

cube = Cube()

cube, moves = get_scrambled_cube_with_moves(cube)
print(moves)
print()

def rotate_home(cube):
    for i in range(6):
        if cube.data[i][1][1] == 0:
            # if center white
            white = i
            break
    if white == 1:
        cube.parse_move("z")
    elif white == 2:
        cube.parse_move("x")
    elif white == 3:
        cube.parse_move("z'")
    elif white == 4:
        cube.parse_move("x'")
    elif white == 5:
        cube.parse_move("x2")

    for i in range(1,5):
        if cube.data[i][1][1] == 2:
            # if green center
            green = i
            break
    if green == 1:
        cube.parse_move("y")
    elif green == 3:
        cube.parse_move("y'")
    elif green == 4:
        cube.parse_move("y2")

def get_pos_from_corner(sticker, left, right):
    solved = Cube()
    for i in range(6):
        if solved.data[i][1][1] == sticker:
            # i is the correct face
            for j in range(4):
                if left == face_mappings[i][j]:
                    if right == face_mappings[i][j-1]:
                        sticker_pos = [[i,0,0],[i,0,2],[i,2,2],[i,2,0]][j]
                        return sticker_pos
                    else:
                        print("something has gone very wrong")
                        return

def get_corner_from_pos(cube, position):
    # cube = Cube() and position = [face,row,col]
    face = position[0]
    sticker = cube.data[face][position[1]][position[2]]
    i = [[0,0],[0,2],[2,2],[2,0]].index([position[1],position[2]])
    left_face = face_mappings[face][i]
    right_face = face_mappings[face][i-1]
    right_loc = [[0,0],[0,2],[2,2],[2,0]][face_mappings[right_face].index(face)]
    right_sticker = cube.data[right_face][right_loc[0]][right_loc[1]]

    left_loc = [[0,0],[0,2],[2,2],[2,0]][face_mappings[left_face].index(face)-3]
    left_sticker = cube.data[left_face][left_loc[0]][left_loc[1]]

    return [sticker, left_sticker, right_sticker]

# Returns the position where an edge should be, given it's colours
def get_pos_from_edge(sticker, opposite):
    solved = Cube()
    for i in range(6):
        if solved.data[i][1][1] == sticker:
            for j in range(4):
                if opposite == face_mappings[i][j]:
                    sticker_pos = [[i,0,1],[i,1,2],[i,2,1],[i,1,0]][j]
                    return sticker_pos
    return "something went wrong"

# Returns the colours of an edge, given the position on the cube in indices
def get_edge_from_pos(cube, position):
    # position = [face, row, col]
    face = position[0]
    sticker = cube.data[face][position[1]][position[2]]
    i = [[0,1],[1,2],[2,1],[1,0]].index([position[1],position[2]])
    opposite_face = face_mappings[face][i]
    opposite_loc = [[0,1],[1,2],[2,1],[1,0]][face_mappings[opposite_face].index(face)]
    opposite = cube.data[opposite_face][opposite_loc[0]][opposite_loc[1]]

    return [sticker, opposite]


def get_blind(cube):

    def set_visited_edge(position):
        if position in [[0, 0, 1], [4, 0, 1]]:
            visited_edge[0] = 1
        elif position in [[0, 1, 2], [3, 0, 1]]:
            visited_edge[1] = 1
        elif position in [[0, 2, 1], [2, 0, 1]]:
            visited_edge[2] = 1
        elif position in [[0, 1, 0], [1, 0, 1]]:
            visited_edge[3] = 1
        elif position in [[1, 1, 2], [2, 1, 0]]:
            visited_edge[4] = 1
        elif position in [[2, 1, 2], [3, 1, 0]]:
            visited_edge[5] = 1
        elif position in [[3, 1, 2], [4, 1, 0]]:
            visited_edge[6] = 1
        elif position in [[4, 1, 2], [1, 1, 0]]:
            visited_edge[7] = 1
        elif position in [[2, 2, 1], [5, 0, 1]]:
            visited_edge[8] = 1
        elif position in [[3, 2, 1], [5, 1, 2]]:
            visited_edge[9] = 1
        elif position in [[4, 2, 1], [5, 2, 1]]:
            visited_edge[10] = 1
        elif position in [[1, 2, 1], [5, 1, 0]]:
            visited_edge[11] = 1

    def check_visited_edge(position):
        if position in [[0, 0, 1], [4, 0, 1]]:
            return visited_edge[0] == 1
        elif position in [[0, 1, 2], [3, 0, 1]]:
            return visited_edge[1] == 1
        elif position in [[0, 2, 1], [2, 0, 1]]:
            return visited_edge[2] == 1
        elif position in [[0, 1, 0], [1, 0, 1]]:
            return visited_edge[3] == 1
        elif position in [[1, 1, 2], [2, 1, 0]]:
            return visited_edge[4] == 1
        elif position in [[2, 1, 2], [3, 1, 0]]:
            return visited_edge[5] == 1
        elif position in [[3, 1, 2], [4, 1, 0]]:
            return visited_edge[6] == 1
        elif position in [[4, 1, 2], [1, 1, 0]]:
            return visited_edge[7] == 1
        elif position in [[2, 2, 1], [5, 0, 1]]:
            return visited_edge[8] == 1
        elif position in [[3, 2, 1], [5, 1, 2]]:
            return visited_edge[9] == 1
        elif position in [[4, 2, 1], [5, 2, 1]]:
            return visited_edge[10] == 1
        elif position in [[1, 2, 1], [5, 1, 0]]:
            return visited_edge[11] == 1

    def set_visited_corner(position):
        if position in [[0, 0, 0], [1, 0, 0], [4, 0, 2]]:
            visited_corner[0] = 1
        elif position in [[0, 0, 2], [3, 0, 2], [4, 0, 0]]:
            visited_corner[1] = 1
        elif position in [[0, 2, 2], [2, 0, 2], [3, 0, 0]]:
            visited_corner[2] = 1
        elif position in [[0, 2, 0], [1, 0, 2], [2, 0, 0]]:
            visited_corner[3] = 1
        elif position in [[5, 2, 0], [1, 2, 0], [4, 2, 2]]:
            visited_corner[4] = 1
        elif position in [[5, 2, 2], [3, 2, 2], [4, 2, 0]]:
            visited_corner[5] = 1
        elif position in [[5, 0, 2], [2, 2, 2], [3, 2, 0]]:
            visited_corner[6] = 1
        elif position in [[5, 0, 0], [1, 2, 2], [2, 2, 0]]:
            visited_corner[7] = 1

    def check_visited_corner(position):
        if position in [[0, 0, 0], [1, 0, 0], [4, 0, 2]]:
            return visited_corner[0] == 1
        elif position in [[0, 0, 2], [3, 0, 2], [4, 0, 0]]:
            return visited_corner[1] == 1
        elif position in [[0, 2, 2], [2, 0, 2], [3, 0, 0]]:
            return visited_corner[2] == 1
        elif position in [[0, 2, 0], [1, 0, 2], [2, 0, 0]]:
            return visited_corner[3] == 1
        elif position in [[5, 2, 0], [1, 2, 0], [4, 2, 2]]:
            return visited_corner[4] == 1
        elif position in [[5, 2, 2], [3, 2, 2], [4, 2, 0]]:
            return visited_corner[5] == 1
        elif position in [[5, 0, 2], [2, 2, 2], [3, 2, 0]]:
            return visited_corner[6] == 1
        elif position in [[5, 0, 0], [1, 2, 2], [2, 2, 0]]:
            return visited_corner[7] == 1

    visited_edge = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    visited_corner = [0, 0, 0, 0, 0, 0, 0, 0]

    rotate_home(cube)

    # Edges

    edge_str = ""

    to_pos = [0, 1, 2]
    set_visited_edge(to_pos)

    while True:
        edge = get_edge_from_pos(cube, to_pos)
        to_pos = get_pos_from_edge(edge[0], edge[1])
        if check_visited_edge(to_pos):
            if 0 not in visited_edge:
                break
            else:
                while check_visited_edge(to_pos):
                    to_pos = choice([[i] + lst for lst in [[0,1],[1,0],[1,2],[2,1]] for i in range(6)])
        else:
            set_visited_edge(to_pos)
        edge_str += " " + letter_scheme[to_pos[0]][to_pos[1]][to_pos[2]]

    edges = edge_str.split()
    i = 0
    while i<len(edges)-1:
        if edges[i] == edges[i+1]:
            del edges[i:i+2]
        else:
            i += 1

    edge_str = ""
    for i in edges:
        edge_str += " " + i

    # corners

    corner_str = ""

    to_pos = [0, 0, 0]
    set_visited_corner(to_pos)

    while True:
        corner = get_corner_from_pos(cube, to_pos)
        to_pos = get_pos_from_corner(corner[0], corner[1], corner[2])
        if check_visited_corner(to_pos):
            if 0 not in visited_corner:
                break
            else:
                while check_visited_corner(to_pos):
                    to_pos = choice([[i] + lst for lst in [[0,0],[0,2],[2,0],[2,2]] for i in range(6)])
        else:
            set_visited_corner(to_pos)
        corner_str += " " + letter_scheme[to_pos[0]][to_pos[1]][to_pos[2]]

    corners = corner_str.split()
    i = 0
    while i < len(corners)-1:
        if corners[i] == corners[i+1]:
            del corners[i:i+2]
        else:
            i += 1

    corner_str = ""
    for i in corners:
        corner_str += " " + i

    print("Edges:")
    print(edge_str)

    parity = False
    if len(edge_str)%2 == 1:
        parity = True
        print("\nParity detected")

    print("\nCorners:")
    print(corner_str)

    return edges, corners, parity


face_mappings = [[4,3,2,1],
                [0,2,5,4],
                [0,3,5,1],
                [0,4,5,2],
                [0,1,5,3],
                [2,3,4,1]]

letter_scheme = [[["A","A","B"],
                  ["D","0","B"],
                  ["D","C","C"]],

                 [["E","E","F"],
                  ["H","0","F"],
                  ["H","G","G"]],

                 [["I","I","J"],
                  ["L","0","J"],
                  ["L","K","K"]],

                 [["M","M","N"],
                  ["P","0","N"],
                  ["P","O","O"]],

                 [["Q","Q","R"],
                  ["T","0","R"],
                  ["T","S","S"]],

                 [["U","U","V"],
                  ["X","0","V"],
                  ["X","W","W"]],]


get_blind(cube)