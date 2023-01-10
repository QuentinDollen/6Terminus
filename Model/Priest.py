import os
import sys

# Construct the full path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the PYTHONPATH
sys.path.append(parent_dir)

from Model import Walker as W

class Priest(W.Walker):
	def __init__(self,x,y):
		W.Walker.__init__(self,x,y)
		self.name = 'Priest'

		
	
