import pygame
import tkinter as tk
from tkinter import messagebox
from itertools import chain

from cube import Cube
from scrambler import get_scramble, get_scramble_iterator
from blind import get_blind
from algs import algs


class Gui:
    size = (1100, 700)  # window size
    margin = 30  # distance between cube and side
    gridSize = 20  # size of grids
    blackGrids = 1  # number of grids occupied by black plastic borders
    colourGrids = 3  # number of grids occupied by coloured stickers
    colourMap = {
        -1: (0, 0, 0),  # black for plastic
        -2: (100, 100, 100),  # grey for borders
        Cube.u: (250, 250, 250),  # white
        Cube.d: (245, 255, 0),  # yellow
        Cube.f: (0, 220, 0),  # green
        Cube.b: (10, 0, 255),  # blue
        Cube.r: (255, 0, 0),  # red
        Cube.l: (255, 136, 0)  # orange
    }
    edgeWidth = 2
    sideMultiplier = 0.7
    possibleWideableMoves = ["u", "d", "r", "l", "f", "b"]
    possibleMoves = ["x", "y", "z", "S", "M", "E"]

    button_x = 600
    button_y = 150
    button_width = 210
    button_height = 30
    button_sep = 10

    keybinds_str = """Keybinds:
w = U          i = x
a = L          j = y
s = F          k = x'
d = R          l = y'
q = D          u = z'
e = B          o = z
RShift+w = E'  LShift+<c> = c'
RShift+a = M   LCtrl+<c> = c2
RShift+s = S   LAlt+<c> = Cw
RShift+d = M'
RShift+q = E
RShift+e = S'"""

    def __init__(self, cube):
        self.screen = pygame.display.set_mode(Gui.size)
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 16)
        self.mono_font = pygame.font.Font(pygame.font.match_font('mono'), 14)
        self.cube = cube
        self.moves = iter([])
        self.buttons = []

    @staticmethod
    def map_keypress(key):
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

    def make_button(self, text, x, y, width, height, on_click):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, (100, 100, 100), button)
        button_text = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(button_text, dest=(x + 10, y + 8))
        button_clicker = pygame.Rect(x, y, width, height)
        self.buttons.append((button_clicker, on_click))

    def get_polygons(self):
        side_grids = Gui.colourGrids * 3 + Gui.blackGrids * 4
        polygons = [
            # black plastic
            (-1, [
                (0, side_grids), (0, side_grids * 2), (side_grids, side_grids * 2),
                (side_grids * (1 + Gui.sideMultiplier), side_grids * (2 - Gui.sideMultiplier)),
                (side_grids * (1 + Gui.sideMultiplier), side_grids * (1 - Gui.sideMultiplier)),
                (side_grids * Gui.sideMultiplier, side_grids * (1 - Gui.sideMultiplier))
            ]),
            # grey borders
            (-2, [
                (0, side_grids), (0, side_grids * 2),
                (side_grids, side_grids * 2), (side_grids, side_grids)
            ]),
            (-2, [
                (0, side_grids), (side_grids, side_grids),
                (side_grids * (1 + Gui.sideMultiplier), side_grids * (1 - Gui.sideMultiplier)),
                (side_grids * Gui.sideMultiplier, side_grids * (1 - Gui.sideMultiplier))
            ]),
            (-2, [
                (side_grids, side_grids), (side_grids, side_grids * 2),
                (side_grids * (1 + Gui.sideMultiplier), side_grids * (2 - Gui.sideMultiplier)),
                (side_grids * (1 + Gui.sideMultiplier), side_grids * (1 - Gui.sideMultiplier))
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
                skewed_points = [(side_grids * Gui.sideMultiplier + point[0] - point[1] * Gui.sideMultiplier,
                    side_grids * (1 - Gui.sideMultiplier) + point[1] * Gui.sideMultiplier)
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
                skewed_points = [(side_grids + point[0] * Gui.sideMultiplier, 
                    side_grids + point[1] - point[0] * Gui.sideMultiplier)
                                 for point in points]
                polygons.append((colour, skewed_points))
        return polygons

    def draw(self, background=(204, 204, 204)):

        self.buttons = []

        polygons = self.get_polygons()
        self.screen.fill(background)  # white background
        for polygon in polygons:
            points = [(i[0] * Gui.gridSize + Gui.margin, i[1] * Gui.gridSize + Gui.margin)
                      for i in polygon[1]]
            width = Gui.edgeWidth if polygon[0] == -2 else 0
            colour = self.get_colour(polygon[0])
            pygame.draw.polygon(self.screen, colour, points, width)

        bee_pic = pygame.image.load("media/logo_small.png")
        self.screen.blit(bee_pic, dest=(627, 40))

        self.make_button("Enter Moves", self.button_x, self.button_y, self.button_width, self.button_height,
                         lambda: self.apply_moves(self.get_text().split()))

        self.make_button("Find Positions", self.button_x, self.button_y + self.button_height + self.button_sep,
                         self.button_width, self.button_height, self.show_blind)

        self.make_button("Scramble", self.button_x, self.button_y + 2 * (self.button_height + self.button_sep),
                         self.button_width, self.button_height, lambda: self.apply_moves(get_scramble()))

        self.make_button("Scramble Continuously", self.button_x,
                         self.button_y + 3 * (self.button_height + self.button_sep), self.button_width,
                         self.button_height, lambda: self.apply_moves(get_scramble_iterator()))

        self.make_button("Stop", self.button_x, self.button_y + 4 * (self.button_height + self.button_sep),
                         self.button_width, self.button_height, self.clear_moves)

        self.make_button("Solve", self.button_x, self.button_y + 5 * (self.button_height + self.button_sep),
                         self.button_width, self.button_height, self.reset)

        i = 0
        for name, moves in algs.items():
            self.make_button(name, self.button_x, self.button_y + (6 + i) * (self.button_height + self.button_sep),
                         self.button_width, self.button_height, lambda x=moves: self.apply_moves(x.split()))
            i += 1

        keybinds_start = 830, 150
        offset = 0
        for line in self.keybinds_str.splitlines(False):
            line_text = self.mono_font.render(line, True, (0, 0, 0))
            self.screen.blit(line_text, dest=(keybinds_start[0], keybinds_start[1] + offset))
            offset += line_text.get_height() + 2

        pygame.display.flip()

    def redraw(self):
        polygons = self.get_polygons()
        for polygon in polygons:
            points = [(i[0] * Gui.gridSize + Gui.margin, i[1] * Gui.gridSize + Gui.margin)
                      for i in polygon[1]]
            width = Gui.edgeWidth if polygon[0] == -2 else 0
            colour = self.get_colour(polygon[0])
            pygame.draw.polygon(self.screen, colour, points, width)

        pygame.display.update(pygame.Rect(50, 100, 450, 500))

    def apply_moves(self, moves):
        self.moves = chain(self.moves, moves)

    def show_blind(self):
        edges, corners, parity = get_blind(self.cube)
        msg = "Edges: "
        if len(edges) < 1:
            msg += "None"
        else:
            msg += edges
        msg += "\n"
        if parity:
            msg += "There is parity\n"
        msg += "Corners: "
        if len(corners) < 1:
            msg += "None"
        else:
            msg += corners
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Blind Letters", msg)
        root.destroy()

    def clear_moves(self):
        self.moves = iter([])

    def reset(self):
        self.cube = Cube()

    def run(self, move_period=100):
        pygame.time.set_timer(pygame.USEREVENT, move_period)
        self.draw()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button, button_action in self.buttons:
                        if button.collidepoint(pos):
                            button_action()
                elif event.type == pygame.KEYDOWN:
                    self.apply_moves([self.map_keypress(event.key)])
                elif event.type == pygame.USEREVENT:
                    next_move = next(self.moves, None)
                    if next_move is not None:
                        self.cube.parse_move(next_move)
                        if self.cube.is_solved():
                            self.draw((255, 255, 255))
                            pygame.mixer.init()
                            pygame.mixer.music.load("victory.mp3")
                            pygame.mixer.music.play()
                            pygame.time.set_timer(pygame.USEREVENT+1, 250)
                elif event.type == pygame.USEREVENT+1:
                    self.draw()
                    pygame.time.set_timer(pygame.USEREVENT+1, 0)
            self.redraw()
