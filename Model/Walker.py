import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

from Model import batiment as b


class Walker():
	def __init__(self,x,y, bat):
		self.x = x
		self.y = y
		self.name = 'no Walker'
		self.ttl = 20
		self.tab_path = [(x,y)]
<<<<<<< HEAD
		self.batiment = bat

=======
		self.prev_pos = ( x , y ) # Nécessaire pour le déplacement 
>>>>>>> Controller


