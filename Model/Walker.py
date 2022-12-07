
from Terminus_project.Model import batiment as b


class Walker():
	def __init__(self,x,y, bat):
		self.x = x
		self.y = y
		self.name = 'no Walker'
		self.ttl = 20
		self.tab_path = [(x,y)]
		self.batiment = bat



