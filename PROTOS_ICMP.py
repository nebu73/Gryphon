#!/usr/bin/env python
#Modulo del protocolo ICMP
import sys
from scapy.all import *
total = len(sys.argv)
typ=sys.argv[1]
ip=sys.argv[2]
ifc=sys.argv[3]
key=sys.argv[4]
load=sys.argv[5]

if total <= 6:
	#Si es para enviar paquetes
	if typ!=0:
		ippaq=IP(dst=ip)
		icmp=ICMP(type=8)
		paq=ippaq/icmp/load
		# Enviamos el paquete
		a = sr (paq,iface=ifc,verbose=False,retry= 0, timeout=5)
		if len(a)==True:
			e=open("aux.txt","w")
			e.write("1")
		else:
			e=open("aux.txt","w")
			e.write("0")
		#si es para enviar paquetes

else:
	#Si es para recibir paquetes
	data=sys.argv[6]
	z=open(data,"r")
	pkt=z.read()
	z.close()
	pkt=pkt.split(",")
	carga=str(pkt[28].partition("load="))
	print "la carga del paquete es :"+ str(carga)
	if pkt[27] == 8 :
		print "he evaluado bien que se trata de un paquete echo-request"
		carga=carga[::-1]
		carga=base64.b64decode(carga)
		if carga.load[0:4] == key:
		#abrimos el archivo 'received.txt' y escribimos los datos recibidos
			f = open('received.txt', "a")
			data =pkt[ICMP].load[4:]
			datap=data.partition("_")
			datap=datap[2].partition("_")
			num_paq=datap[0]
			datap=datap[2].partition("_")
			tot_paq=datap[0]
			data=str(datap[2])
			f.write(data)
			f.close()
			e=open("aux.txt","w")
			auxdata=num_paq + "_" + tot_paq
			e.write(auxdata)
			e.close
