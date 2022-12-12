import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

from Model import batiment as b
class Herb(b.Batiment):
    def __init__(self,x,y):
        b.Batiment.__init__(self, x,y,0,0,0,0,0,0,0,0)
        self.name = "Herb"
