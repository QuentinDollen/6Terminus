import sys
sys.path.insert(0, '..')
from Model import Walker as W

class Priest(W.Walker):
	def __init__(self,x,y):
		W.Walker.__init__(self,x,y)
		self.name = 'Priest'

		
	
