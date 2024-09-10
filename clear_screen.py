# função separada somente para poder limpar a tela do terminal

import os
import sys

def Clear():

	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		try:
			os.system("clear")
		except:
			pass