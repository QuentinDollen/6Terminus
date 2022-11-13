import pathlib
import batiment as b

global dir_path

bat_path = '' + str(pathlib.Path(__file__).absolute())

dir_path: str = bat_path.replace('Batiment.py', '')

class Walker():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.image_path = dir_path+''
		self.name = 'no Walker'
		self.ttl = 20
		self.tab_path = [(x,y)]



