import pygame as pg
from settings import *

class Map:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width 
        self.height = height
        self.matrix = [
            [3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             0, 0, 0, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 65, 3, 3, 3, 3,
             3, 3, 0, 0, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 0, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3,
             3, 3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 3,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3,
             3, 3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             3, 3, 3, 0],
            [3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1,
             1, 3, 1, 3],
            [3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 1,
             1, 1, 1, 1],
            [3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 1, 1,
             1, 1, 1, 1],
            [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3,
             1, 1, 1, 1],
            [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
             3, 3, 1, 1],
            [0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 3, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
             0, 0, 0, 3],
            [0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3,
             3, 3, 3, 3],
            [0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0,
             0, 3, 3, 3],
            [3089, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 3087, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0,
             0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 0, 0, 3],
            [1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 3],
            [1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             0, 3, 0, 3, 3],
            [1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 0, 3, 3],
            [1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 39, 3, 3, 3, 3,
             3, 3, 3, 3, 3],
            [0, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0, 0, 2, 0, 0, 2, 2, 3, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3,
             3, 3, 3, 3],
            [3, 0, 1, 1, 1, 1, 1, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 2, 2, 0, 3, 3, 3, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 3, 3],
            [3, 3, 3, 1, 1, 1, 1, 0, 0, 3, 0, 0, 2, 2, 0, 0, 0, 3, 3, 0, 0, 0, 2, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
             3, 3, 3, 3],
            [0, 3, 3, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 2, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 2, 3, 0, 0, 3, 3, 0, 3, 3, 3, 3,
             3, 3, 3, 3, 3],
            [3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3,
             3, 3, 3, 3],
            [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3, 3, 3, 3,
             3, 0, 0, 3, 3],
            [3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 3],
            [3, 3, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0],
            [3, 0, 2, 0, 0, 0, 2, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0,
             0, 0, 2, 2],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
             0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 2, 0, 2, 0,
             0, 0, 2, 2],
            [0, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 0,
             0, 0, 2, 2]
        ]
        self.matrixNature = [
            [10058, 10054, 10061, 10060, 10055, 10055, 10060, 0, 10036, 10032, 30152, 30172, 30121, 30121, 30121, 30121, 30131, 0, 0, 0, 0, 0, 10055, 10057, 10054, 10058, 10060, 10042, 10047, 10036, 10032, 10052, 10061, 10058, 10060, 10043, 0, 0, 0, 0],
            [10058, 10058, 10058, 10060, 10051, 10060, 10054, 10053, 10052, 10052, 10052, 30154, 30172, 30121, 30121, 30121, 30170, 30133, 30133, 30133, 30144, 0, 0, 10032, 10031, 10054, 10045, 10047, 10036, 10055, 0, 10036, 10060, 10061, 10054, 10057, 10031, 0, 0, 0],
            [10057, 10059, 10061, 10059, 10049, 10059, 10057, 10042, 10047, 10036, 10036, 10052, 30153, 30141, 30142, 30143, 30172, 30121, 30121, 30121, 30129, 0, 10056, 10057, 10054, 10055, 10060, 10036, 10036, 10032, 10036, 10061, 10042, 10043, 10047, 10052, 10052, 10031, 0, 0],
            [10057, 10061, 10060, 10036, 10055, 10054, 10052, 10052, 10038, 10033, 10053, 10061, 10044, 10054, 10045, 10060, 30154, 30143, 30172, 30121, 30170, 30144, 0, 10032, 10036, 10042, 10047, 10043, 10031, 10045, 10054, 10056, 10057, 10050, 10055, 10031, 10031, 10040, 10040, 0],
            [10050, 10032, 10036, 10055, 10058, 10058, 10059, 10060, 10061, 10044, 10043, 10045, 0, 10031, 0, 10052, 10051, 0, 30154, 30172, 30121, 30170, 30147, 0, 10036, 10036, 10032, 10031, 10040, 0, 0, 0, 10061, 10060, 10057, 10055, 10054, 10056, 10057, 0],
            [10054, 10051, 10052, 10053, 10057, 10055, 10061, 10033, 10033, 10038, 10053, 10042, 10040, 10036, 10035, 10057, 10045, 0, 0, 30152, 30172, 30121, 30170, 30133, 30144, 10036, 10047, 10045, 10032, 10036, 10043, 10042, 10047, 10055, 10056, 10057, 10060, 10061, 10040, 0],
            [10054, 10051, 10052, 10047, 10040, 10055, 10042, 10036, 10038, 10036, 10042, 10045, 10036, 10036, 10032, 10040, 10037, 10038, 10033, 0, 30154, 30172, 30121, 30121, 30170, 30133, 30135, 30133, 30133, 30146, 0, 0, 10031, 10032, 0, 10055, 10043, 10058, 10057, 0],
            [10056, 10060, 10054, 10052, 10053, 10057, 10055, 10042, 10036, 10061, 10045, 10042, 10036, 10042, 0, 10032, 10057, 10036, 10040, 0, 0, 30152, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30144, 0, 10060, 10059, 10052, 10053, 10043, 10047, 10032, 0],
            [10050, 10040, 10055, 10061, 10055, 10045, 0, 10038, 10040, 10036, 10032, 10036, 10042, 10044, 0, 0, 10032, 10057, 10040, 10040, 10040, 0, 30154, 30172, 30121, 30121, 30121, 30121, 30121, 30121, 30170, 30146, 0, 10045, 10054, 10055, 10036, 10031, 10040, 0],
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 10036, 10033, 10033, 10033, 10036, 10036, 10040, 10036, 0, 10036, 10040, 0, 0, 0, 0, 0, 0, 0, 10033, 0, 0, 10033, 10036, 10041, 10041, 10034, 10036, 10036, 10037, 10033, 10033, 10032, 0, 0, 10034],
            [30146, 0, 0, 10033, 10047, 10053, 10040, 10042, 10053, 10044, 10034, 10034, 10034, 10031, 10036, 0, 0, 0, 0, 10054, 10033, 10035, 10035, 10037, 10040, 10049, 10046, 10044, 10038, 10037, 10045, 10043, 10035, 10040, 10042, 10044, 10040, 10040, 10033, 10031],
            [30170, 30144, 0, 0, 10036, 10040, 10040, 10040, 10042, 10033, 0, 0, 0, 10052, 0, 0, 0, 0, 0, 10033, 10036, 39, 10041, 10038, 10042, 10035, 10047, 10044, 10044, 10044, 10043, 10042, 10041, 10050, 10040, 0, 10047, 0, 10040, 10044],
            [30121, 30170, 30147, 0, 0, 10053, 10036, 10036, 10047, 10047, 0, 0, 0, 0, 10047, 0, 10037, 10037, 10037, 10037, 10033, 10035, 10042, 10042, 10042, 10042, 10043, 10045, 10050, 10060, 10060, 10049, 10061, 10040, 10054, 10046, 10050, 0, 10053, 10060],
            [30141, 30172, 30170, 30135, 30147, 0, 0, 10040, 10040, 10050, 0, 0, 0, 0, 0, 0, 0, 20378, 10054, 10041, 10042, 10043, 10044, 10045, 10044, 10043, 10042, 10041, 10040, 10040, 39, 10038, 10037, 10037, 10038, 10042, 10044, 10037, 10060, 10054],
            [0, 30152, 30172, 30121, 30131, 0, 0, 10036, 10042, 10043, 10044, 0, 0, 0, 20384, 0, 0, 20383, 20371, 10035, 20377, 0, 0, 0, 0, 10037, 10053, 10053, 10038, 10038, 10053, 10035, 0, 0, 10037, 10050, 10060, 10040, 10054, 10055],
            [10033, 0, 30152, 30172, 30170, 30133, 30147, 0, 0, 10052, 10053, 0, 0, 0, 0, 0, 0, 10043, 20372, 20372, 0, 10040, 10037, 10038, 0, 10038, 0, 10053, 10053, 10054, 10045, 10044, 10046, 10047, 10058, 10060, 10044, 10042, 10054, 10054],
            [10030, 10033, 10037, 30139, 30121, 30121, 30131, 0, 0, 10040, 0, 0, 20379, 20372, 0, 0, 0, 10044, 10033, 0, 0, 0, 20381, 10033, 0, 0, 10053, 10037, 10037, 10036, 10056, 10060, 10040, 10050, 0, 0, 10038, 10034, 10054, 10046],
            [0, 10037, 10044, 30152, 30172, 30121, 30170, 30144, 10036, 0, 0, 0, 0, 20378, 0, 0, 10033, 10037, 10044, 10036, 0, 0, 0, 0, 20380, 10033, 0, 0, 10038, 10053, 0, 10035, 10034, 10034, 10036, 10036, 10040, 10050, 10042, 10038],
            [10043, 10038, 10036, 10044, 30152, 30172, 30121, 30170, 30146, 0, 0, 0, 0, 20381, 10037, 10036, 10056, 10060, 10060, 10042, 0, 10035, 0, 0, 0, 20378, 0, 0, 0, 10034, 10047, 10042, 10044, 10040, 10050, 10060, 10059, 10058, 10036, 10038],
            [10042, 10040, 10052, 10033, 0, 30138, 30121, 30121, 30170, 30144, 20374, 0, 0, 0, 10035, 10044, 10042, 10038, 10034, 10043, 0, 10045, 0, 0, 0, 20381, 20374, 0, 0, 0, 0, 10036, 10038, 10040, 10037, 10036, 0, 0, 10047, 10053],
            [10047, 10036, 10036, 10036, 0, 30154, 30172, 30121, 30121, 30129, 0, 0, 0, 20380, 10040, 10060, 10050, 10055, 10061, 10034, 10040, 10042, 10041, 0, 0, 0, 20372, 20374, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10033],
            [10037, 10047, 0, 0, 0, 20371, 30152, 30172, 30121, 30170, 30145, 10033, 10060, 10042, 10043, 10058, 10047, 10061, 10061, 10061, 10059, 10056, 10059, 0, 0, 0, 20381, 20372, 20377, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [10036, 0, 20374, 0, 0, 0, 20371, 30152, 30140, 30172, 30170, 30144, 10043, 10059, 10042, 10046, 10046, 10046, 10042, 0, 10050, 10043, 0, 10054, 10055, 20378, 0, 0, 20382, 20375, 0, 20371, 0, 0, 20372, 0, 0, 0, 20382, 20372],
            [0, 0, 0, 0, 0, 0, 20384, 0, 0, 30137, 30121, 30170, 30133, 30144, 10033, 10044, 10040, 10042, 10041, 10041, 10041, 10058, 10060, 10058, 10034, 10044, 0, 0, 0, 0, 0, 0, 0, 0, 20379, 0, 0, 0, 0, 0],
            [0, 0, 0, 20384, 0, 0, 20377, 20374, 0, 30138, 30121, 30121, 30121, 30131, 10053, 10036, 10040, 10042, 10044, 10043, 10035, 10057, 10042, 10060, 10043, 10050, 10061, 10061, 20375, 0, 0, 0, 20383, 0, 20371, 0, 0, 0, 20384, 20380],
            [0, 0, 0, 0, 20372, 20376, 20372, 0, 0, 30139, 30121, 30121, 30121, 30131, 0, 10040, 10036, 0, 10052, 10047, 10036, 0, 0, 10031, 10045, 10040, 10053, 0, 0, 0, 0, 0, 20377, 20372, 20372, 0, 0, 0, 20371, 20372]
        ]


        self.grass_tiles = pg.Surface((grid_length_x * TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)).convert_alpha()
        self.tiles = self.load_images()
        self.map = self.create_map()

    def draw_mini(self, screen, camera):

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                # render_pos = self.map[x][y]["render_pos"]
                tile = self.map[x][y]["tile"]
                # minimap
                minimap_offset = [40, 40]
                render_pos_mini = self.map[x][y]["render_pos_mini"]

                if tile == "tree58":
                    pg.draw.circle(screen, GREEN, (
                        render_pos_mini[0] + 1414 + minimap_offset[0],
                        render_pos_mini[1] + 40 + minimap_offset[1]), 2)

                mini = self.map[x][y]["iso_poly_mini"]
                mini = [(x + 1412 + minimap_offset[0], y + 40 + minimap_offset[1]) for x, y in mini]
                pg.draw.polygon(screen, SADDLEBROWN, mini, 2)    

    def draw(self, screen, camera):

        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                render_pos = self.map[x][y]["render_pos"]
                tile = self.map[x][y]["tile"]
                if tile != "":
                    screen.blit(self.tiles[tile],
                        (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                        render_pos[1] - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y))

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
            ((grid_x * TILE_SIZE + TILE_SIZE), grid_y * TILE_SIZE),
            ((grid_x * TILE_SIZE + TILE_SIZE), (grid_y * TILE_SIZE + TILE_SIZE)),
            (grid_x * TILE_SIZE, (grid_y * TILE_SIZE + TILE_SIZE))
        ]

        rect_mini_map = [
            (grid_x * TILE_SIZE_MINI_MAP, grid_y * TILE_SIZE_MINI_MAP),
            ((grid_x * TILE_SIZE_MINI_MAP + TILE_SIZE_MINI_MAP), grid_y * TILE_SIZE_MINI_MAP),
            ((grid_x * TILE_SIZE_MINI_MAP + TILE_SIZE_MINI_MAP), (grid_y * TILE_SIZE_MINI_MAP + TILE_SIZE_MINI_MAP)),
            (grid_x * TILE_SIZE_MINI_MAP, (grid_y * TILE_SIZE_MINI_MAP + TILE_SIZE_MINI_MAP))
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]
        iso_poly_mini = [self.cart_to_iso(x, y) for x, y in rect_mini_map]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        minx_mini = min([x for x, y in iso_poly_mini])
        miny_mini = min([y for x, y in iso_poly_mini])
        
        # if self.matrix[grid_x][grid_y] == 3: #TREES
        match (self.matrixNature[grid_x][grid_y]):
                case 10030:  tile = "tree30"
                case 10031:  tile = "tree31"
                case 10032:  tile = "tree32"
                case 10033:  tile = "tree33"
                case 10034:  tile = "tree34"
                case 10035:  tile = "tree35"
                case 10036:  tile = "tree36"
                case 10037:  tile = "tree37"
                case 10038:  tile = "tree38"
                case 10040:  tile = "tree40"
                case 10041:  tile = "tree41"
                case 10042:  tile = "tree42"
                case 10043:  tile = "tree43"
                case 10044:  tile = "tree44"
                case 10045:  tile = "tree45"
                case 10046:  tile = "tree46"
                case 10047:  tile = "tree47"
                case 10049:  tile = "tree49"
                case 10050:  tile = "tree50"
                case 10051:  tile = "tree51"
                case 10052:  tile = "tree52"
                case 10053:  tile = "tree53"
                case 10054:  tile = "tree54"
                case 10055:  tile = "tree55"
                case 10056:  tile = "tree56"
                case 10057:  tile = "tree57"
                case 10058:  tile = "tree58"
                case 10059:  tile = "tree59"
                case 10060:  tile = "tree60"
                case 10061:  tile = "tree61"

                # Types of rocks
                case 20371:  tile = "rock71"
                case 20372:  tile = "rock72"
                case 20374:  tile = "rock74"
                case 20375:  tile = "rock75"
                case 20376:  tile = "rock76"
                case 20377:  tile = "rock77"
                case 20378:  tile = "rock78"

                # Types of waters
                case 30121:  tile = "water21"
                case 30129:  tile = "water29"
                case 30131:  tile = "water31"
                case 30133:  tile = "water33"
                case 30134:  tile = "water34"
                case 30135:  tile = "water35"
                case 30137:  tile = "water37"
                case 30138:  tile = "water38" 
                case 30139:  tile = "water39"
                case 30140:  tile = "water40"
                case 30141:  tile = "water41"
                case 30142:  tile = "water42"
                case 30143:  tile = "water43"
                case 30144:  tile = "water44"
                case 30145:  tile = "water45"
                case 30146:  tile = "water46"
                case 30147:  tile = "water47"
                case 30151:  tile = "water51"
                case 30152:  tile = "water52"
                case 30153:  tile = "water53"
                case 30154:  tile = "water54"
                case 30156:  tile = "water56"
                case 30165:  tile = "water65"
                case 30170:  tile = "water70"
                case 30171:  tile = "water71"
                case 30172:  tile = "water72"
                case 30174:  tile = "water74"

                case _:      tile = ""   

        out = {
                "grid": [grid_x, grid_y],
                "cart_rect": rect,
                "cart_rect_mini_map": rect_mini_map,
                "iso_poly": iso_poly,
                "iso_poly_mini": iso_poly_mini,
                "render_pos": [minx, miny],
                "render_pos_mini": [minx_mini, miny_mini],
                "tile": tile
              }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        block = pg.image.load("Graphique/Land1a_00255.png").convert_alpha()

        # Image of trees
        tree30 = pg.image.load("Graphique/Land1a_00030.png").convert_alpha()
        tree31 = pg.image.load("Graphique/Land1a_00031.png").convert_alpha()
        tree32 = pg.image.load("Graphique/Land1a_00032.png").convert_alpha()
        tree33 = pg.image.load("Graphique/Land1a_00033.png").convert_alpha()
        tree34 = pg.image.load("Graphique/Land1a_00034.png").convert_alpha()
        tree35 = pg.image.load("Graphique/Land1a_00035.png").convert_alpha()
        tree36 = pg.image.load("Graphique/Land1a_00036.png").convert_alpha()
        tree37 = pg.image.load("Graphique/Land1a_00037.png").convert_alpha()
        tree38 = pg.image.load("Graphique/Land1a_00038.png").convert_alpha()
        tree40 = pg.image.load("Graphique/Land1a_00040.png").convert_alpha()
        tree41 = pg.image.load("Graphique/Land1a_00041.png").convert_alpha()
        tree42 = pg.image.load("Graphique/Land1a_00042.png").convert_alpha()
        tree43 = pg.image.load("Graphique/Land1a_00043.png").convert_alpha()
        tree44 = pg.image.load("Graphique/Land1a_00044.png").convert_alpha()
        tree45 = pg.image.load("Graphique/Land1a_00045.png").convert_alpha()
        tree46 = pg.image.load("Graphique/Land1a_00046.png").convert_alpha()
        tree47 = pg.image.load("Graphique/Land1a_00047.png").convert_alpha()
        tree49 = pg.image.load("Graphique/Land1a_00049.png").convert_alpha()
        tree50 = pg.image.load("Graphique/Land1a_00050.png").convert_alpha()
        tree51 = pg.image.load("Graphique/Land1a_00051.png").convert_alpha()
        tree52 = pg.image.load("Graphique/Land1a_00052.png").convert_alpha()
        tree53 = pg.image.load("Graphique/Land1a_00053.png").convert_alpha()
        tree54 = pg.image.load("Graphique/Land1a_00054.png").convert_alpha()
        tree55 = pg.image.load("Graphique/Land1a_00055.png").convert_alpha()
        tree56 = pg.image.load("Graphique/Land1a_00056.png").convert_alpha()
        tree57 = pg.image.load("Graphique/Land1a_00057.png").convert_alpha()
        tree58 = pg.image.load("Graphique/Land1a_00058.png").convert_alpha()
        tree59 = pg.image.load("Graphique/Land1a_00059.png").convert_alpha()
        tree60 = pg.image.load("Graphique/Land1a_00060.png").convert_alpha()
        tree61 = pg.image.load("Graphique/Land1a_00061.png").convert_alpha()

        # Image of rocks
        rock71 = pg.image.load("Graphique/land3a_00071.png").convert_alpha()
        rock72 = pg.image.load("Graphique/land3a_00072.png").convert_alpha()
        rock74 = pg.image.load("Graphique/land3a_00074.png").convert_alpha()
        rock75 = pg.image.load("Graphique/land3a_00075.png").convert_alpha()
        rock76 = pg.image.load("Graphique/land3a_00076.png").convert_alpha()
        rock77 = pg.image.load("Graphique/land3a_00077.png").convert_alpha()  
        rock78 = pg.image.load("Graphique/land3a_00078.png").convert_alpha()
        
        # Image of waters
        water21 = pg.image.load("Graphique/Land1a_00121.png").convert_alpha()
        water29 = pg.image.load("Graphique/Land1a_00129.png").convert_alpha()
        water31 = pg.image.load("Graphique/Land1a_00131.png").convert_alpha()
        water33 = pg.image.load("Graphique/Land1a_00133.png").convert_alpha()
        water34 = pg.image.load("Graphique/Land1a_00134.png").convert_alpha()
        water35 = pg.image.load("Graphique/Land1a_00135.png").convert_alpha()
        water37 = pg.image.load("Graphique/Land1a_00137.png").convert_alpha()
        water38 = pg.image.load("Graphique/Land1a_00138.png").convert_alpha()
        water39 = pg.image.load("Graphique/Land1a_00139.png").convert_alpha()
        water40 = pg.image.load("Graphique/Land1a_00140.png").convert_alpha()
        water41 = pg.image.load("Graphique/Land1a_00141.png").convert_alpha()
        water42 = pg.image.load("Graphique/Land1a_00142.png").convert_alpha()
        water43 = pg.image.load("Graphique/Land1a_00143.png").convert_alpha()
        water44 = pg.image.load("Graphique/Land1a_00144.png").convert_alpha()
        water45 = pg.image.load("Graphique/Land1a_00145.png").convert_alpha()
        water46 = pg.image.load("Graphique/Land1a_00146.png").convert_alpha()
        water47 = pg.image.load("Graphique/Land1a_00147.png").convert_alpha()
        water51 = pg.image.load("Graphique/Land1a_00151.png").convert_alpha()
        water52 = pg.image.load("Graphique/Land1a_00152.png").convert_alpha()
        water53 = pg.image.load("Graphique/Land1a_00153.png").convert_alpha()
        water54 = pg.image.load("Graphique/Land1a_00154.png").convert_alpha()
        water56 = pg.image.load("Graphique/Land1a_00156.png").convert_alpha()
        water65 = pg.image.load("Graphique/Land1a_00165.png").convert_alpha()
        water70 = pg.image.load("Graphique/Land1a_00170.png").convert_alpha()     
        water71 = pg.image.load("Graphique/Land1a_00171.png").convert_alpha()
        water72 = pg.image.load("Graphique/Land1a_00172.png").convert_alpha()
        water74 = pg.image.load("Graphique/Land1a_00174.png").convert_alpha()
        
        

        return {
                "block": block,

                ##### Trees
                "tree30": tree30, "tree31": tree31, "tree32": tree32, "tree33": tree33, "tree34": tree34,
                "tree35": tree35, "tree36": tree36, "tree37": tree37, "tree38": tree38, "tree40": tree40, 
                "tree41": tree41, "tree42": tree42, "tree43": tree43, "tree44": tree44, "tree45": tree45, 
                "tree46": tree46, "tree47": tree47, "tree49": tree49, "tree50": tree50, "tree51": tree51, 
                "tree52": tree52, "tree53": tree53, "tree54": tree54, "tree55": tree55, "tree56": tree56, 
                "tree61": tree61, "tree57": tree57, "tree58": tree58, "tree59": tree59, "tree60": tree60, 
                
                ##### Rocks
                "rock71": rock71, "rock72": rock72, "rock74": rock74, "rock75": rock75, "rock76": rock76, 
                "rock77": rock77, "rock78": rock78,

                ##### Waters
                "water21": water21, "water29": water29, "water31": water31, "water33": water33, "water34": water34,
                "water35": water35, "water37": water37, "water38": water38, "water39": water39, "water40": water40, 
                "water41": water41, "water42": water42, "water43": water43, "water44": water44, "water45": water45, 
                "water46": water46, "water47": water47, "water51": water51, "water52": water52, "water53": water53, 
                "water54": water54, "water56": water56, "water65": water65, "water70": water70, "water71": water71, 
                "water72": water72, "water74": water74

               }

