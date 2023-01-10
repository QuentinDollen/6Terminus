import pygame as pg

class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0)
        self.dx = 0
        self.dy = 0
        self.speed = 23
        self.zoomLevel = 1

    def update(self):

        mouse_pos = pg.mouse.get_pos()
        # keys = pg.key.get_pressed() 

        # x movement
        if mouse_pos[0] > self.width * 0.98:
            self.dx = -self.speed
        elif mouse_pos[0] < self.width * 0.02:
            self.dx = self.speed
        else:
            self.dx = 0

        # y movement
        if mouse_pos[1] > self.height * 0.98:
            self.dy = -self.speed
        elif mouse_pos[1] < self.height * 0.02:
            self.dy = self.speed
        else:
            self.dy = 0

        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy 




