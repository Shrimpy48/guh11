from cube import Cube

cube = Cube()

cube.data = [[[0,4,1],
            [1,0,4],
            [4,4,1]],
[[2,0,4],
[5,1,2],
[3,0,4]],
        [[5,1,2],
        [0,2,4],
        [0,3,5]],
               [[3,0,3],
               [3,3,1],
               [2,1,2]],
                        [[5,5,5],
                        [5,4,2],
                        [1,2,4]],
            [[1,5,3],
            [3,5,2],
            [0,3,0]]]

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

face_mappings = [[4,3,2,1],
                [0,2,5,4],
                [0,3,5,1],
                [0,4,5,2],
                [0,1,5,3],
                [2,3,4,1]]

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

def get_pos_from_edge(sticker, opposite):
    solved = Cube()
    for i in range(6):
        if solved.data[i][1][1] == sticker:
            for j in range(4):
                if opposite == face_mappings[i][j]:
                    sticker_pos = [[i,0,1],[i,1,2],[i,2,1],[i,1,0]][j]
                    return sticker_pos
    return "something went wrong"

def get_edge_from_pos(cube, position):
    # position = [face, row, col]
    face = position[0]
    sticker = cube.data[face][position[1]][position[2]]
    i = [[0,1],[1,2],[2,1],[1,0]].index([position[1],position[2]])
    opposite_face = face_mappings[face][i]
    opposite_loc = [[0,1],[1,2],[2,1],[1,0]][face_mappings[opposite_face].index(face)]
    opposite = cube.data[opposite_face][opposite_loc[0]][opposite_loc[1]]

    print(sticker, opposite)
    return [sticker, opposite]


def get_blind(cube):
    rotate_home(cube)
    print("corners")

    corners_str = ""

    edge = get_edge_from_pos(cube, [0,1,2])
    to_pos = get_pos_from_edge(edge[0], edge[1])

    corners_str += " " + letter_scheme[to_pos[0]][to_pos[1]][to_pos[2]]

    while True:
        edge = get_edge_from_pos(cube, to_pos)
        to_pos = get_pos_from_edge(edge[0], edge[1])
        corners_str += " " + letter_scheme[to_pos[0]][to_pos[1]][to_pos[2]]
        if to_pos in  [[0,1,2],[3,1,0]]:
            break

    print(corners_str)

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

