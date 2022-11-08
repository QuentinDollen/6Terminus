
from nis import match
import Walker as W

class Food_Guy(W.Walker):
	def __init__(self):
		W.Walker.__init__(self)
		self.cargaison = [ ['blé', 0 ], ['fruits', 0], ['viande', 0] ]
		self.name = 'Food_Guy'

	
	def ajout_marchandise(self,type_nourriture,nb):
		if(type_nourriture == 'blé'): self.cargaison[0][1] = self.cargaison[0][1] + nb
		if(type_nourriture == 'fruits'): self.cargaison[1][1] = self.cargaison[1][1] + nb
		if(type_nourriture == 'viandes'): self.cargaison[2][1] = self.cargaison[2][1] + nb
