#Voy a intentar crear una base de datos similar a MyAnimeList, donde pueda guardar nombres, capítulos vistos/leídos y opiniones con un máximo de caracteres.

#Edit: Simplemente voy a permitir el ingreso de Animes (sin base de datos, ponemos lo que nos pinta)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Antes que nada, importamos las bibliotecas a utilizar:

import os
import os.path
import pickle
import io
import sys
import datetime
from datetime import datetime
from datetime import date
import time

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Primero debo pensar y establecer los registros y archivos que voy a utilizar.

#En principio, voy a crear 2 registros y archivos: 1 para la lista del usuario (yo) y otro para la base de datos a partir de la cual podré registrar en mi lista.

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#class Lista:
#	def __init__(self):
#		self.Cod=0   #Código que identifica a la obra en cuestión...
#		self.NomENG=" "	#60 caracteres por ahora...
#		self.NomJAP=" "	#60 caracteres
#		self.Desc= " "  #500 caracteres para la descripción...
#		self.Opino=" "	#500 caracteres para opinar...
#		self.Tipo=" "	#Acá voy a establecer si es un Anime o un Manga | 5 caracteres...
#		self.CapL=0	#Dentro va a ir el límite de capítulos que tenga el anime/manga
#		self.TomoL=0	#Dentro va a ir el límite de tomos que tenga el manga
#		self.CapV=0 #Capítulos vistos
#		self.TomoV=0 #Tomos Leídos
#		self.Puntos=0 #Puntaje del 1 al 10 que uno le dió al anime/manga

class Base:
	def __init__(self):
		self.Cod=0   #Código que identifica a la obra...
		self.NomENG=" "	#60 caracteres por ahora...
		self.NomJAP=" "	#60 caracteres
		self.Desc=" "	#500 caracteres para ingresar la descripción de el anime/manga
		self.Tipo=" "	#Acá voy a establecer si es un Anime o un Manga | 5 caracteres...
		self.CapL=0	#Dentro va a ir el límite de capítulos que tenga el anime/manga
		self.TomoL=0	#Dentro va a ir el límite de tomos que tenga el manga
		self.CapV=0   #Capítulos vistos
		self.TomoV=0   #Tomos Leídos
		self.Puntos=0   #Puntaje del 1 al 10 que uno le dió al anime/manga
		self.Estado=" "   #Si la serie está dada de alta o de baja.

#Más adelante me gustaría guardar imágenes, pero está jodida la cosa jeje

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#En principio esta sería la declarativa del programita. Más adelante veré de hacer los cambios que pueda / se me ocurran.

#Ahora, vamos a crear los archivos a utilizar y, posteriormente, el menú de opciones con todas las funcionalidades...

def abrir():
	global afl, al, afb, alb
#	afl=r"D:\\Mauro\Programas\Python\ListaPROJECT.dat"
#	if os.path.exists(afl)==True:
#		al=open(afl,"r+b")
#	else:
#		al=open(afl,"w+b")
	afb=r"D:\Mauro\Programas\Python(Personal)\BaseDatosPROJECT.dat"
	if os.path.exists(afb)==True:
		alb=open(afb,"r+b")
	else:
		alb=open(afb,"w+b")
	#L=Lista()

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Ahora tenemos que pensar las opciones que vamos a dar al usuario a la hora de utilizar el programa.

#En principio, vamos a ofrecer:


# 1- Agregar Anime/Manga a la Base de Datos.

# Código
# Nombre
# Tipo
# Descripción
# Capítulo
# Tomo (En caso de ser MANGA)

# 2- Eliminar Anime/Manga de la Base de Datos.

# 3- Modificar la Base de Datos.

#		* Tomo
#		* Capítulo
#		* Puntaje
#		* Descripción
#		* Nombre ING
#		* Nombre JAP

#Más tarde veré si hace falta agregar algo más, pero en principio esto estaría bien...

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Este módulo valida la opción ingresada por el usuario dentro del Menú Principal...

def opcion():
	global op
	print("[ MENU DE OPCIONES ]")
	print()
	print("-------------------------")
	print("1- Agregar Anime/Manga")
	print()
	print("2- Eliminar Anime/Manga")
	print()
	print("3- Modificaciones")
	print()
	print("4- Ver Lista")
	print()
	print("0- Salir del Programa")
	print("-------------------------")
	print()
	op=input("Ingrese el número de la opción a acceder: ")
	while op.isdigit()==False:
		print()
		print("Por favor, ingrese un número y no una letra/símbolo...")
		print()
		input("Presione [Enter] para continuar...")
		os.system("cls")
		print("[ MENU DE OPCIONES ]")
		print()
		print("-------------------------")
		print("1- Agregar Anime/Manga")
		print()
		print("2- Eliminar Anime/Manga")
		print()
		print("3- Modificaciones")
		print()
		print("4- Ver Lista")
		print()
		print("0- Salir del Programa")
		print("-------------------------")
		print()
		op=input("Ingrese el número de la opción a acceder: ")
	op=int(op)
	while op<0 or op>4:
		print()
		print("El valor ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		input("Presione [Enter] para continuar...")
		os.system("cls")
		print("[ MENU DE OPCIONES ]")
		print()
		print("-------------------------")
		print("1- Agregar Anime/Manga")
		print()
		print("2- Eliminar Anime/Manga")
		print()
		print("3- Modificaciones")
		print()
		print("4- Ver Lista")
		print()
		print("0- Salir del Programa")
		print("-------------------------")
		print()
		op=int(input("Ingrese el número de la opción a acceder: "))

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

def BuscarCod(x):
	global B, puntB
	alb.seek(0,0)
	limB=os.path.getsize(afb)
	puntB=alb.tell()
	B=pickle.load(alb)
	while alb.tell()<limB and B.Cod!=x:
		puntB=alb.tell()
		B=pickle.load(alb)
	if B.Cod==x:
		return puntB
	else:
		return -1

#------------------------------------------------------------------------------------------------------

def NomObra(x):
	if x.NomENG!=" ":
		return x.NomENG
	else:
		return x.NomJAP

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Estos son los Módulos que se encuentran dentro de la Primera Opción del Menú Principal y aún no 

# fueron definidos...

def IngCod():
	global cod
	cod=input("Ingrese el código de la obra [N° Mayor que (0)]: ")
	while cod.isdigit()==False:
		print()
		print("Ingrese un valor númerico. Inténtelo nuevamente...")
		print()
		cod=input("Ingrese el código de la obra [N° Mayor que (0)]: ")
	cod=int(cod)
	while cod<0:
		print()
		print("Recuerde que el código de la obra debe ser un número mayor que (0). Inténtelo nuevamente...")
		print()
		cod=int(input("Ingrese el código de la obra [N° Mayor que (0)]"))


#------------------------------------------------------------------------------------------------------

def IngNom():
	global nom
	nom=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
	nom=nom.title()
	nom=nom.ljust(60," ")
	while len(nom)!=60:
		print()
		print("Superó el máximo de 60 caracteres. Inténtelo nuevamente...")
		print()
		nom=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
		nom=nom.title()
		nom=nom.ljust(60," ")
	while nom.isdigit()==True:
		print()
		print("No ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		nom=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
		nom=nom.title()
		nom=nom.ljust(60," ")

#------------------------------------------------------------------------------------------------------

def BuscarNom(x):
	global B, puntB
	alb.seek(0,0)
	limB=os.path.getsize(afb)
	puntB=alb.tell()
	B=pickle.load(alb)
	while alb.tell()<limB and B.NomENG!=x and B.NomJAP!=x:
		puntB=alb.tell()
		B=pickle.load(alb)
	if B.NomENG==x or B.NomJAP==x:
		return puntB
	else:
		return -1

#------------------------------------------------------------------------------------------------------

def BuscarCodTipo(x,y):
	global B, puntB
	alb.seek(0,0)
	limB=os.path.getsize(afb)
	puntB=alb.tell()
	B=pickle.load(alb)
	while alb.tell()<limB and B.Cod!=x or B.Tipo!=y:
		puntB=alb.tell()
		B=pickle.load(alb)
	if B.Cod==x and B.Tipo==y:
		return puntB
	else:
		return -1

#------------------------------------------------------------------------------------------------------

def BuscarNomTipo(x,y):
	global B, puntB
	alb.seek(0,0)
	limB=os.path.getsize(afb)
	puntB=alb.tell()
	B=pickle.load(alb)
	while alb.tell()<limB and ((B.NomJAP!=x and B.NomENG!=x) or B.Tipo!=y):
		puntB=alb.tell()
		B=pickle.load(alb)
	if (B.NomENG==x or B.NomJAP==x) and B.Tipo==y:
		return puntB
	else:
		return -1

#------------------------------------------------------------------------------------------------------

def IngNom2():
	global nom2
	nom2=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
	nom2=nom2.ljust(60," ")
	while len(nom2)!=60:
		print()
		print("Superó el máximo de 60 caracteres. Inténtelo nuevamente...")
		print()
		nom2=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
		nom2=nom2.ljust(60," ")
	while nom2.isdigit()==True:
		print()
		print("No ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		nom2=input("Ingrese el nombre de la obra [Máximo 60 caracteres]: ")
		nom2=nom2.ljust(60," ")

#------------------------------------------------------------------------------------------------------

def IngDesc():
	global desc
	desc=input("Ingrese la descripción de la obra (es decir, de qué trata) [No utilice tildes]: ")
	desc=desc.title()
	desc=desc.ljust(500," ")
	while desc.isdigit()==True:
		print()
		print("No ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		desc=input("Ingrese la descripción de la obra (es decir, de qué trata) [No utilice tildes]: ")
		desc=desc.title()
		desc=desc.ljust(500," ")
	while len(desc)!=500:
		print()
		print("Superó los 500 caracteres permitidos. Inténtelo nuevamente...")
		print()
		desc=input("Ingrese la descripción de la obra (es decir, de qué trata) [No utilice tildes]: ")
		desc=desc.title()
		desc=desc.ljust(500," ")

#------------------------------------------------------------------------------------------------------

def IngCap():
	global cap
	cap=input("Ingrese la cantidad total de capítulos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: ")
	while cap.isdigit()==False:
		print()
		print("Ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		cap=input("Ingrese la cantidad total de capítulos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: ")
	cap=int(cap)
	while cap<0:
		print()
		print("Ingrese un valor mayor o igual a 0. Inténtelo nuevamente...")
		print()
		cap=int(input("Ingrese la cantidad total de capítulos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: "))

#------------------------------------------------------------------------------------------------------

def IngTomo():
	global tomo
	tomo=input("Ingrese la cantidad total de tomos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: ")
	while tomo.isdigit()==False:
		print()
		print("Ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		tomo=input("Ingrese la cantidad total de tomos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: ")
	tomo=int(tomo)
	while tomo<0:
		print()
		print("Ingrese un valor mayor o igual a 0. Inténtelo nuevamente...")
		print()
		tomo=int(input("Ingrese la cantidad total de tomos que tiene la obra. Si no conoce o no se sabe el total, ingrese [0]: "))

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Este es el Módulo de la primera opción del Menú Principal...

def AgregBD():
	os.system("cls")
	print("[ AGREGAR {ANIME / MANGA} EN BASE DE DATOS ]")
	print()
	print()
	print("Ingrese [0] para finalizar...")
	print()
	IngCod()
	while cod!=0:
		print()
		IngNom()
		if os.path.getsize(afb)!=0:
			if BuscarCod(cod)!=-1:
				alb.seek(puntB,0)
				B=pickle.load(alb)
				if B.Tipo=="Anime":
					if BuscarCodTipo(cod,"Manga")!=-1:
						g=2
					else:
						g=1
						print()
						print("El Manga de esta obra no se encuentra registrado...")
						print()
						rp=input("¿Desea registrar el Manga de esta obra? [S - Si | N - No]: ")
						rp=rp.upper()
						while rp!="S" and rp!="N":
							print()
							print()
							print()
							rp=input("¿Desea registrar el Manga de esta obra? [S - Si | N - No]: ")
							rp=rp.upper()
						h=2
				else:
					if BuscarCodTipo(cod,"Anime")!=-1:
						g=2
					else:
						g=1
						print()
						print("El Anime de esta obra no se encuentra registrado...")
						print()
						rp=input("¿Desea registrar el Anime de esta obra? [S - Si | N - No]: ")
						rp=rp.upper()
						while rp!="S" and rp!="N":
							print()
							print()
							print()
							rp=input("¿Desea registrar el Anime de esta obra? [S - Si | N - No]: ")
							rp=rp.upper()
						h=1
			else:
				g=3
				print()
				print("Ni el Anime ni el Manga de esta obra se encuentran registrados...")
				rp="S"
				h=3
		else:
			g=4
			print()
			print("Ni el Anime ni el Manga de esta obra se encuentran registrados...")
			rp="S"
			h=3
		if g!=2 and rp=="S":
			B=Base()
			B.Cod=cod
			print()
			print("Excelente!! Procedamos con el registro de la obra...")
			print()
			print("-----------------------------------------------------------------------------------------------")
			print()
			r=input("El nombre que usted ingresó, ¿Está en Japonés o Inglés? [J - I]: ")
			r=r.upper()
			while r!="J" and r!="I":
				print()
				print("El dato ingresado no es correcto. Inténtelo nuevamente...")
				print()
				r=input("El nombre que usted ingresó, ¿Está en Japonés o Inglés? [J - I]: ")
				r=r.upper()
			if r=="J":
				B.NomJAP=nom
				print()
				res=input("¿Desea ingresar también el nombre en inglés de la obra? [S - Si | N - No]: ")
				res=res.upper()
				while res!="S" and res!="N":
					print()
					print("El dato ingresado no es correcto. Inténtelo nuevamente...")
					print()
					res=input("¿Desea ingresar también el nombre en inglés de la obra? [S - Si | N - No]: ")
					res=res.upper()
			else:
				B.NomENG=nom
				print()
				res=input("¿Desea ingresar también el nombre en japonés de la obra? [S - Si | N - No]: ")
				res=res.upper()
				while res!="S" and res!="N":
					print()
					print("El dato ingresado no es correcto. Inténtelo nuevamente...")
					print()
					res=input("¿Desea ingresar también el nombre en japonés de la obra? [S - Si | N - No]: ")
					res=res.upper()
			if res=="S":
				print()
				IngNom2()
				while nom2==nom:
					print()
					print("No ingrese el mismo nombre que escribió anteriormente...")
					print()
					IngNom2()
				if r=="J":
					B.NomENG=nom2
				else:
					B.NomJAP=nom2
			if h==1:
				B.Tipo="Anime"
			elif h==2:
				B.Tipo="Manga"
			else:
				print()
				resp=input("¿La obra que quiere registrar es un Manga o un Anime? [A - Anime | M - Manga]: ")
				resp=resp.upper()
				while resp!="A" and resp!="M":
					print()
					print("El dato ingresado no es correcto. Inténtelo nuevamente...")
					print()
					resp=input("¿La obra que quiere registrar es un Manga o un Anime? [A - Anime | M - Manga]: ")
					resp=resp.upper()
				if resp=="A":
					B.Tipo="Anime"
				else:
					B.Tipo="Manga"
			print()
			IngDesc()
			B.Desc=desc
			print()
			IngCap()
			B.CapL=cap
			if B.Tipo=="Manga":
				print()
				IngTomo()
				B.TomoL=tomo
			B.Estado="Alta"
			alb.seek(0,2)
			pickle.dump(B,alb)
			alb.flush()
			print()
			print("Operación Realizada con éxito...")
		else:
			print()
			print("Tanto el Anime como el Manga de esa obra ya se encuentran registrados...")
		print()
		input("Presione [Enter] para continuar...")
		os.system("cls")
		print("[ AGREGAR {ANIME / MANGA} EN BASE DE DATOS ]")
		print()
		print()
		print("Ingrese [0] para finalizar...")
		print()
		IngCod()

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

def pantallaBD():
	global y
	alb.seek(0,0)
	limB=os.path.getsize(afb)
	y=0
	while alb.tell()<limB:
		B=pickle.load(alb)
		if B.Estado!="Baja":
			print()
			print("-------------------------------------------------------------")
			print()
			print("Código de la obra: ",B.Cod)
			if B.NomENG!=" ":
				print("Nombre en Inglés de la obra: ",B.NomENG)
			if B.NomJAP!=" ":
				print("Nombre en Japonés de la obra: ",B.NomJAP)
			print("Tipo de obra: ", B.Tipo)
			print()
			print("-------------------------------------------------------------")
			y=1



#------------------------------------------------------------------------------------------------------

#Este es el Módulo de la segunda opción del Menú Principal...

def ElimBD():
	os.system("cls")
	print()
	print("[ ELIMINAR ]")
	print()
	if os.path.getsize(afb)!=0:
		pantallaBD()
		if y!=0:
			print()
			print("Ingrese [0] para finalizar...")
			print()
			IngCod()
			while cod!=0:
				if BuscarCod(cod)!=-1:
					if B.Estado!="Baja":
						os.system("cls")
						print()
						print("[ ELIMINAR ]")
						print()
						print("-------------------------------------------------------------")
						print()
						if B.NomJAP!=" ":
							print("Usted está a punto de eliminar a [", B.NomJAP, "] de la base de datos.")
							print()
							resl=input("¿Desea usted continuar? (S - Si | N - No): ")
							resl=resl.upper()
							while resl!="S" and resl!="N":
								print()
								print("Error. Ingrese un caracter válido...")
								print()
								input("Presione [Enter] para continuar: ")
								os.system("cls")
								print()
								print("[ ELIMINAR ]")
								print()
								print("-------------------------------------------------------------")
								print()
								print("Usted está a punto de eliminar a [", B.NomJAP, "] de la base de datos.")
								print()
								resl=input("¿Desea usted continuar? (S - Si | N - No): ")
								resl=resl.upper()
						else:
							print("Usted está a punto de eliminar a [", B.NomENG, "] de la base de datos.")
							print()
							resl=input("¿Desea usted continuar? (S - Si | N - No): ")
							resl=resl.upper()
							while resl!="S" and resl!="N":
								print()
								print("Error. Ingrese un caracter válido...")
								print()
								input("Presione [Enter] para continuar: ")
								os.system("cls")
								print()
								print("[ ELIMINAR ]")
								print()
								print("-------------------------------------------------------------")
								print()
								print("Usted está a punto de eliminar a [", B.NomENG, "] de la base de datos.")
								print()
								resl=input("¿Desea usted continuar? (S - Si | N - No): ")
								resl=resl.upper()
						if resl=="S":
							B.Estado="Baja"
							alb.seek(puntB,0)
							pickle.dump(B,alb)
							alb.flush()
							print()
							print("Operación realizada con éxito...")
							print()
							input("Presione [Enter] para continuar: ")
					else:
						print()
						print("La serie ya se encuentra dada de baja.")
						print()
						input("Presione [Enter] para continuar: ")
				else:
					print()
					print("El código de esa serie no se encuentra registrado. Inténtelo nuevamente...")
					print()
					input("Presione [Enter] para continuar: ")
				os.system("cls")
				print()
				print("[ ELIMINAR ]")
				print()
				pantallaBD()
				print()
				print("Ingrese [0] para finalizar...")
				print()
				IngCod()
		else:
			print("No hay datos ingresados en la base de datos...")
			print()
			input("Presione [Enter] para continuar: ")
	else:
		print("No hay datos ingresados en la base de datos...")
		print()
		input("Presione [Enter] para continuar: ")

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------ 

#Aqui tenemos algunas funciones relacionadas con el Tercer Módulo del Menú Principal.

def opcionBD():
	global opBD
	print("1- Nombre Inglés")
	print("2- Nombre Japonés")
	print("3- Descripción")
	print("4- Tipo")
	print("5- Capítulo")
	print("6- Tomo")
	print("7- Datos Actuales de la Obra")
	print("0- Volver")
	print()
	opBD=input("Ingrese el número de la opción a acceder: ")
	while opBD.isdigit()==False:
		print()
		print("Ingrese valores numéricos. Inténtelo nuevamente...")
		print()
		input("Presione [Enter] para continuar: ")
		os.system("cls")
		print()
		print("[MODIFICACIÓN en BASE de DATOS]")
		print()
		print("1- Nombre Inglés")
		print("2- Nombre Japonés")
		print("3- Descripción")
		print("4- Tipo")
		print("5- Capítulo")
		print("6- Tomo")
		print("7- Datos Actuales de la Obra")
		print("0- Volver")
		print()
		opBD=input("Ingrese el número de la opción a acceder: ")
	opBD=int(opBD)
	while opBD<0 or opBD>7:
		print()
		print("El número ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		input("Presione [Enter] para continuar: ")
		os.system("cls")
		print()
		print("[MODIFICACIÓN en BASE de DATOS]")
		print()
		print("1- Nombre Inglés")
		print("2- Nombre Japonés")
		print("3- Descripción")
		print("4- Tipo")
		print("5- Capítulo")
		print("6- Tomo")
		print("7- Datos Actuales de la Obra")
		print("0- Volver")
		print()
		opBD=int(input("Ingrese el número de la opción a acceder: "))

#------------------------------------------------------------------------------------------------------

def ModNE():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de NOMBRE INGLÉS]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print()
	IngNom2()
	print()
	r=input("¿Está seguro de modificar el nombre ["+B.NomENG+"] por ["+nom2.rstrip()+"]? | (S - Si / N - No): ")
	r=r.upper()
	while r!="S" and r!="N":
		print()
		print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		r=input("¿Está seguro de modificar el nombre ["+B.NomENG+"] por ["+nom2.rstrip()+"]? | (S - Si / N - No): ")
		r=r.upper()
	if r=="S":
		B.NomENG=nom2
		alb.seek(puntB,0)
		pickle.dump(B,alb)
		alb.flush()
		print()
		print("Operación realizada con éxito...")
	else:
		print()
		print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

def ModNJ():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de NOMBRE JAPONÉS]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print()
	IngNom2()
	print()
	r=input("¿Está seguro de modificar el nombre [",B.NomJAP,"] por [",nom2,"]? | (S - Si / N - No)")
	r=r.upper()
	while r!="S" and r!="N":
		print()
		print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		r=input("¿Está seguro de modificar el nombre [",B.NomJAP,"] por [",nom2,"]? | (S - Si / N - No)")
		r=r.upper()
	if r=="S":
		B.NomJAP=nom2
		alb.seek(puntB,0)
		pickle.dump(B,alb)
		alb.flush()
		print()
		print("Operación realizada con éxito...")
	else:
		print()
		print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

def ModDesc():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de DESCRIPCIÓN]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print()
	IngDesc()
	print()
	r=input("¿Está seguro de modificar la descripción de la obra? | (S - Si / N - No)")
	r=r.upper()
	while r!="S" and r!="N":
		print()
		print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		r=input("¿Está seguro de modificar la descripción de la obra? | (S - Si / N - No)")
		r=r.upper()
	if r=="S":
		B.Desc=desc
		alb.seek(puntB,0)
		pickle.dump(B,alb)
		alb.flush()
		print()
		print("Operación realizada con éxito...")
	else:
		print()
		print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

def ModTipo():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de TIPO]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print()
	if B.Tipo=="Anime":
		tip="Manga"
	else:
		tip="Anime"
	r=input("¿Está seguro de modificar el tipo de la obra? | (S - Si / N - No): ")
	r=r.upper()
	while r!="S" and r!="N":
		print()
		print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		r=input("¿Está seguro de modificar el tipo de la obra? | (S - Si / N - No): ")
		r=r.upper()
	if r=="S":
		B.Tipo=tip
		alb.seek(puntB,0)
		pickle.dump(B,alb)
		alb.flush()
		print()
		print("El tipo de la obra ha sido modificado a [",tip,"] exitosamente...")
	else:
		print()
		print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

#AGREGAR FUNCIONALIDAD PARA MODIFICAR LOS CAPÍTULOS VISTOS HASTA EL MOMENTO

def ModCap():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de CAPÍTULOS]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print()
	IngCap()
	print()
	r=input("¿Está seguro de modificar la cantidad de capítulos de la obra? | (S - Si / N - No): ")
	r=r.upper()
	while r!="S" and r!="N":
		print()
		print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
		print()
		r=input("¿Está seguro de modificar la cantidad de capítulos de la obra? | (S - Si / N - No): ")
		r=r.upper()
	if r=="S":
		B.CapL=cap
		alb.seek(puntB,0)
		pickle.dump(B,alb)
		alb.flush()
		print()
		print("Operación realizada con éxito...")
	else:
		print()
		print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

#AGREGAR FUNCIONALIDAD PARA MODIFICAR LOS TOMOS LEÍDOS HASTA EL MOMENTO

def ModTomo():
	os.system("cls")
	print()
	print("[MODIFICACIÓN de TOMOS]")
	alb.seek(puntB,0)
	B=pickle.load(alb)
	if B.Tipo!="Manga":
		print()
		print("La obra no se trata de un manga, por lo tanto no cuenta con tomos...")
	else:
		print()
		IngTomo()
		print()
		r=input("¿Está seguro de modificar la cantidad de tomos de la obra? | (S - Si / N - No)")
		r=r.upper()
		while r!="S" and r!="N":
			print()
			print("El caracter ingresado es incorrecto. Inténtelo nuevamente...")
			print()
			r=input("¿Está seguro de modificar la cantidad de tomos de la obra? | (S - Si / N - No)")
			r=r.upper()
		if r=="S":
			B.TomoL=tomo
			alb.seek(puntB,0)
			pickle.dump(B,alb)
			alb.flush()
			print()
			print("Operación realizada con éxito...")
		else:
			print()
			print("Operación cancelada con éxito...")

#------------------------------------------------------------------------------------------------------

def DatObra():
	os.system("cls")
	print()
	print("[DATOS DE LA OBRA]")
	print()
	alb.seek(puntB,0)
	B=pickle.load(alb)
	print("Código de la Obra: ",B.Cod)
	if B.NomENG!=" ":
		print("Nombre en Inglés de la obra: ",B.NomENG)
	if B.NomJAP!=" ":
		print("Nombre en Japonés de la obra: ",B.NomJAP)
	print("Descripción de la Obra: ")
	print()
	print(B.Desc)
	print()
	print("Tipo de Obra: ",B.Tipo)
	print("Capítulos totales de la Obra: ",B.CapL)
	if B.Tipo=="Manga":
		print("Tomos de la Obra: ",B.TomoL)

#------------------------------------------------------------------------------------------------------

def menumodifBD():
	os.system("cls")
	print()
	print("[MODIFICACIONES]")
	print()
	opcionBD()
	while opBD!=0:
		if opBD==1:
			ModNE()
		elif opBD==2:
			ModNJ()
		elif opBD==3:
			ModDesc()
		elif opBD==4:
			ModTipo()
		elif opBD==5:
			ModCap()
		elif opBD==6:
			ModTomo()
		else:
			DatObra()
		print()
		input("Presione [Enter] para continuar: ")
		os.system("cls")
		print()
		print("[MODIFICACIONES]")
		print()
		opcionBD()

#------------------------------------------------------------------------------------------------------

# Esta es la tercera opción del menú principal. Permite modificar algunos aspectos de las series 

# guardadas en la base de datos

def ModifBD():
	os.system("cls")
	print()
	print("[MODIFICACIONES]")
	print()
	if os.path.getsize(afb)!=0:
		pantallaBD()
		if y!=0:
			print()
			print("Ingrese [0] para finalizar...")
			print()
			IngCod()
			while cod!=0:
				if BuscarCod(cod)!=-1:
					menumodifBD()
				else:
					print()
					print("Esa obra no se encuentra registrada. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar: ")
				os.system("cls")
				print()
				print("[MODIFICACIONES]")
				print()
				pantallaBD()
				print()
				print("Ingrese [0] para finalizar...")
				print()
				IngCod()
		else:
			print()
			print("No hay datos ingresados en la base de datos.")
			print()
			input("Presione [Enter] para continuar: ")
	else:
		print()
		print("No hay datos ingresados en la base de datos.")
		print()
		input("Presione [Enter] para continuar: ")

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

def VerLis():
	os.system("cls")
	print()
	print("[VER LISTA]")
	print()
	pantallaBD()
	if y==0:
		print()
		print("No hay datos ingresados en la base de datos.")
	print()
	input("Presione [Enter] para continuar: ")

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Este es el módulo del Menú Principal que visualizará el usuario...

def menu():
	opcion()
	while op!=0:
		if op==1:
			AgregBD()
		elif op==2:
			ElimBD()
		elif op==3:
			ModifBD()
		else:
			VerLis()
		os.system("cls")
		opcion()

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Cerramos los archivos lógicos creados la comienzo para trabajar con los datos guardados...

def cerrar():
	#al.close()
	alb.close()

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Este es el Módulo del Programa Principal...

def ProgramaPrincipal():
	abrir()
	menu()
	cerrar()
#	alb.seek(0,0)
#	limB=os.path.getsize(afb)
#	while alb.tell()<limB:
#		B=pickle.load(alb)
#		print("ENG: ",B.NomENG)
#		print("JAP: ",B.NomJAP)
#		print("Tipo: ",B.Tipo)
#		print("Descripción:", B.Desc)
#		print("CapítulosL: ", B.CapL)
#		print("TomosL: ", B.TomoL)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

#Finalmente, ejecutamos el programa...

ProgramaPrincipal()