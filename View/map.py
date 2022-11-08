import pygame as pg
from settings import TILE_SIZE


class Map:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        self.matrix = [
                      [58, 54, 61, 60, 55, 55, 60, 0, 36, 32, 152, 172, 121, 121, 121, 121, 131, 0, 0, 0, 0, 0, 55, 57, 54, 58, 60, 42, 47, 36, 32, 52, 61, 58, 60, 43, 0, 0, 0, 0],
                      [58, 58, 58, 60, 51, 60, 54, 53, 52, 52, 52, 154, 172, 121, 121, 121, 170, 133, 133, 133, 144, 0, 0, 32, 31, 54, 45, 47, 36, 55, 65, 36, 60, 61, 54, 57, 31, 0, 0, 0],
                      [57, 59, 61, 59, 49, 59, 57, 42, 47, 36, 36, 52, 153, 141, 142, 143, 172, 121, 121, 121, 129, 0, 56, 57, 54, 55, 60, 36, 36, 32, 36, 61, 42, 43, 47, 52, 52, 31, 0, 0],
                      [57, 61, 60, 36, 55, 54, 52, 52, 36, 32, 55, 61, 43, 45, 57, 60, 154, 143, 172, 121, 170, 144, 0, 32, 36, 42, 47, 43, 31, 45, 54, 56, 57, 50, 55, 31, 31, 40, 40, 0],
                      [50, 32, 36, 55, 57, 58, 59, 60, 61, 42, 43, 45, 47, 31, 0, 52, 51, 0, 154, 172, 121, 170, 147, 0, 36, 36, 32, 31, 40, 0, 0, 0, 61, 60, 57, 55, 54, 56, 57, 0],
                      [54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 0, 0, 152, 172, 121, 170, 133, 144, 36, 47, 45, 32, 36, 43, 42, 47, 55, 56, 57, 60, 61, 40, 0],
                      [54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 154, 172, 121, 121, 170, 133, 135, 133, 133, 146, 0, 0, 31, 32, 0, 55, 43, 58, 57, 0],
                      [56, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 36, 40, 0, 0, 152, 172, 121, 121, 121, 121, 121, 121, 170, 144, 0, 60, 59, 52, 53, 43, 47, 32, 0],
                      [60, 56, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 36, 40, 40, 0, 154, 172, 121, 121, 121, 121, 121, 121, 170, 146, 0, 45, 54, 55, 36, 31, 40, 0],
                      [55, 60, 56, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 36, 40, 32, 0, 152, 172, 121, 121, 121, 121, 121, 121, 129, 0, 151, 145, 0, 56, 60, 31, 0],
                      [60, 55, 60, 56, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 36, 40, 32, 0, 152, 172, 121, 121, 121, 121, 121, 170, 133, 171, 129, 0, 32, 40, 36, 0],
                      [61, 57, 61, 60, 36, 55, 54, 52, 52, 36, 32, 55, 61, 43, 45, 57, 60, 40, 40, 40, 40, 36, 0, 0, 0, 152, 141, 143, 142, 141, 172, 121, 121, 121, 170, 147, 31, 32, 36, 0],
                      [55, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 0, 0, 52, 52, 36, 32, 55, 61, 43, 45, 57, 40, 152, 140, 172, 121, 121, 170, 146, 36, 165, 40],
                      [58, 55, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 0, 0, 52, 52, 36, 32, 55, 61, 43, 45, 0, 0, 0, 153, 143, 172, 121, 170, 135, 174, 134],
                      [55, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 0, 45, 54, 154, 143, 172, 121, 121, 121],
                      [52, 55, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 0, 45, 54, 40, 154, 143, 172, 121],
                      [52, 45, 45, 36, 0, 42, 45, 47, 36, 32, 57, 45, 45, 36, 0, 0, 45, 54, 40, 0, 0, 55, 54, 51, 52, 53, 57, 55, 42, 36, 61, 45, 42, 45, 36, 0, 42, 45, 154, 142],
                      [36, 45, 47, 36, 32, 57, 45, 45, 36, 0, 42, 45, 47, 36, 32, 57, 0, 36, 0, 0, 45, 54, 40, 0, 0, 55, 54, 51, 52, 53, 57, 55, 42, 36, 0, 0, 0, 0, 0, 54],
                      [57, 0, 36, 0, 0, 45, 54, 40, 0, 0, 55, 54, 51, 52, 53, 57, 55, 42, 36, 0, 0, 0, 0, 0, 54, 36, 45, 47, 36, 32, 57, 45, 45, 36, 0, 42, 45, 47, 36, 32],
                      [47, 36, 32, 57, 45, 45, 36, 0, 42, 45, 47, 36, 32, 57, 0, 36, 0, 0, 45, 54, 40, 0, 0, 55, 54, 51, 52, 53, 57, 55, 42, 36, 0, 0, 0, 0, 0, 54, 36, 45],
                      [3089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 36, 0, 42, 45, 47, 36, 32, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3087, 0],
                      [2103, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2101],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [170, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [121, 170, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [141, 172, 170, 135, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 152, 172, 121, 131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [33, 0, 152, 172, 170, 133, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [30, 33, 37, 139, 121, 121, 131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 37, 44, 152, 172, 121, 170, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [43, 38, 36, 44, 152, 172, 121, 170, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 138, 121, 121, 170, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 154, 172, 121, 121, 129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 152, 172, 121, 170, 145, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 152, 140, 172, 170, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 137, 121, 170, 133, 144, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 300, 0, 0, 0, 0, 0, 0, 138, 121, 121, 121, 131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 139, 121, 121, 121, 131, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                      ]

        # self.perlin_scale = grid_length_x/2

        self.grass_tiles = pg.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
        self.tiles = self.load_images()
        self.map = self.create_map()


    def create_map(self):

        map = []

        for grid_x in range(self.grid_length_x):
            map.append([])
            for grid_y in range(self.grid_length_y):
                map_tile = self.grid_to_map(grid_x, grid_y)
                map[grid_x].append(map_tile)

                render_pos = map_tile["render_pos"]
                self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1]))

        return map

    def grid_to_map(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        if self.matrix[grid_x][grid_y] == 33:
            tile = "tree33"
        elif self.matrix[grid_x][grid_y] == 30:
            tile = "tree30"
        elif self.matrix[grid_x][grid_y] == 37:
            tile = "tree37"
        elif self.matrix[grid_x][grid_y] == 58:
            tile = "tree58"
        elif self.matrix[grid_x][grid_y] == 56:
            tile = "tree56"
        elif self.matrix[grid_x][grid_y] == 54:
            tile = "tree54"
        elif self.matrix[grid_x][grid_y] == 61:
            tile = "tree61"
        elif self.matrix[grid_x][grid_y] == 60:
            tile = "tree60"
        elif self.matrix[grid_x][grid_y] == 55:
            tile = "tree55"
        elif self.matrix[grid_x][grid_y] == 51:
            tile = "tree51"
        elif self.matrix[grid_x][grid_y] == 57:
            tile = "tree57"
        elif self.matrix[grid_x][grid_y] == 31:
            tile = "tree31"
        elif self.matrix[grid_x][grid_y] == 32:
            tile = "tree32"
        elif self.matrix[grid_x][grid_y] == 52:
            tile = "tree52"
        elif self.matrix[grid_x][grid_y] == 53:
            tile = "tree53"
        elif self.matrix[grid_x][grid_y] == 59:
            tile = "tree59"
        elif self.matrix[grid_x][grid_y] == 49:
            tile = "tree49"
        elif self.matrix[grid_x][grid_y] == 50:
            tile = "tree50"
        elif self.matrix[grid_x][grid_y] == 36:
            tile = "tree36"
        elif self.matrix[grid_x][grid_y] == 38:
            tile = "tree38"
        elif self.matrix[grid_x][grid_y] == 42:
            tile = "tree42"
        elif self.matrix[grid_x][grid_y] == 47:
            tile = "tree47"
        elif self.matrix[grid_x][grid_y] == 45:
            tile = "tree45"
        elif self.matrix[grid_x][grid_y] == 43:
            tile = "tree43"
        elif self.matrix[grid_x][grid_y] == 40:
            tile = "tree40"
        elif self.matrix[grid_x][grid_y] == 44:
            tile = "tree44"
        elif self.matrix[grid_x][grid_y] == 3089:
            tile = "direction1"
        elif self.matrix[grid_x][grid_y] == 3087:
            tile = "direction2"
        elif self.matrix[grid_x][grid_y] == 2103:
            tile = "road1"
        elif self.matrix[grid_x][grid_y] == 2093:
            tile = "road2"
        elif self.matrix[grid_x][grid_y] == 2101:
            tile = "road3"
        elif self.matrix[grid_x][grid_y] == 121:
            tile = "water"
        elif self.matrix[grid_x][grid_y] == 152:
            tile = "water1"
        elif self.matrix[grid_x][grid_y] == 153:
            tile = "water2"
        elif self.matrix[grid_x][grid_y] == 154:
            tile = "water4"
        elif self.matrix[grid_x][grid_y] == 172:
            tile = "water3"
        elif self.matrix[grid_x][grid_y] == 131:
            tile = "water5"
        elif self.matrix[grid_x][grid_y] == 141:
            tile = "water6"
        elif self.matrix[grid_x][grid_y] == 142:
            tile = "water7"
        elif self.matrix[grid_x][grid_y] == 143:
            tile = "water8"
        elif self.matrix[grid_x][grid_y] == 170:
            tile = "water9"
        elif self.matrix[grid_x][grid_y] == 135:
            tile = "water10"
        elif self.matrix[grid_x][grid_y] == 133:
            tile = "water11"
        elif self.matrix[grid_x][grid_y] == 144:
            tile = "water12"
        elif self.matrix[grid_x][grid_y] == 129:
            tile = "water13"
        elif self.matrix[grid_x][grid_y] == 147:
            tile = "water14"
        elif self.matrix[grid_x][grid_y] == 146:
            tile = "water15"
        elif self.matrix[grid_x][grid_y] == 140:
            tile = "water16"
        elif self.matrix[grid_x][grid_y] == 151:
            tile = "water17"
        elif self.matrix[grid_x][grid_y] == 171:
            tile = "water18"
        elif self.matrix[grid_x][grid_y] == 145:
            tile = "water19"
        elif self.matrix[grid_x][grid_y] == 165:
            tile = "water20"
        elif self.matrix[grid_x][grid_y] == 174:
            tile = "water21"
        elif self.matrix[grid_x][grid_y] == 134:
            tile = "water22"
        elif self.matrix[grid_x][grid_y] == 156:
            tile = "water23"
        elif self.matrix[grid_x][grid_y] == 139:
            tile = "water24"
        elif self.matrix[grid_x][grid_y] == 138:
            tile = "water25"
        elif self.matrix[grid_x][grid_y] == 137:
            tile = "water26"
        elif self.matrix[grid_x][grid_y] == 300:
            tile = "rock300"
        else:
            tile = ""

        out = {
                "grid": [grid_x, grid_y],
                "cart_rect": rect,
                "iso_poly": iso_poly,
                "render_pos": [minx, miny],
                "tile": tile
              }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        block = pg.image.load("Graphique/Land1a_00255.png").convert_alpha()
        tree33 = pg.image.load("Graphique/Land1a_00033.png").convert_alpha()
        tree30 = pg.image.load("Graphique/Land1a_00030.png").convert_alpha()
        tree37 = pg.image.load("Graphique/Land1a_00037.png").convert_alpha()
        tree54 = pg.image.load("Graphique/Land1a_00054.png").convert_alpha()
        tree58 = pg.image.load("Graphique/Land1a_00058.png").convert_alpha()
        tree51 = pg.image.load("Graphique/Land1a_00051.png").convert_alpha()
        tree55 = pg.image.load("Graphique/Land1a_00055.png").convert_alpha()
        tree61 = pg.image.load("Graphique/Land1a_00061.png").convert_alpha()
        tree60 = pg.image.load("Graphique/Land1a_00060.png").convert_alpha()
        tree57 = pg.image.load("Graphique/Land1a_00057.png").convert_alpha()
        tree31 = pg.image.load("Graphique/Land1a_00031.png").convert_alpha()
        tree32 = pg.image.load("Graphique/Land1a_00032.png").convert_alpha()
        tree36 = pg.image.load("Graphique/Land1a_00036.png").convert_alpha()
        tree38 = pg.image.load("Graphique/Land1a_00038.png").convert_alpha()
        tree42 = pg.image.load("Graphique/Land1a_00042.png").convert_alpha()
        tree45 = pg.image.load("Graphique/Land1a_00045.png").convert_alpha()
        tree47 = pg.image.load("Graphique/Land1a_00047.png").convert_alpha()
        tree52 = pg.image.load("Graphique/Land1a_00052.png").convert_alpha()
        tree53 = pg.image.load("Graphique/Land1a_00053.png").convert_alpha()
        tree59 = pg.image.load("Graphique/Land1a_00059.png").convert_alpha()
        tree49 = pg.image.load("Graphique/Land1a_00049.png").convert_alpha()
        tree50 = pg.image.load("Graphique/Land1a_00050.png").convert_alpha()
        tree56 = pg.image.load("Graphique/Land1a_00056.png").convert_alpha()
        tree43 = pg.image.load("Graphique/Land1a_00043.png").convert_alpha()
        tree40 = pg.image.load("Graphique/Land1a_00040.png").convert_alpha()
        tree44 = pg.image.load("Graphique/Land1a_00044.png").convert_alpha()
        direction1 = pg.image.load("Graphique/land3a_00089.png").convert_alpha()
        direction2 = pg.image.load("Graphique/land3a_00087.png").convert_alpha()
        road1 = pg.image.load("Graphique/Land2a_00103.png").convert_alpha()
        road2 = pg.image.load("Graphique/Land2a_00093.png").convert_alpha()
        road3 = pg.image.load("Graphique/Land2a_00101.png").convert_alpha()
        rock1 = pg.image.load("Graphique/Land1a_00290.png").convert_alpha()
        rock2 = pg.image.load("Graphique/Land1a_00291.png").convert_alpha()
        rock3 = pg.image.load("Graphique/Land1a_00292.png").convert_alpha()
        rock4 = pg.image.load("Graphique/Land1a_00293.png").convert_alpha()
        rock5 = pg.image.load("Graphique/Land1a_00294.png").convert_alpha()
        rock6 = pg.image.load("Graphique/Land1a_00295.png").convert_alpha()
        rock7 = pg.image.load("Graphique/Land1a_00296.png").convert_alpha()
        rock8 = pg.image.load("Graphique/Land1a_00297.png").convert_alpha()
        water = pg.image.load("Graphique/Land1a_00121.png").convert_alpha()
        water1 = pg.image.load("Graphique/Land1a_00152.png").convert_alpha()
        water2 = pg.image.load("Graphique/Land1a_00153.png").convert_alpha()
        water3 = pg.image.load("Graphique/Land1a_00172.png").convert_alpha()
        water4 = pg.image.load("Graphique/Land1a_00154.png").convert_alpha()
        water5 = pg.image.load("Graphique/Land1a_00131.png").convert_alpha()
        water6 = pg.image.load("Graphique/Land1a_00141.png").convert_alpha()
        water7 = pg.image.load("Graphique/Land1a_00142.png").convert_alpha()
        water8 = pg.image.load("Graphique/Land1a_00143.png").convert_alpha()
        water9 = pg.image.load("Graphique/Land1a_00170.png").convert_alpha()
        water10 = pg.image.load("Graphique/Land1a_00135.png").convert_alpha()
        water11 = pg.image.load("Graphique/Land1a_00133.png").convert_alpha()
        water12 = pg.image.load("Graphique/Land1a_00144.png").convert_alpha()
        water13 = pg.image.load("Graphique/Land1a_00129.png").convert_alpha()
        water14 = pg.image.load("Graphique/Land1a_00147.png").convert_alpha()
        water15 = pg.image.load("Graphique/Land1a_00146.png").convert_alpha()
        water16 = pg.image.load("Graphique/Land1a_00140.png").convert_alpha()
        water17 = pg.image.load("Graphique/Land1a_00151.png").convert_alpha()
        water18 = pg.image.load("Graphique/Land1a_00171.png").convert_alpha()
        water19 = pg.image.load("Graphique/Land1a_00145.png").convert_alpha()
        water20 = pg.image.load("Graphique/Land1a_00165.png").convert_alpha()
        water21 = pg.image.load("Graphique/Land1a_00174.png").convert_alpha()
        water22 = pg.image.load("Graphique/Land1a_00134.png").convert_alpha()
        water23 = pg.image.load("Graphique/Land1a_00156.png").convert_alpha()
        water24 = pg.image.load("Graphique/Land1a_00139.png").convert_alpha()
        water25 = pg.image.load("Graphique/Land1a_00138.png").convert_alpha()
        water26 = pg.image.load("Graphique/Land1a_00137.png").convert_alpha()
        rock300 = pg.image.load("Graphique/Land1a_00300.png").convert_alpha()

        return {"block": block,
                "tree33": tree33, "tree51": tree51, "tree55": tree55, "tree54": tree54, "tree36": tree36,
                "tree60": tree60, "tree61": tree61, "tree57": tree57, "tree56": tree56, "tree58": tree58,
                "tree31": tree31, "tree52": tree52, "tree59": tree59, "tree49": tree49, "tree50": tree50,
                "tree32": tree32, "tree53": tree53, "tree42": tree42, "tree47": tree47, "tree45": tree45,
                "tree43": tree43, "tree40": tree40, "tree30": tree30, "tree37": tree37, "tree44": tree44,
                "tree38": tree38,
                "rock1": rock1, "rock2": rock2, "rock3": rock3, "rock4": rock4,
                "rock5": rock5, "rock6": rock6, "rock7": rock7, "rock8": rock8,
                "direction1": direction1, "direction2": direction2,
                "road1": road1, "road2": road2, "road3": road3,
                "water": water, "water1": water1, "water2": water2, "water3": water3, "water4": water4,
                "water5": water5, "water6": water6, "water7": water7, "water8": water8, "water9": water9,
                "water10": water10, "water11": water11, "water12": water12, "water13": water13, "water14": water14,
                "water15": water15, "water16": water16, "water17": water17, "water18": water18, "water19": water19,
                "water20": water20, "water21": water21, "water22": water22, "water23": water23, "water24": water24,
                "water25": water25, "water26": water26,
                "rock300": rock300
               }


