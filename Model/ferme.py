import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

from Model import batiment as b

class Ferme (b.Batiment):
    def __init__(self, posx, posy):
        b.Batiment.__init__(self, 3, 100, posx, posy, 4, 0, 2, 1, 1, 2, 10)
        ind_Harv = 0
    def growFood(self):
        self.growFood = self.growFood + 1
        if(self.growFood >= 5):
            self.growFood = 0
            
