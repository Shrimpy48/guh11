import pygame, time
import tkinter as tk
from cube import Cube

class Gui:
    size = (800, 600) # window size
    margin = 10 # distance between cube and side
    gridSize = 20 # size of grids
    blackGrids = 1 # number of grids occupied by black plastic borders
    colourGrids = 3 # number of grids occupied by coloured stickers
    colourMap = {
        -1: (0, 0, 0),       # black for plastic
        -2: (100, 100, 100),  # grey for borders
        Cube.u: (255, 255, 255),    # white
        Cube.d: (255, 255, 0),      # yellow
        Cube.f: (0, 255, 0),        # green
        Cube.b: (0, 0, 255),        # blue
        Cube.r: (255, 0, 0),        # red
        Cube.l: (255, 127, 0)       # orange
    }
    edgeWidth = 2
    possibleWideableMoves = ["u", "d", "r", "l", "f", "b"]
    possibleMoves = ["x", "y", "z", "S", "M", "E"]

    def __init__(self):
        self.screen = pygame.display.set_mode(Gui.size)
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)

    def handle(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                moveButton = pygame.Rect(600, 100, 120, 30)
                scrambleButton = pygame.Rect(600, 300, 95, 30)
                if moveButton.collidepoint(pos):
                    return self.get_text()
                elif scrambleButton.collidepoint(pos):
                    return 1
            elif event.type == pygame.KEYDOWN:
                return self.handle_keypress(event.key)

    def handle_keypress(self, key):
        keys = pygame.key.get_pressed()
        outStr = ""
        slice = keys[pygame.K_RSHIFT]
        notOuterBlock = slice
        if key == pygame.K_s:
            outStr += "F" if not slice else "S"
        elif key == pygame.K_w:
            outStr += "U" if not slice else "E'"
        elif key == pygame.K_a:
            outStr += "L" if not slice else "M"
        elif key == pygame.K_d:
            outStr += "R" if not slice else "M'"
        elif key == pygame.K_q:
            outStr += "D" if not slice else "E"
        elif key == pygame.K_e:
            outStr += "B" if not slice else "S'"
        else:
            notOuterBlock = True
            if key == pygame.K_k:
                outStr += "x'"
            elif key == pygame.K_i:
                outStr += "x"
            elif key == pygame.K_j:
                outStr += "y"
            elif key == pygame.K_l:
                outStr += "y'"
            elif key == pygame.K_u:
                outStr += "z'"
            elif key == pygame.K_o:
                outStr += "z"
            else:
                return None
        if keys[pygame.K_LSHIFT] and not notOuterBlock:
            outStr += "'"
        if keys[pygame.K_LCTRL]:
            outStr += "2"
        if keys[pygame.K_LALT] and not notOuterBlock:
            outStr = outStr.lower()
        return outStr

    def get_text(self):
        while True:
            movesIn = self.input_from_window("Enter your moves: ")
            splitMoves = [move for move in movesIn.split(" ") if move != ""]
            possible = True
            for move in splitMoves:
                if move[0].lower() in Gui.possibleWideableMoves or move[0] in Gui.possibleMoves:
                    if len(move) <= 3:
                        if len(move) > 1:
                            if move[1] == "2" or move[1] == "'":
                                if len(move) == 3:
                                    if move[2] != "2" and move[2] != "'":
                                        possible = False
                            else:
                                possible = False
                    else:
                        possible = False
                else:
                    possible = False
                if not possible:
                    break
            if possible:
                return movesIn

    def input_from_window(self, labelStr):
        def get():
            nonlocal output
            output = entry.get()
            window.destroy()

        window = tk.Tk()
        window.geometry("300x100");

        label = tk.Label(window, text = labelStr)
        label.pack()

        entry = tk.Entry(window, width = 150)
        entry.pack()
        entry.focus_set()

        moveButton = tk.Button(window, text = "Enter", command = get)
        moveButton.pack()

        output = ""

        window.mainloop()
        print(output)
        return output

        

    def get_colour(self, face):
        return Gui.colourMap[face]

    def get_polygons(self, cubeData):
        sideGrids = Gui.colourGrids * 3 + Gui.blackGrids * 4
        polygons = []
        # black plastic
        polygons.append(
            (
                -1, 
                [
                    (0, sideGrids), (0, sideGrids * 2), (sideGrids, sideGrids * 2),
                    (sideGrids * 2, sideGrids), (sideGrids * 2, 0), (sideGrids, 0)
                ]
            )
        )
        # grey borders
        polygons.append(
            (
                -2,
                [
                    (0, sideGrids), (0, sideGrids * 2),
                    (sideGrids, sideGrids * 2), (sideGrids, sideGrids)
                ]
            )
        )
        polygons.append(
            (
                -2,
                [
                    (0, sideGrids), (sideGrids, sideGrids),
                    (sideGrids * 2, 0), (sideGrids, 0)
                ]
            )
        )
        polygons.append(
            (
                -2,
                [
                    (sideGrids, sideGrids), (sideGrids, sideGrids * 2),
                    (sideGrids * 2, sideGrids), (sideGrids * 2, 0)
                ]
            )
        )
        # front face
        for y in range(3):
            for x in range(3):
                colour = cubeData[Cube.f][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    sideGrids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    sideGrids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    sideGrids + (Gui.blackGrids + Gui.colourGrids)* (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    sideGrids + (Gui.blackGrids + Gui.colourGrids)* (y + 1))
                ]
                polygons.append((colour, points))
        # up face
        for y in range(3):
            for x in range(3):
                colour = cubeData[Cube.u][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    (Gui.blackGrids + Gui.colourGrids)* (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    (Gui.blackGrids + Gui.colourGrids)* (y + 1))
                ]
                skewedPoints = [(sideGrids + point[0] - point[1], point[1])
                                        for point in points]
                polygons.append((colour, skewedPoints))
        # right face
        for y in range(3):
            for x in range(3):
                colour = cubeData[Cube.r][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                    (Gui.blackGrids + Gui.colourGrids)* (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                    (Gui.blackGrids + Gui.colourGrids)* (y + 1))
                ]
                skewedPoints = [(sideGrids + point[0], sideGrids + point[1] - point[0])
                                        for point in points]
                polygons.append((colour, skewedPoints))
        return polygons

    def draw(self, cubeData):
        polygons = self.get_polygons(cubeData)
        self.screen.fill((255, 255, 255)) # white background
        for polygon in polygons:
            points = [(i[0] * Gui.gridSize + Gui.margin, i[1] * Gui.gridSize + Gui.margin)
                    for i in polygon[1]]
            width = Gui.edgeWidth if polygon[0] == -2 else 0
            colour = self.get_colour(polygon[0])
            pygame.draw.polygon(self.screen, colour, points, width)
        moveButton = pygame.Rect(600, 100, 120, 30)
        pygame.draw.rect(self.screen, (100, 100, 100), moveButton)
        moveText = self.font.render("Enter Moves", True, (255, 255, 255))
        self.screen.blit(moveText, dest=(610, 108))

        scrambleButton = pygame.Rect(600, 300, 95, 30)
        pygame.draw.rect(self.screen, (100, 100, 100), scrambleButton)
        scrambleText = self.font.render("Scramble", True, (255, 255, 255))
        self.screen.blit(scrambleText, dest=(610, 308))

        pygame.display.flip()