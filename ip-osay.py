import urllib.request
import json
import os

blue = "\033[1;34;40m"
reset = "\033[0;37;40m"
cyan = "\033[1;36;40m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"


os.system("clear")
print()
print()

print("""
╔══╦═══╗─╔═══╗
╚╣╠╣╔═╗║─║╔═╗║
─║║║╚═╝║─║║─║╠══╦══╦╗─╔╗
─║║║╔═╦╩═╣║─║║══╣╔╗║║─║║
╔╣╠╣║─╚══╣╚═╝╠══║╔╗║╚═╝║
╚══╩╝────╚═══╩══╩╝╚╩═╗╔╝
───────────────────╔═╝║
───────────────────╚══╝""")
print(red+"""					by Osay""")
print()
print()

print()
peticion = input(yellow+"Ingrese la IP de la victima: ")
print()

print(red+"Datos:\n")
print(reset+" ")

def main():
	ip = "https://ipinfo.io/"+peticion+"/json"
	url = urllib.request.urlopen(ip)
	
	nya = json.loads(url.read())
	
	
	for dato in nya:
		
		print(dato+":"+nya[dato])
	
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()
		
		
		
print(reset+" ")
