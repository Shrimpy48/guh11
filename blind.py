from cube import Cube

cube = Cube()

cube.data = [[[0,4,1],[1,0,4],[4,4,1]],
            [[2,0,4],[5,1,2],[3,0,4]],
            [[5,1,2],[0,2,4],[0,3,5]],
            [[3,0,3],[3,3,1],[2,1,2]],
            [[5,5,5],[5,4,2],[1,2,4]],
            [[1,5,3],[3,5,2],[0,3,0]]]

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

def find_correct_corner_pos(sticker, left, right):
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
    

def get_blind(cube):
    rotate_home(cube)

    print("corners")


print(find_corner_pos(5,2,1))

