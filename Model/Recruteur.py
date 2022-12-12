from Terminus_project.Model import Walker as W

class Recruteur(W.Walker):
	def __init__(self,x,y):
		W.Walker.__init__(x,y)
		self.transport
		self.name = 'Recruteur'

