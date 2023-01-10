import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

 # from nis import match
from Model import Walker as W

class Food_Guy(W.Walker):
	def __init__(self,x,y):
		W.Walker.__init__(self,x,y)
		self.cargaison = [ ['blé', 0 ], ['fruits', 0], ['viande', 0] ]
		self.name = 'Food_Guy'
	def ajout_marchandise(self,type_nourriture,nb):
		if(type_nourriture == 'blé'): self.cargaison[0][1] = self.cargaison[0][1] + nb
		if(type_nourriture == 'fruits'): self.cargaison[1][1] = self.cargaison[1][1] + nb
		if(type_nourriture == 'viandes'): self.cargaison[2][1] = self.cargaison[2][1] + nb
