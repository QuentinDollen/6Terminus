from Terminus_project.Model import batiment as b
class tree(b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, "", posx, posy, 0, 0, 0, 0, 0, 0)
        self.name = "Tree"