import os
import sys

def Banner():
	if sys.platform == "linux":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		try:
			os.system("clear")
		except:
			pass
	print("""\033[1;36m
	\t\t _____         _      ____                      _   
	\t\t|  |  |___ ___| |_   |    \ ___ ___ ___ _ _ ___| |_ 
	\t\t|     | .'|_ -|   |  |  |  | -_|  _|  _| | | . |  _|
	\t\t|__|__|__,|___|_|_|  |____/|___|___|_| |_  |  _|_|  
	\t\t                                       |___|_|\033[m
	\t\t            \033[1m[\033[m\033[1;31m+\033[m\033[1m]\033[m \033[1mCoded by: Nano\033[m
	\t\t            \033[1m[\033[m\033[1;31m+\033[m\033[1m]\033[m \033[1mTelegram: t.me/rdzin9\033[m   
			\n\n""")