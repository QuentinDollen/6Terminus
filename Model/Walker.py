import sys
sys.path.insert(0, '..')
from Model import batiment as b


class Walker():
	def __init__(self,x,y, bat):
		self.x = x
		self.y = y
		self.name = 'no Walker'
		self.ttl = 20
		self.tab_path = []
		self.batiment = bat
		self.dest_x = -1
		self.dest_y = -1
		self.has_moved = 0



