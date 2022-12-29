import sys

sys.path.insert(0, '..')
from Model import Walker as W


class Delivery_Guy(W.Walker):
	def __init__(self,x,y,bat,bat_cible,type_marchandise='ble', type_transport='warhouse'):
		W.Walker.__init__(self,x,y,bat)
		self.name = 'Delivery_Guy'
		self.cargaison_nourriture = [ ['ble', 0 ], ['fruits', 0], ['viande', 0]]
		self.cargaison_produits = [ ['argile',0], ['potterie',0], ['huile',0], ['',0], ['',0]]
		self.bat_destination = bat_cible
		self.type_transport=type_transport

	# ajoute une marchandise a la cargaison
	def ajout_marchandise(self,type_transport,nb):
		if(type_transport == 'ble'): self.cargaison_nourriture[0][1] = self.cargaison_nourriture[0][1] + nb
		if(type_transport == 'fruits'): self.cargaison_nourriture[1][1] = self.cargaison_nourriture[1][1] + nb
		if(type_transport == 'viandes'): self.cargaison_nourriture[2][1] = self.cargaison_nourriture[2][1] + nb
		if(type_transport == 'olives'): self.cargaison_produits[2][1] = self.cargaison_produits[2][1] + nb
		if(type_transport == 'argile'): self.cargaison_produits[0][1] = self.cargaison_produits[0][1] + nb
	
	# decharge une marchandise
	def dechargement(self,type_transport):
		if(type_transport == 'ble'): 
			res = ["ble", self.cargaison_nourriture[0][1]]
			self.cargaison_nourriture[0][1] = 0
			return res
		if type_transport == 'fruits':
			res = [self.cargaison_nourriture[1][1]]
			self.cargaison_nourriture[1][1] = 0
			return res
		if type_transport == 'viandes':
			res = [self.cargaison_nourriture[2][1]]
			self.cargaison_nourriture[2][1] = 0
			return res
		if type_transport == 'olives':
			res = [self.cargaison_produits[2][1]]
			self.cargaison_produits[2][1] = 0
			return res
		if type_transport == 'argile':
			res = [self.cargaison_produits[0][1]]
			self.cargaison_produits[0][1] = 0
			return res
