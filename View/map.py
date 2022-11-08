import pygame as pg
from settings import TILE_SIZE


class Map:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        self.matrix = [
                      [10058, 10054, 10061, 10060, 10055, 10055, 10060, 0, 10036, 10032, 30152, 30172, 30121, 30121, 30121, 30121, 30131, 0, 0, 0, 0, 0, 10055, 10057, 10054, 10058, 10060, 10042, 10047, 10036, 10032, 10052, 10061, 10058, 10060, 10043, 0, 0, 0, 0],
                      [10058, 10058, 10058, 10060, 10051, 10060, 10054, 10053, 10052, 10052, 10052, 30154, 30172, 30121, 30121, 30121, 30170, 30133, 30133, 30133, 30144, 0, 0, 10032, 10031, 10054, 10045, 10047, 10036, 10055, 65, 10036, 10060, 10061, 10054, 10057, 10031, 0, 0, 0],
                      [10057, 10059, 10061, 10059, 10049, 10059, 10057, 10042, 10047, 10036, 10036, 10052, 30153, 30141, 30142, 30143, 30172, 30121, 30121, 30121, 30129, 0, 10056, 10057, 10054, 10055, 10060, 10036, 10036, 10032, 10036, 10061, 10042, 10043, 10047, 10052, 10052, 10031, 0, 0],
                      [10057, 10061, 10060, 10036, 10055, 10054, 10052, 10052, 10038, 10033, 10053, 10061, 10044, 10054, 10045, 10060, 30154, 30143, 30172, 30121, 30170, 30144, 0, 10032, 10036, 10042, 10047, 10043, 10031, 10045, 10054, 10056, 10057, 10050, 10055, 10031, 10031, 10040, 10040, 0],
                      [10050, 10032, 10036, 10055, 10058, 10058, 10059, 10060, 10061, 10044, 10043, 10045, 48, 10031, 0, 10052, 10051, 0, 30154, 30172, 30121, 30170, 30147, 0, 10036, 10036, 10032, 10031, 10040, 0, 0, 0, 10061, 10060, 10057, 10055, 10054, 10056, 10057, 0],
                      [10054, 10051, 10052, 10053, 10057, 10055, 10061, 10033, 10033, 10038, 10053, 10042, 10040, 10036, 10035, 10057, 10045, 0, 0, 30152, 30172, 30121, 30170, 30133, 30144, 10036, 10047, 10045, 10032, 10036, 10043, 10042, 10047, 10055, 10056, 10057, 10060, 10061, 10040, 0],
                      [10054, 10051, 10052, 10047, 10040, 10055, 10042, 10036, 10038, 10036, 10042, 10045, 10036, 10036, 10032, 10040, 10037, 10038, 10033, 0, 30154, 30172, 30121, 30121, 30170, 30133, 30135, 30133, 30133, 30146, 0, 0, 10031, 10032, 0, 10055, 10043, 10058, 10057, 0],
                      [10056, 10060, 10054, 10052, 10053, 10057, 10055, 10042, 10036, 10061, 10045, 10042, 10036, 10042, 0, 10032, 10057, 10036, 10040, 0, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30144, 0, 10060, 10059, 10052, 10053, 10043, 10047, 10032, 0],
                      [10050, 10040, 10055, 10061, 10055, 10045, 48, 10038, 10040, 10036, 10032, 10036, 10042, 10044, 0, 0, 10032, 10057, 10040, 10040, 10040, 0, 30154, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30146, 0, 10045, 10054, 10055, 10036, 10031, 10040, 0],
                      [10055, 10060, 10056, 10054, 10037, 10061, 10044, 10044, 10044, 10042, 10036, 10036, 10040, 10044, 0, 0, 0, 0, 10057, 10037, 10040, 10032, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30129, 0, 30151, 30145, 0, 10056, 10060, 10031, 0],
                      [10060, 10055, 10060, 10056, 10054, 10042, 10052, 10040, 10053, 10055, 10040, 10037, 10041, 10044, 0, 0, 0, 0, 0, 0, 10037, 10035, 10032, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30170, 30133, 30171, 30129, 0, 10032, 10040, 10036, 0],
                      [10061, 10041, 10041, 10041, 10036, 10036, 10036, 0, 0, 10033, 10032, 10033, 10047, 10043, 0, 10057, 0, 0, 0, 10040, 10040, 10040, 0, 0, 0, 30152, 30141, 30143, 30142, 30141, 30172, 30121, 30121, 30121, 30170, 30147, 10031, 10032, 10036, 0],
                      [10055, 10038, 10034, 10037, 10053, 10040, 0, 0, 10036, 10034, 10036, 10045, 10045, 10038, 10035, 10037, 10055, 10045, 0, 0, 10038, 10037, 10040, 10032, 10034, 10033, 10034, 10036, 10038, 10040, 30152, 30140, 30172, 30121, 30121, 30170, 30146, 10036, 30165, 10040],
                      [10058, 10036, 10034, 10036, 10035, 0, 0, 0, 10042, 10036, 10061, 10045, 10042, 10045, 10047, 10036, 10032, 10057, 10045, 0, 0, 10052, 10038, 10038, 10032, 10055, 10061, 10043, 10045, 0, 0, 0, 30153, 30143, 30172, 30121, 30170, 30135, 30174, 30134],
                      [10055, 10032, 10036, 10042, 0, 0, 0, 0, 0, 10044, 10045, 10042, 10045, 10047, 10036, 10032, 10061, 10055, 10034, 10037, 0, 10042, 10045, 10047, 10038, 10032, 10057, 10045, 10045, 10036, 0, 0, 10045, 10054, 30154, 30143, 30172, 30121, 30121, 30121],
                      [10052, 10035, 10034, 10041, 10042, 0, 0, 0, 0, 0, 10061, 10045, 10042, 10045, 10047, 10036, 10032, 10057, 10045, 10045, 10036, 0, 10042, 10045, 10045, 10040, 10032, 10057, 10045, 10045, 10036, 0, 0, 10045, 10054, 10040, 30154, 30143, 30172, 30121],
                      [10052, 10038, 10038, 10036, 10036, 10034, 0, 0, 0, 0, 0, 10045, 10045, 10036, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10054, 10051, 10052, 10045, 10040, 10055, 10042, 10036, 10061, 10045, 10042, 10045, 10036, 0, 10042, 10045, 30154, 30142],
                      [0, 0, 10034, 10036, 10032, 10036, 10045, 0, 0, 0, 0, 0, 10034, 10036, 10032, 10036, 0, 10036, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10044, 10041, 10052, 10053, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054],
                      [0, 0, 0, 0, 0, 10044, 10034, 10040, 0, 0, 0, 0, 0, 0, 0, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054, 10036, 10045, 10047, 10042, 10032, 10057, 10045, 10045, 10036, 0, 10042, 10045, 10047, 10036, 10032],
                      [0, 0, 0, 0, 10036, 10036, 10036, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10045, 10054, 10040, 0, 0, 10055, 10054, 10051, 10052, 10053, 10057, 10055, 10042, 10036, 0, 0, 0, 0, 0, 10054, 10036, 10045],
                      [3089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10042, 10045, 10047, 10036, 10032, 10057, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3087, 0],
                      [2103, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2093, 2101],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 10035, 0, 0, 0, 0, 0, 10052, 0, 0, 0, 0, 0, 0, 0, 0, 10033, 10033, 0, 0, 0, 0, 0, 0, 0, 0, 10035, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 10036, 10033, 10033, 10033, 10036, 10036, 10040, 10036, 0, 10036, 10040, 0, 0, 0, 0, 0, 0, 0, 10033, 0, 0, 10033, 10036, 10041, 10041, 10034, 10036, 10036, 10037, 10033, 10033, 10032, 0, 0, 10034],
                      [30146, 0, 0, 10033, 10047, 10053, 10040, 10042, 10053, 10044, 10034, 10034, 10034, 10031, 10036, 0, 0, 0, 0, 10054, 10033, 10035, 10035, 10037, 10040, 10049, 10046, 10044, 10038, 10037, 10045, 10043, 10035, 10040, 10042, 10044, 10040, 10040, 10033, 10031],
                      [30170, 30144, 0, 0, 10036, 10040, 10040, 10040, 10042, 10033, 0, 0, 0, 10052, 0, 0, 0, 0, 0, 10033, 10036, 39, 10041, 10038, 10042, 10035, 10047, 10044, 10044, 10044, 10043, 10042, 10041, 10050, 10040, 0, 10047, 0, 10040, 10044],
                      [30121, 30170, 30147, 0, 0, 10053, 10036, 10036, 10047, 10047, 0, 0, 0, 0, 10047, 0, 10037, 10037, 10037, 10037, 10033, 10035, 10042, 10042, 10042, 10042, 10043, 10045, 10050, 10060, 10060, 10049, 10061, 10040, 10054, 10046, 10050, 0, 10053, 10060],
                      [30141, 30172, 30170, 30135, 30147, 0, 0, 10040, 10040, 10050, 0, 0, 0, 0, 0, 0, 0, 20378, 10054, 10041, 10042, 10043, 10044, 10045, 10044, 10043, 10042, 10041, 10040, 10040, 39, 10038, 10037, 10037, 10038, 10042, 10044, 10037, 10060, 10054],
                      [0, 30152, 30172, 30121, 30131, 0, 0, 10036, 10042, 10043, 10044, 0, 0, 0, 20384, 0, 0, 20383, 20371, 10035, 20377, 0, 0, 0, 0, 10037, 10053, 10053, 10038, 10038, 10053, 10035, 0, 0, 10037, 10050, 10060, 10040, 10054, 10055],
                      [10033, 0, 30152, 30172, 30170, 30133, 30147, 0, 0, 10052, 10053, 0, 0, 0, 0, 0, 0, 10043, 20372, 20372, 0, 10040, 10037, 10038, 48, 10038, 48, 10053, 10053, 10054, 10045, 10044, 10046, 10047, 10058, 10060, 10044, 10042, 10054, 10054],
                      [10030, 10033, 10037, 30139, 30121, 30121, 30131, 0, 0, 10040, 0, 0, 20379, 20372, 0, 0, 0, 10044, 10033, 0, 0, 0, 20381, 10033, 0, 0, 10053, 10037, 10037, 10036, 10056, 10060, 10040, 10050, 0, 0, 10038, 10034, 10054, 10046],
                      [0, 10037, 10044, 30152, 30172, 30121, 30170, 30144, 10036, 0, 0, 0, 0, 20378, 0, 0, 10033, 10037, 10044, 10036, 0, 0, 0, 0, 20380, 10033, 0, 0, 10038, 10053, 48, 10035, 10034, 10034, 10036, 10036, 10040, 10050, 10042, 10038],
                      [10043, 10038, 10036, 10044, 30152, 30172, 30121, 30170, 30146, 0, 0, 0, 0, 20381, 10037, 10036, 10056, 10060, 10060, 10042, 0, 10035, 0, 0, 0, 20378, 0, 0, 0, 10034, 10047, 10042, 10044, 10040, 10050, 10060, 10059, 10058, 10036, 10038],
                      [10042, 10040, 10052, 10033, 0, 30138, 30121, 30121, 30170, 30144, 20374, 0, 0, 0, 10035, 10044, 10042, 10038, 10034, 10043, 48, 10045, 0, 0, 0, 20381, 20374, 0, 0, 0, 0, 10036, 10038, 10040, 10037, 10036, 0, 0, 10047, 10053],
                      [10047, 10036, 10036, 10036, 0, 30154, 30172, 30121, 30121, 30129, 0, 0, 0, 20380, 10040, 10060, 10050, 10055, 10061, 10034, 10040, 10042, 10041, 0, 0, 0, 20372, 20374, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10033],
                      [10037, 10047, 0, 0, 0, 20371, 30152, 30172, 30121, 30170, 30145, 10033, 10060, 10042, 10043, 10058, 10047, 10061, 10061, 10061, 10059, 10056, 10059, 0, 0, 0, 20381, 20372, 20377, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [10036, 0, 20374, 0, 0, 0, 20371, 30152, 30140, 30172, 30170, 30144, 10043, 10059, 10042, 10046, 10046, 10046, 10042, 0, 10050, 10043, 0, 10054, 10055, 20378, 0, 0, 20382, 20375, 0, 20371, 0, 0, 20372, 0, 0, 0, 20382, 20372],
                      [0, 0, 0, 0, 0, 0, 20384, 0, 0, 30137, 30121, 30170, 30133, 30144, 10033, 10044, 10040, 10042, 10041, 10041, 10041, 10058, 10060, 10058, 10034, 10044, 0, 0, 0, 0, 0, 0, 0, 0, 20379, 0, 0, 0, 0, 0],
                      [0, 0, 0, 20384, 0, 0, 20377, 20374, 0, 30138, 30121, 30121, 30121, 30131, 10053, 10036, 10040, 10042, 10044, 10043, 10035, 10057, 10042, 10060, 10043, 10050, 10061, 10061, 20375, 0, 0, 0, 20383, 0, 20371, 0, 0, 0, 20384, 20380],
                      [0, 0, 0, 0, 20372, 20376, 20372, 0, 0, 30139, 30121, 30121, 30121, 30131, 0, 10040, 10036, 0, 10052, 10047, 10036, 0, 0, 10031, 10045, 10040, 10053, 0, 0, 0, 0, 0, 20377, 20372, 20372, 0, 0, 0, 20371, 20372]
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

        if self.matrix[grid_x][grid_y] == 10033:
            tile = "tree33"
        elif self.matrix[grid_x][grid_y] == 10030:
            tile = "tree30"
        elif self.matrix[grid_x][grid_y] == 10037:
            tile = "tree37"
        elif self.matrix[grid_x][grid_y] == 10058:
            tile = "tree58"
        elif self.matrix[grid_x][grid_y] == 10056:
            tile = "tree56"
        elif self.matrix[grid_x][grid_y] == 10054:
            tile = "tree54"
        elif self.matrix[grid_x][grid_y] == 10061:
            tile = "tree61"
        elif self.matrix[grid_x][grid_y] == 10060:
            tile = "tree60"
        elif self.matrix[grid_x][grid_y] == 10055:
            tile = "tree55"
        elif self.matrix[grid_x][grid_y] == 10051:
            tile = "tree51"
        elif self.matrix[grid_x][grid_y] == 10041:
            tile = "tree41"
        elif self.matrix[grid_x][grid_y] == 10057:
            tile = "tree57"
        elif self.matrix[grid_x][grid_y] == 10031:
            tile = "tree31"
        elif self.matrix[grid_x][grid_y] == 10032:
            tile = "tree32"
        elif self.matrix[grid_x][grid_y] == 10035:
            tile = "tree35"
        elif self.matrix[grid_x][grid_y] == 10052:
            tile = "tree52"
        elif self.matrix[grid_x][grid_y] == 10053:
            tile = "tree53"
        elif self.matrix[grid_x][grid_y] == 10059:
            tile = "tree59"
        elif self.matrix[grid_x][grid_y] == 10049:
            tile = "tree49"
        elif self.matrix[grid_x][grid_y] == 10046:
            tile = "tree46"
        elif self.matrix[grid_x][grid_y] == 10050:
            tile = "tree50"
        elif self.matrix[grid_x][grid_y] == 10036:
            tile = "tree36"
        elif self.matrix[grid_x][grid_y] == 10034:
            tile = "tree34"
        elif self.matrix[grid_x][grid_y] == 10038:
            tile = "tree38"
        elif self.matrix[grid_x][grid_y] == 10042:
            tile = "tree42"
        elif self.matrix[grid_x][grid_y] == 10047:
            tile = "tree47"
        elif self.matrix[grid_x][grid_y] == 10045:
            tile = "tree45"
        elif self.matrix[grid_x][grid_y] == 10043:
            tile = "tree43"
        elif self.matrix[grid_x][grid_y] == 10040:
            tile = "tree40"
        elif self.matrix[grid_x][grid_y] == 10044:
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
        elif self.matrix[grid_x][grid_y] == 20384:
            tile = "rock1"
        elif self.matrix[grid_x][grid_y] == 20376:
            tile = "rock2"
        elif self.matrix[grid_x][grid_y] == 20372:
            tile = "rock3"
        elif self.matrix[grid_x][grid_y] == 20374:
            tile = "rock4"
        elif self.matrix[grid_x][grid_y] == 20377:
            tile = "rock5"
        elif self.matrix[grid_x][grid_y] == 20371:
            tile = "rock6"
        elif self.matrix[grid_x][grid_y] == 20380:
            tile = "rock7"
        elif self.matrix[grid_x][grid_y] == 20381:
            tile = "rock8"
        elif self.matrix[grid_x][grid_y] == 20379:
            tile = "rock9"
        elif self.matrix[grid_x][grid_y] == 20378:
            tile = "rock10"
        elif self.matrix[grid_x][grid_y] == 20383:
            tile = "rock11"
        elif self.matrix[grid_x][grid_y] == 20382:
            tile = "rock12"
        elif self.matrix[grid_x][grid_y] == 20375:
            tile = "rock13"
        elif self.matrix[grid_x][grid_y] == 20300:
            tile = "rock300"
        elif self.matrix[grid_x][grid_y] == 30121:
            tile = "water"
        elif self.matrix[grid_x][grid_y] == 30152:
            tile = "water1"
        elif self.matrix[grid_x][grid_y] == 30153:
            tile = "water2"
        elif self.matrix[grid_x][grid_y] == 30154:
            tile = "water4"
        elif self.matrix[grid_x][grid_y] == 30172:
            tile = "water3"
        elif self.matrix[grid_x][grid_y] == 30131:
            tile = "water5"
        elif self.matrix[grid_x][grid_y] == 30141:
            tile = "water6"
        elif self.matrix[grid_x][grid_y] == 30142:
            tile = "water7"
        elif self.matrix[grid_x][grid_y] == 30143:
            tile = "water8"
        elif self.matrix[grid_x][grid_y] == 30170:
            tile = "water9"
        elif self.matrix[grid_x][grid_y] == 30135:
            tile = "water10"
        elif self.matrix[grid_x][grid_y] == 30133:
            tile = "water11"
        elif self.matrix[grid_x][grid_y] == 30144:
            tile = "water12"
        elif self.matrix[grid_x][grid_y] == 30129:
            tile = "water13"
        elif self.matrix[grid_x][grid_y] == 30147:
            tile = "water14"
        elif self.matrix[grid_x][grid_y] == 30146:
            tile = "water15"
        elif self.matrix[grid_x][grid_y] == 30140:
            tile = "water16"
        elif self.matrix[grid_x][grid_y] == 30151:
            tile = "water17"
        elif self.matrix[grid_x][grid_y] == 30171:
            tile = "water18"
        elif self.matrix[grid_x][grid_y] == 30145:
            tile = "water19"
        elif self.matrix[grid_x][grid_y] == 30165:
            tile = "water20"
        elif self.matrix[grid_x][grid_y] == 30174:
            tile = "water21"
        elif self.matrix[grid_x][grid_y] == 30134:
            tile = "water22"
        elif self.matrix[grid_x][grid_y] == 30156:
            tile = "water23"
        elif self.matrix[grid_x][grid_y] == 30139:
            tile = "water24"
        elif self.matrix[grid_x][grid_y] == 30138:
            tile = "water25"
        elif self.matrix[grid_x][grid_y] == 30137:
            tile = "water26"

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
        tree46 = pg.image.load("Graphique/Land1a_00046.png").convert_alpha()
        tree41 = pg.image.load("Graphique/Land1a_00041.png").convert_alpha()
        tree31 = pg.image.load("Graphique/Land1a_00031.png").convert_alpha()
        tree32 = pg.image.load("Graphique/Land1a_00032.png").convert_alpha()
        tree34 = pg.image.load("Graphique/Land1a_00034.png").convert_alpha()
        tree35 = pg.image.load("Graphique/Land1a_00035.png").convert_alpha()
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
        tree46 = pg.image.load("Graphique/Land1a_00046.png").convert_alpha()
        rock1 = pg.image.load("Graphique/land3a_00084.png").convert_alpha()
        rock2 = pg.image.load("Graphique/land3a_00076.png").convert_alpha()
        rock3 = pg.image.load("Graphique/land3a_00072.png").convert_alpha()
        rock4 = pg.image.load("Graphique/land3a_00074.png").convert_alpha()
        rock5 = pg.image.load("Graphique/land3a_00077.png").convert_alpha()
        rock6 = pg.image.load("Graphique/land3a_00071.png").convert_alpha()
        rock7 = pg.image.load("Graphique/land3a_00080.png").convert_alpha()
        rock8 = pg.image.load("Graphique/land3a_00081.png").convert_alpha()
        rock9 = pg.image.load("Graphique/land3a_00079.png").convert_alpha()
        rock10 = pg.image.load("Graphique/land3a_00078.png").convert_alpha()
        rock11 = pg.image.load("Graphique/land3a_00083.png").convert_alpha()
        rock12 = pg.image.load("Graphique/land3a_00082.png").convert_alpha()
        rock13 = pg.image.load("Graphique/land3a_00075.png").convert_alpha()
        direction1 = pg.image.load("Graphique/land3a_00089.png").convert_alpha()
        direction2 = pg.image.load("Graphique/land3a_00087.png").convert_alpha()
        road1 = pg.image.load("Graphique/Land2a_00103.png").convert_alpha()
        road2 = pg.image.load("Graphique/Land2a_00093.png").convert_alpha()
        road3 = pg.image.load("Graphique/Land2a_00101.png").convert_alpha()
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
                "tree38": tree38, "tree35": tree35, "tree34": tree34, "tree46": tree46, "tree41": tree41,
                "rock1": rock1, "rock2": rock2, "rock3": rock3, "rock4": rock4, "rock5": rock5, "rock6": rock6,
                "rock7": rock7, "rock8": rock8, "rock9": rock9, "rock10": rock10, "rock11": rock11, "rock12": rock12,
                "rock13": rock13, "rock300": rock300,
                "direction1": direction1, "direction2": direction2,
                "road1": road1, "road2": road2, "road3": road3,
                "water": water, "water1": water1, "water2": water2, "water3": water3, "water4": water4,
                "water5": water5, "water6": water6, "water7": water7, "water8": water8, "water9": water9,
                "water10": water10, "water11": water11, "water12": water12, "water13": water13, "water14": water14,
                "water15": water15, "water16": water16, "water17": water17, "water18": water18, "water19": water19,
                "water20": water20, "water21": water21, "water22": water22, "water23": water23, "water24": water24,
                "water25": water25, "water26": water26
               }


