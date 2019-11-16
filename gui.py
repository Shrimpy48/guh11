import pygame
import tkinter as tk
from time import sleep

from cube import Cube
from scrambler import get_scramble


class Gui:
    size = (800, 600)  # window size
    margin = 10  # distance between cube and side
    gridSize = 20  # size of grids
    blackGrids = 1  # number of grids occupied by black plastic borders
    colourGrids = 3  # number of grids occupied by coloured stickers
    colourMap = {
        -1: (0, 0, 0),  # black for plastic
        -2: (100, 100, 100),  # grey for borders
        Cube.u: (255, 255, 255),  # white
        Cube.d: (255, 255, 0),  # yellow
        Cube.f: (0, 255, 0),  # green
        Cube.b: (0, 0, 255),  # blue
        Cube.r: (255, 0, 0),  # red
        Cube.l: (255, 127, 0)  # orange
    }
    edgeWidth = 2
    possibleWideableMoves = ["u", "d", "r", "l", "f", "b"]
    possibleMoves = ["x", "y", "z", "S", "M", "E"]

    def __init__(self, cube):
        self.screen = pygame.display.set_mode(Gui.size)
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)
        self.cube = cube

    def handle(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                move_button = pygame.Rect(600, 100, 120, 30)
                scramble_button = pygame.Rect(600, 300, 95, 30)
                if move_button.collidepoint(pos):
                    return self.get_text()
                elif scramble_button.collidepoint(pos):
                    return 1
            elif event.type == pygame.KEYDOWN:
                return self.handle_keypress(event.key)

    @staticmethod
    def handle_keypress(key):
        keys = pygame.key.get_pressed()
        out_str = ""
        slice_mode = keys[pygame.K_RSHIFT]
        not_outer_block = slice_mode
        if key == pygame.K_s:
            out_str += "F" if not slice_mode else "S"
        elif key == pygame.K_w:
            out_str += "U" if not slice_mode else "E'"
        elif key == pygame.K_a:
            out_str += "L" if not slice_mode else "M"
        elif key == pygame.K_d:
            out_str += "R" if not slice_mode else "M'"
        elif key == pygame.K_q:
            out_str += "D" if not slice_mode else "E"
        elif key == pygame.K_e:
            out_str += "B" if not slice_mode else "S'"
        else:
            not_outer_block = True
            if key == pygame.K_k:
                out_str += "x'"
            elif key == pygame.K_i:
                out_str += "x"
            elif key == pygame.K_j:
                out_str += "y"
            elif key == pygame.K_l:
                out_str += "y'"
            elif key == pygame.K_u:
                out_str += "z'"
            elif key == pygame.K_o:
                out_str += "z"
            else:
                return None
        if keys[pygame.K_LSHIFT] and not not_outer_block:
            out_str += "'"
        if keys[pygame.K_LCTRL]:
            out_str += "2"
        if keys[pygame.K_LALT] and not not_outer_block:
            out_str = out_str.lower()
        return out_str

    def get_text(self):
        while True:
            moves_in = self.input_from_window("Enter your moves: ")
            split_moves = [move for move in moves_in.split(" ") if move != ""]
            possible = True
            for move in split_moves:
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
                return moves_in

    @staticmethod
    def input_from_window(label_str):
        def get():
            nonlocal output
            output = entry.get()
            window.destroy()

        window = tk.Tk()
        window.geometry("300x100")

        label = tk.Label(window, text=label_str)
        label.pack()

        entry = tk.Entry(window, width=150)
        entry.pack()
        entry.focus_set()

        move_button = tk.Button(window, text="Enter", command=get)
        move_button.pack()

        output = ""

        window.mainloop()
        return output

    @staticmethod
    def get_colour(face):
        return Gui.colourMap[face]

    def get_polygons(self):
        side_grids = Gui.colourGrids * 3 + Gui.blackGrids * 4
        polygons = [
            # black plastic
            (-1, [
                (0, side_grids), (0, side_grids * 2), (side_grids, side_grids * 2),
                (side_grids * 2, side_grids), (side_grids * 2, 0), (side_grids, 0)
            ]),
            # grey borders
            (-2, [
                (0, side_grids), (0, side_grids * 2),
                (side_grids, side_grids * 2), (side_grids, side_grids)
            ]),
            (-2, [
                (0, side_grids), (side_grids, side_grids),
                (side_grids * 2, 0), (side_grids, 0)
            ]),
            (-2, [
                (side_grids, side_grids), (side_grids, side_grids * 2),
                (side_grids * 2, side_grids), (side_grids * 2, 0)
            ])]

        # front face
        for y in range(3):
            for x in range(3):
                colour = self.cube.data[Cube.f][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     side_grids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     side_grids + Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     side_grids + (Gui.blackGrids + Gui.colourGrids) * (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     side_grids + (Gui.blackGrids + Gui.colourGrids) * (y + 1))
                ]
                polygons.append((colour, points))
        # up face
        for y in range(3):
            for x in range(3):
                colour = self.cube.data[Cube.u][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     (Gui.blackGrids + Gui.colourGrids) * (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     (Gui.blackGrids + Gui.colourGrids) * (y + 1))
                ]
                skewed_points = [(side_grids + point[0] - point[1], point[1])
                                 for point in points]
                polygons.append((colour, skewed_points))
        # right face
        for y in range(3):
            for x in range(3):
                colour = self.cube.data[Cube.r][y][x]
                points = [
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     Gui.blackGrids * (y + 1) + Gui.colourGrids * y),
                    ((Gui.blackGrids + Gui.colourGrids) * (x + 1),
                     (Gui.blackGrids + Gui.colourGrids) * (y + 1)),
                    (Gui.blackGrids * (x + 1) + Gui.colourGrids * x,
                     (Gui.blackGrids + Gui.colourGrids) * (y + 1))
                ]
                skewed_points = [(side_grids + point[0], side_grids + point[1] - point[0])
                                 for point in points]
                polygons.append((colour, skewed_points))
        return polygons

    def draw(self):
        polygons = self.get_polygons()
        self.screen.fill((255, 255, 255))  # white background
        for polygon in polygons:
            points = [(i[0] * Gui.gridSize + Gui.margin, i[1] * Gui.gridSize + Gui.margin)
                      for i in polygon[1]]
            width = Gui.edgeWidth if polygon[0] == -2 else 0
            colour = self.get_colour(polygon[0])
            pygame.draw.polygon(self.screen, colour, points, width)
        move_button = pygame.Rect(600, 100, 120, 30)
        pygame.draw.rect(self.screen, (100, 100, 100), move_button)
        move_text = self.font.render("Enter Moves", True, (255, 255, 255))
        self.screen.blit(move_text, dest=(610, 108))

        scramble_button = pygame.Rect(600, 300, 95, 30)
        pygame.draw.rect(self.screen, (100, 100, 100), scramble_button)
        scramble_text = self.font.render("Scramble", True, (255, 255, 255))
        self.screen.blit(scramble_text, dest=(610, 308))

        pygame.display.flip()

    def apply_moves(self, moves_str):
        for move in moves_str.split():
            sleep(0.05)
            self.cube.parse_move(move)
            self.draw()

    def run(self):
        while True:
            action = self.handle()
            if action == -1:
                break
            elif action == 1:
                self.apply_moves(get_scramble())
            else:
                self.draw()
                if action is not None:
                    self.apply_moves(action)
