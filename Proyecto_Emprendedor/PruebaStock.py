#Este programa consistirá en un software genérico de almacenamiento de stock.

#El mismo contará con 2 menúes principales:

# 1- Administración   |   2- Stock

#En administración se podrá agregar, modificar y eliminar productos al stock. Además, podremos asignar los distintos proveedores de nuestros productos, agregar nuevos, etc.

#En stock podremos visualizar los productos en stock, sus nombres, su código de identificación, la cantidad disponible y su proveedor.

#Administracion
#    Proveedores
#        Agregar Proveedor (se pide nombre, mail/telefono, cuil, direccion, se asigna automaticamente un codigo)
#        Modificar Proveedores (Muestra los proveedores registrados. El usuario indica el proveedore que modificar y cambia los datos que desee)
#        Ver Proveedores (Muestra los proveedores registrados.)
#        Eliminar Proveedor (Muestra los proveedores. El usuario indica el proveedor que quiere eliminar. El sistema mostrará un aviso antes de realizar la acción)
#   Producto
#        Agregar Producto (pide cod, nombre, precio unitario, cantidad maxima y minima)
#        Modificar Producto (Muestra los productos registrados.)
#        Eliminar Producto (Muestra los productos registrados. El usuario elige el producto a eliminar. El sistema brinda un aviso)
#Stock
#   Ver lista (muetra nombre, stock, precio y si requiere reponer)
#   Agregar stock


#-------------------------------------------------------------------------
#print("","_".center(tm+2,"_"))
#print ("|","MENÚ PRINCIPAL".ljust(tm),"|")
#print("|".ljust(tm+2,"-"),"|")
#print ("|"," A - ADMINISTRACIÓN".ljust(tm),"|")
#print ("|"PrecioProducto," B - STOCK".ljust(tm),"|")
#print("","_".center(tm+2,"_"))
#-------------------------------------------------------------------------

""" 
def menuPrincipal():
	op = 3
	while op!=0:
		print("Menú Principal")
		print()
		print()
		print("1- Administración")
		print()
		print("2- Stock")
		opcion()
		if op == 1:
			Admin()
		else op == 2:
			Stock()
		Borrar()
	Borrar()
	print("Sesión Finalizada")
	print()
	print("Developed by SBSolutions")

"""


import pickle
import os
import os.path
import sys
import io
import string


tm=50
class PRODUCTO:
	def __init__(self):
		self.cod = "0".rjust(4, "0")
		self.nombre = " ".ljust(12, " ")
		self.precio = "0.00".rjust(8, "0")
		self.codProveedor = "0".rjust(8, "0")
		self.stock = "0".rjust(4, "0")
		self.cantMax = "0".rjust(4, "0")
		self.cantMin = "0".rjust(4, "0")
		self.Estado = " ".ljust(5, " ")

class PROVEEDOR:
	def __init__(self):
		self.cod = "0".rjust(4, "0")
		self.nombre = " ".ljust(12, " ")
		self.mail = " ".ljust(40, " ")
		self.telefono = "0".rjust(14, ' ')
		self.ciudad = " ".ljust(20, " ")
		self.calle = " ".ljust(20, " ")
		self.numCalle = "0".rjust(4, "0")
		self.Estado = " ".ljust(5, " ")


#------------------------DECLARACIONES-VARIABLES-SIMPLES---------------------------
afprod = "SBS_Software\Productos.dat"
afprov = "SBS_Software\Proveedores.dat"
carpeta = "SBS_Software"
tmprov = 262
tmprod = 211

#Funcion borrar adaptada para SO Linux, Windows y Apple
def Borrar():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

#-----------------------MANEJOS-ARCHIVOS---------------------------------------
#Módulo con el que establecemos las rutas de guardado de los archivos a utilizar y abrimos los archivos lógicos asociados.
def CrearCarpeta(carpeta):
	if not os.path.exists(carpeta):
		os.makedirs(carpeta)

def abrir():
	global alprod, alprov
	if os.path.exists(afprod)==True:
		alprod = open(afprod, "r+b")
	else:
		alprod = open(afprod, "w+b")
	if os.path.exists(afprov)==True:
		alprov = open(afprov, "r+b")
	else:
		alprov = open(afprov, "w+b")


#Módulo con el que cierro los archivos lógicos utilizados a lo largo del programa.
def cerrar():
	alprov.close()
	alprod.close()
	
#------------------------------BUSQUEDAS-----------------------------------------------------

#Módulo de búsqueda del nombre del proveedor en el archivo "ProveedoresARCHIVO.dat"
def BusquedaNombreProveedor(nom):
	prov = PROVEEDOR()
	puntProv = alprov.tell()
	alprov.seek(0,0)
	prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and prov.nombre != nom:
		puntProv = alprov.tell()
		prov = pickle.load(alprov)
	if prov.nombre != nom:
		puntProv = -1
	return puntProv

#Módulo de búsqueda del código del proveedor en el archivo "ProveedoresARCHIVO.dat"
def BuscarCodProv(x):
	alprov.seek(0,0)
	puntProv = alprov.tell()
	prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and (x != prov.cod):
		puntProv = alprov.tell()
		prov = pickle.load(alprov)
	if x == prov.cod and prov.Estado:
		return puntProv
	elif not prov.Estado:
		return -2
	else:
		return -1

#Módulo de búsqueda del nombre de un producto en el archivo "ProductosARCHIVO.dat"
def buscarNomProd(x):
	global puntProd
	if os.path.getsize(afprod) == 0:
		return -1
	else:
		alprod.seek(0,0)
		puntProd = alprod.tell()
		Prod = pickle.load(alprod)
		while os.path.getsize(afprod) > alprod.tell() and (x != Prod.nombre):
			puntProd = alprod.tell()
			Prod = pickle.load(alprod)
		if x == Prod.nombre:
			return puntProd
		else:
			return -1

#Módulo de búsqueda del código de un producto en el archivo "ProductosARCHIVO.dat".			
def buscarCodProd(x):
	global puntProd
	alprod.seek(0,0)
	puntProd = alprod.tell()
	Prod = pickle.load(alprod)
	while os.path.getsize(afprod) > alprod.tell() and (x != Prod.cod):
		puntProd = alprod.tell()
		Prod = pickle.load(alprod)
	if x == Prod.cod and Prod.Estado != "False":
		return puntProd
	else:
		return -1
#Módulo que busca productos dados de alta.d			
def buscoProdAlta():
	if os.path.getsize(afprod) != 0:
		alprod.seek(0,0)
		Prod = pickle.load(alprod)
		while os.path.getsize(afprod) > alprod.tell() and Prod.Estado != "True ":
			Prod = pickle.load(alprod)
		if Prod.Estado == "True ":
			return 1
		else:
			return -1	
#------------------------------ORDENAMIENTOS---------------------------------------------------------------------------------
def OrdenarProductos():
	try:
		alprod.seek(0,0)
		prod = pickle.load(alprod)
		tam = alprod.tell()
		alprod.seek(0,0)
		for i in range((os.path.getsize(afprod)//tam)-1):
			for j in range(i+1,(os.path.getsize(afprod)//tam)-1):
				alprod.seek(i*tam)
				prod1 =  pickle.load(alprod) 
				alprod.seek(j*tam)
				prod2 =  pickle.load(alprod) 
				if int(prod1.cod) < int(prod2.cod):
					alprod.seek(i*tam)
					pickle.dump(prod2,alprod)
					alprod.seek(j*tam)
					pickle.dump(prod1,alprod)
	except:
		a = ""

#------------------------------VALIDACIONES----------------------------------------------------------------------------------
#Este módulo valida que el formato del MAIL sea correscto
def ValidarMail(mail):
	try:
		mail = mail.strip().partition("@")
		nombre, arroba, dom = mail
		dom = dom.partition(".")
		dom1,punto,dom2 = dom
		if (len(nombre) > 0 and len(dom1) > 0 and len(dom2) > 0) or nombre == '-':
			return False
		else:
			return True
	except:
		return True

#Este módulo valida que el formato del TELEFONO sea correscto	
def ValidarTelefono(tel):
	if (tel.isdigit() and len(tel)<=14) or tel == "-":
		False
	else:
		True

def Tamaño(tm):
	tm = tm-8
	if tm%4 ==0:
		b = int(tm//4)
		a = b+5
		d = b-5
		c = b-3
	elif tm%4 == 1:
		b = int(tm//4)
		a = b+5
		d = b-4
		c = b-3
	elif tm%4 == 2:
		b = int(tm//4)+1
		a = b+4
		d = b-5
		c = b-4
	else:
		b = 1+int(tm//4)
		a = b+4
		d = b-5
		c = b-3
	return a,b,c,d

#------------------------------OPCIONES--------------------------------------------------------------------------------------

#Módulo correspondiente a la variable que ingresa el usuario para elegír la opción a la que quiere ingresar del menú principal
def opcion():
	global op
	op = input("Ingrese el número de la opción a la que desee acceder: ")
	while op.isdigit()==False:
		print("Error. Ingrese un número correspondiente a una opción del menú")
		input("Presione [Enter] para continuar...")
		Borrar()
		op = input("Ingrese el número de la opción a la que desee acceder: ") 
	op=int(op)
	while op<0 or op>2:
		print("Error. El número ingresado no corresponde a una opción del menú. Inténtelo nuevamente.")
		input("Presione [Enter] para continuar...")
		Borrar()
		op = int(input("Ingrese el número de la opción a la que desee acceder: "))

#Módulo que permite elegir las distintas opciones del módulo "Proveedores".
def opcion1():
	global op1
	op1 = input("Ingrese el número de la opción a la que desee acceder: ")
	while op1.isdigit()==False:
		print("Error. Ingrese un número correspondiente a una opción del menú")
		input("Presione [Enter] para continuar...")
		Borrar()
		op1 = input("Ingrese el número de la opción a la que desee acceder: ") 
	op1=int(op1)
	while op1<0 or op1>4:
		print("Error. El número ingresado no corresponde a una opción del menú. Inténtelo nuevamente.")
		input("Presione [Enter] para continuar...")
		Borrar()
		op1 = int(input("Ingrese el número de la opción a la que desee acceder: "))

#Módulo que permite elegir las distintas opciones del menú "Productos".
def opcion2():
	global op2
	op2 = input("Ingrese el número de la opción a la que desee acceder: ")
	while op2.isdigit()==False:
		print("Error. Ingrese un número correspondiente a una opción del menú")
		input("Presione [Enter] para continuar...")
		Borrar()
		op2 = input("Ingrese el número de la opción a la que desee acceder: ") 
	op2=int(op2)
	while op2<0 or op2>3:
		print("Error. El número ingresado no corresponde a una opción del menú. Inténtelo nuevamente.")
		input("Presione [Enter] para continuar...")
		Borrar()
		op2 = int(input("Ingrese el número de la opción a la que desee acceder: "))

#------------------------------MENUS------------------------------------------
#Módulo que muestra el conjunto de proveedores registrados en el sistema.
def pantallaProv():
	a=((tm)*3)//10-2
	b =int(((tm-.1)*7)//10-2)
	alprov.seek(0,0)
	print("|".ljust(tm," "),"|")
	print("|".ljust(tm,"-"),"|")
	print("|".ljust(tm," "),"|")
	print("|","Código".center(a),"|","Nombre".center(b),"|")
	while os.path.getsize(afprov) > alprov.tell():
		prov = pickle.load(alprov)
		if prov.Estado:
			print("|",prov.cod.center(a),"|",prov.nombre.strip().center(b),"|")
	print("|","_".center(a,"_"),  "|","_".center(b,"_"),"|")

#1er Módulo del menú "Proveedores". Permite registrar proveedores en el sistema.
def CargaProveedor(prov):
	Borrar()
	print(" Ingrese '-' si el proveedor no tiene mail")
	aux = input("ingrese el nuevo mail del proveedor:").ljust(40)
	while len(aux)>40 or ValidarMail(aux):
		Borrar()
		print(" Mail inválido ")
		if len(aux)>40:
			print(" La longitur del mail no debe ser mayo a 40 caracteres")
		else:
			print(" El mail debe tener el formato Ejemplo@Domino.com ")
		print("")
		aux = input("ingrese el nuevo mail del proveedor:").ljust(40)
	prov.mail = aux
	Borrar()
	print(" Ingrese '-' si el proveedor no tiene telefono")
	aux = input("ingrese el telefono del proveedor:").rjust(14, ' ')
	while ValidarTelefono(aux):
		Borrar()
		if aux.isdigit():
			print(" El telefono debe estar compuesto unicamente por numeros")
		else:
			print(" El telefono debe tener una longitud menor a 14 caracteres")
		aux = input("ingrese el telefono del proveedor:").rjust(14, ' ')	
	prov.telefono = aux
	Borrar()
	aux = input("ingrese la ciudad del proveedor:").ljust(20)
	while len(aux) >20:
		Borrar()
		print(" La ciudad debe tener una longitud menor a 20 digitos")
		aux = input("ingrese la ciudad del proveedor:").ljust(20)
	prov.ciudad = aux
	Borrar()
	aux = input("ingrese la calle del proveedor:").capitalize().ljust(20)
	while len(aux) >20:
		Borrar()
		print(" La calle debe tener una longitud menor a 20 digitos")
		aux = input("ingrese la calle del proveedor:").capitalize().ljust(20)
	prov.calle = aux
	aux = input("ingrese la altura:").rjust(4, '0')
	while len(aux) > 4 or not aux.isdigit():
		Borrar()
		if len(aux) > 4:
			print(" La altura debe ser menor a 10000")
		else:
			print(" La altura debe contener unicamente numeros")
		aux = input("ingrese la altura:").rjust(4, '0')
	prov.numCalle = aux
def AgregarProv():
	prov = PROVEEDOR()
	opA = ""
	while opA != "N":
		aux = input("ingrese el nombre del proveedor:").ljust(12)
		if os.path.getsize(afprov)>0:
			if BusquedaNombreProveedor(aux) != -1:
				Borrar()
				print("El proveedor ", aux.strip()," ya existe")
			else:
				prov.nombre = aux.ljust(12)
				#hacer validaciones
				CargaProveedor(prov)
				prov.Estado = "True "
				prov.cod = str(os.path.getsize(afprov)//tmprov + 2).rjust(4, "0")
				pickle.dump(prov,alprov)
				alprov.flush()
				Borrar()
				print("Proveedor agregado exitosamente.")
		else:
			prov.nombre = aux.ljust(12)
			CargaProveedor(prov)
			prov.cod = "1".rjust(4, "0")
			pickle.dump(prov,alprov)
			alprov.flush()
			Borrar()
			print("Proveedor agregado exitosamente.")
		opA = input("desea agregar otro proveedor? (S/N): ").upper()
		while opA!= "S" and opA!= "N":
			Borrar()
			opA = input("desea agregar otro proveedor? (S/N): ").upper()

#3er Módulo del menú "Proveedores". Visualiza los proveedores registrados en el sistema junto con sus datos.
def VerProv():
	if os.path.getsize(afprov) == 0:
		print("|".ljust(90," "),"|")
		print("|".ljust(90,"-"),"|")
		print("|".ljust(90," "),"|")
		print("| No hay proveedores cargados".ljust(90," "),"|")
		print("|".ljust(90,"_"),"|")
	else:	
		print("|".ljust(90," "),"|")
		print("|".ljust(90,"-"),"|")
		print("|".ljust(90," "),"|")
		print("|","Proveedores registrados".center(88),"|")
		print("|".ljust(90," "),"|")
		print("|".ljust(90,"-"),"|")
		print("|  Código  |       Nombre    |                    Mail                    |    Teléfono    |")
		alprov.seek(0)
		while os.path.getsize(afprov) > alprov.tell():
			prov = pickle.load(alprov)
			if prov.Estado == "True ":
				print("|",prov.cod.center(8," "),"|",prov.nombre.strip().center(15," "),"|",prov.mail.strip().center(42," "),"|",prov.telefono.center(12," "),"|")
		print("|".ljust(90,"_"),"|")

#2do Módulo del menú "Proveedores". Permite al usuario modificar datos de los proveedores registrados en el sistema.
def ModProveedor(prov):	
	print("Antiguo nombre del proveedor: ", prov.nombre)
	aux = input("ingrese el nuevo nombre del proveedor:").ljust(12)
	res = ""
	while BusquedaNombreProveedor(aux) != -1 and res != "N":
		Borrar()
		print("El proveedor ", aux.strip()," ya existe")
		print("")
		res = print(" ¿Desea continuar? (S/N): ").upper()
	if res != "N":
		prov.nombre = aux
		Borrar()
		print("Antiguo mail del proveedor: ", prov.mail)
		print(" Ingrese '-' si el proveedor no tiene mail")
		aux = input("ingrese el nuevo mail del proveedor:").ljust(40)
		while len(aux)>40 or ValidarMail(aux):
			Borrar()
			print(" Mail inválido ")
			if len(aux)>40:
				print(" La longitur del mail no debe ser mayo a 40 caracteres")
			else:
				print(" El mail debe tener el formato Ejemplo@Domino.com ")
			print("")
			aux = input("ingrese el nuevo mail del proveedor:").ljust(40)
		prov.mail = aux
		Borrar()
		print("Antiguo telefono del proveedor: ", prov.telefono.strip())
		print(" Ingrese '-' si el proveedor no tiene telefono")
		aux = input("ingrese el telefono del proveedor:").rjust(14, ' ')
		while ValidarTelefono(aux):
			Borrar()
			if aux.isdigit():
				print(" El telefono debe estar compuesto unicamente por numeros")
			else:
				print(" El telefono debe tener una longitud menor a 14 caracteres")
			aux = input("ingrese el telefono del proveedor:").rjust(14, ' ')
		prov.telefono = aux	
		Borrar()
		print("Antigua ciudad del proveedor: ", prov.ciudad.strip())
		aux = input("ingrese la ciudad del proveedor:").capitalize().ljust(20)
		while len(aux) >20:
			Borrar()
			print(" La ciudad debe tener una longitud menor a 20 digitos")
			aux = input("ingrese la ciudad del proveedor:").capitalize().ljust(20)
		prov.ciudad = aux
		Borrar()
		print("Antigua calle del proveedor: ", prov.calle.strip())
		aux = input("ingrese la calle del proveedor:").capitalize().ljust(20)
		while len(aux) >20:
			Borrar()
			print(" La calle debe tener una longitud menor a 20 digitos")
			aux = input("ingrese la calle del proveedor:").capitalize().ljust(20)
		prov.calle = aux
		print("Antigua altura del proveedor: ", prov.numCalle.strip('0'))
		aux = input("ingrese la altura:").rjust(4, '0')
		while len(aux) > 4 or not aux.isdigit():
			Borrar()
			if len(aux) > 4:
				print(" La altura debe ser menor a 10000")
			else:
				print(" La altura debe contener unicamente numeros")
			aux = input("ingrese la altura:").rjust(4, '0')
		prov.numCalle = aux
def ModifProv():
	if os.path.getsize(afprov) > 0:
		seguir = " "
		while seguir != "N":
			Borrar()
			print("","_".ljust(90,"_"))
			print("|".ljust(90," "),"|")
			print("|","MODIFICAR PROVEEDORES".center(88),"|")
			VerProv()
			cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(4,"0")
			cont = 1
			seguir = " "
			while BuscarCodProv(cod) < 0 and seguir != "N":
				Borrar()
				print("","_".ljust(90,"_"))
				print("|".ljust(90," "),"|")
				print("|","MODIFICAR PROVEEDORES".center(88),"|")
				VerProv()
				print("| No existe ningun proveedor con el codigo ingresado".ljust(88),"|")
				cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(4, "0")
				cont = cont + 1 
				if cont >= 4:
					Borrar()
					print("","_".ljust(90,"_"))
					print("|".ljust(90," "),"|")
					print("|","MODIFICAR PROVEEDORES".center(88),"|")
					VerProv()
					print("  Ha ingresado un código inexistente demasiadas veces")
					seguir = input("  ¿Desea intentar una vez más? (S/N) ").upper()
					while seguir != "S" and seguir != "N":
						Borrar()
						print("","_".ljust(90,"_"))
						print("|".ljust(90," "),"|")
						print("|","MODIFICAR PROVEEDORES".center(88),"|")
						VerProv()
						print("|","Ha ingresado un sódigo inexistente demasiadas veces".center(88),"|")
						seguir = input("| ¿Desea intentar una vez más? (S/N) ").upper()
					cont = 1
					if seguir == "S":
						VerProv()
						cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(4, "0")
			if seguir != "N":
				alprov.seek(BuscarCodProv(cod))
				prov = pickle.load(alprov)
				ModProveedor(prov)
				confirmar = ""
				while confirmar != 'N' and confirmar != 'S':
					Borrar()
					print(" Actualizar el provedor a :")
					print(f" Nombre: {prov.nombre.strip()}\n Mail: {prov.mail.strip()}\n Telefono: {prov.telefono.strip('0')}\n Ciudad: {prov.ciudad.strip()}\n Direccion: {prov.calle.strip()} {prov.numCalle.strip('0')}")
					confirmar = input("(S/N)").upper()
				if confirmar == "S":
					alprov.seek(tmprov*(int(cod.strip())-1))
					pickle.dump(prov,alprov)
					alprov.flush()
					Borrar()
					print("","_".ljust(90,"_"))
					print("|".ljust(90," "),"|")
					print("|","MODIFICAR PROVEEDORES".center(88),"|")
					print("  Proveedor modificado exitosamente")
				seguir = input("  ¿Desea modificar otro proveedor? (S/N) ").upper()
				while seguir != "S" and seguir != "N":
					Borrar()
					print("","_".ljust(90,"_"))
					print("|".ljust(90," "),"|")
					print("|","MODIFICAR PROVEEDORES".center(88),"|")
					VerProv()
					print("|","Proveedor modificado exitosamente".center(88),"|")
					seguir = input("| ¿Desea modificar otro proveedor? (S/N) ").upper()
	else:	
		Borrar()
		print("","_".ljust(90,"_"))
		print("|".ljust(90," "),"|")
		print("|","MODIFICAR PROVEEDORES".center(88),"|")
		VerProv()
		print("")
		input(" Precione [ENTER] tecla para volver")

#4to Módulo del menú "Proveedores". Permite eliminar proveedores del sistema. Estos pueden ser recuperados a través de la opción "Agregar Proveedor" del menú "Proveedores".
def ElimProv():
	res = ""
	cod = ""
	while res != 'N' and cod != '0000':
		while BuscarCodProv(cod) <= -1 and cod != '0000':
			Borrar()
			print("","_".ljust(tm,"_"))
			print("|".ljust(tm," "),"|")
			print("|","ELIMINAR PROVEEDORES".center(tm-2),"|")
			pantallaProv()
			print("")
			cod = input(" Ingrese el codigo del proveedor que desea eliminar ('0' para salir): ").rjust(4,'0')
		while res != 'N' and res != 'S' and cod != '0000':
			Borrar()
			print("","_".ljust(tm,"_"))
			print("|".ljust(tm," "),"|")
			print("|","ELIMINAR PROVEEDORES".center(tm-2),"|")
			print("|".ljust(tm," "),"|")
			print("|".ljust(tm,"-"),"|")
			print("|".ljust(tm," "),"|")
			print("|","_".ljust(tm-2,"_"),"|")
			alprov.seek(BuscarCodProv(cod))
			prov = pickle.load(alprov)
			print(f' Seguro que desea eliminar al proveedor "{prov.nombre.strip()}" (S/N):', end="")
			res = input().upper()
		if res == 'N':
			Borrar()
			print("","_".ljust(tm,"_"))
			print("|".ljust(tm," "),"|")
			print("|","ELIMINAR PROVEEDORES".center(tm),"|")
			print("|".ljust(tm," "),"|")
			print("|".ljust(tm,"-"),"|")
			print("|".ljust(tm," "),"|")
			print("|"," Eliminacion cancelada".ljust(tm-2," "),"|")
			print("|"," Preciona [ENTER] para continuar".ljust(tm-2," "),"|")
			print("|","_".ljust(tm-2,"_"),"|")
			input("")
		elif res=='S':
			prov.Estado = "False"
			alprov.seek(BuscarCodProv(cod), 0)
			pickle.dump(prov,alprov)
			Borrar()
			print("","_".ljust(tm,"_"))
			print("|".ljust(tm," "),"|")
			print("|","ELIMINAR PROVEEDORES".center(tm),"|")
			print("|".ljust(tm," "),"|")
			print("|".ljust(tm,"-"),"|")
			print("|".ljust(tm," "),"|")
			print("| "," Proveedor eliminado correctamente".ljust(tm-2," "),"|")
			print("|"," Preciona [ENTER] para continuar".ljust(tm-2," "),"|")
			print("|","_".ljust(tm-2,"_"),"|")
			input("")
		res = ""
		while res != 'N' and res != 'S' and cod != '0000':
			Borrar()
			print("","_".ljust(tm,"_"))
			print("|".ljust(tm," "),"|")
			print("|","ELIMINAR PROVEEDORES".center(tm-2),"|")
			print("|".ljust(tm," "),"|")
			print("|".ljust(tm,"-"),"|")
			print("|".ljust(tm," "),"|")
			print("|","_".ljust(tm-2,"_"),"|")
			res = input("Desea eliminar otro proveedor (S/N): ").upper()
	
#Módulo perteneciente al menú "Administración". Contiene las funciones asociadas a los proveedores del comercio.
def Proveedores():
	Borrar()
	print("PROVEEDORES")
	print()
	print()
	print("1- Agregar Proveedor")
	print()
	print("2- Modificar Proveedores")
	print()
	print("3- Ver Proveedores")
	print()
	print("4- Eliminar Proveedor")
	print()
	print("0- Volver al menú anterior")
	print()
	opcion1()
	while op1 != 0:
		if op1 == 1:
			Borrar()
			AgregarProv()
		elif op1 == 2:
			ModifProv()
		elif op1 == 3:
			Borrar()
			print("","_".ljust(90,"_"))
			print("|".ljust(90," "),"|")
			print("|","VER PROVEEDORES".center(88),"|")
			VerProv()
			print(" ")
			input(" Precione [ENTER] tecla para volver")
		else:
			ElimProv()
		Borrar()
		print("PROVEEDORES")
		print()
		print()
		print("1- Agregar Proveedor")
		print()
		print("2- Modificar Proveedores")
		print()
		print("3- Ver Proveedores")
		print()
		print("4- Eliminar Proveedor")
		print()
		print("0- Volver al menú anterior")
		print()
		opcion1()


#Módulo en el que se ingresa y valida el precio de un producto. Utilizado en la función "Agregar Producto" del menú "Productos".
def ingresaPrecioProducto():
	global precio
	Borrar()
	precio = input("Ingrese el precio del producto a registrar (en pesos [ARS]): ")
	band = True
	while band:
		if len(precio)>10:
			Borrar()
			print("\n Error. Ingrese valores numéricos < 100000 \n Inténtelo nuevamente.")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			precio = input("Ingrese el precio del producto a registrar (en pesos [ARS]): ")
		else:
			try:
				precio = round(float(precio),2)
				band = False
			except:
				Borrar()
				print("\n Error. Ingrese valores numéricos.\n Inténtelo nuevamente.")
				input("\n Presione [Enter] para continuar...")
				Borrar()
				precio = input("Ingrese el precio del producto a registrar (en pesos [ARS]): ")
	precio = str(precio)
	precio = precio.rjust(8, "0")

#Módulo en el que se elige el proveedor del que se obtuvo el producto a registrar. Luego, se obtiene el código del proveedor.
def ingresaCodigoProveedor():
	global codProv
	Borrar()
	pantallaProv()
	print()
	print()
	codProv = input("Ingrese el código del proveedor del producto a registrar: ").rjust(4,"0")
	while BuscarCodProv(codProv) <= -1:
		print()
		print("El código ingresado no corresponde a un proveedor registrado. Inténtelo nuevamente...")
		print()
		input("Presione [Enter] para continuar...")
		Borrar()
		pantallaProv()
		print()
		print()
		codProv = input("Ingrese el código del proveedor del producto a registrar: ").rjust(4,"0")
	
#1er Módulo del menú "Productos". Permite registrar nuevos productos en el sistema
def AgregProd():
	Borrar()
	print("Agregar Producto")
	print()
	print()
	if os.path.getsize(afprov) == 0:
		print("No hay proveedores registrados. Ingrese proveedores en el sistema para luego continuar con el registro de productos.")
		print()
		input("Presione [Enter] para continuar...")
	else:
		Prod = PRODUCTO()
		nomProd = input("Ingrese el nombre del producto que desea registrar (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
		nomProd = nomProd.ljust(12, " ")
		nomProd = nomProd.title()
		while nomProd != "**          ":
			while len(nomProd)>12:
				print("El nombre del producto no debe superar los 12 caracteres. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar...")
				Borrar()
				print("Agregar Producto")
				print()
				print()
				nomProd = input("Ingrese el nombre del producto que desea registrar (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
				nomProd = nomProd.ljust(12, " ")
				nomProd = nomProd.title()
			#En este caso, el producto no se encuentra registrado
			if buscarNomProd(nomProd) == -1:
				#Si no hay productos ingresados, el código del primer producto será 1.
				if os.path.getsize(afprod) == 0:
					codProd = "1"
					codProd = codProd.rjust(4, "0")
				#Si ya hay 1 o más productos registrados, el sistema otorgará como código el número que le sigue al último producto del registro
				else:
					alprod.seek(0,0)
					Prod = pickle.load(alprod)
					tamRegProd = alprod.tell()
					cantRegProd = (os.path.getsize(afprod))//(tamRegProd)
#					puntUltimoProducto = ((cantRegProd)-1)*tamRegProd
#					alprod.seek(puntUltimoProducto, 0)
#					Prod = pickle.load(alprod)
#					Prod.cod = int(Prod.cod)
#					codProd = Prod.cod + 1
#					codProd = str(codProd)
#					codProd = codProd.rjust(4, "0")
					codProd = cantRegProd + 1
					codProd = str(codProd)
					codProd = codProd.rjust(4, "0")
				ingresaPrecioProducto()
				ingresaCodigoProveedor()
				alprod.seek(0,2)
				Prod.cod = codProd
				Prod.nombre = nomProd
				Prod.precio = precio
				Prod.codProveedor = codProv
				Prod.Estado = "True "
				pickle.dump(Prod, alprod)
				alprod.flush()
				print()
				print("Producto registrado con éxito...")
			#En este caso, el producto ya se encuentra registrado. En consecuencia, muestra una advertencia al usuario.
			else:
				alprod.seek(puntProd, 0)
				Prod = pickle.load(alprod)
				if Prod.Estado == "False":
					print()
					print("El producto fue dado de baja anteriormente. ¿Desea restaurarlo en el sistema?")
					res = input('(S | N): ')
					res = res.upper()
					while res != 'S' and res != 'N':
						print()
						print("Error. Ingrese [S] o [N] para continuar...")
						print()
						input('Presione [Enter] para continuar...')
						Borrar()
						print("Agregar Producto")
						print()
						print()
						print("Ingrese el nombre del producto que desea registrar (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
						print()
						print("El producto fue dado de baja anteriormente. ¿Desea restaurarlo en el sistema?")
						res = input('(S | N): ')
						res = res.upper()
					if res == 'S':
						Prod.Estado = "True "
						alprod.seek(puntProd, 0)
						pickle.dump(Prod, alprod)
						alprod.flush()
						print()
						print("Producto restaurado en el sistema con éxito. Para realizar las modificaciones pertinentes, diríjase a la función [Modificar Producto].")
					else:
						print()
						print("Operación cancelada con éxito...")
				else:
					print()
					print("El producto ya se encuentra registrado...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("Agregar Producto")
			print()
			print()
			Prod = PRODUCTO()
			OrdenarProductos()
			nomProd = input("Ingrese el nombre del producto que desea registrar (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
			nomProd = nomProd.ljust(12, " ")
			nomProd = nomProd.title()

#Función que devuelve el nombre de un proveedor dado.
def nombreProv(x):
	alprov.seek(0,0)
	Prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and x != Prov.cod:
		Prov = pickle.load(alprov)
	if x == Prov.cod:
		return Prov.nombre
 


#Módulo de búsqueda del código de un producto en el archivo "ProductosARCHIVO.dat".


#Módulo que permite modificar el nombre de un producto
def modifNomProd(x):
	Borrar()
	print("MODIFICACIÓN DE NOMBRE DE PRODUCTO")
	print()
	print()
	newNombre = input("Ingrese el nuevo nombre del producto (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
	newNombre = newNombre.ljust(12, " ")
	newNombre = newNombre.title()
	while newNombre != "**          ":
		while len(newNombre) > 12:
			print()
			print("Error. Se excedió el máximo de caracteres. Inténtelo nuevamente...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("MODIFICACIÓN DE NOMBRE DE PRODUCTO")
			print()
			print()
			newNombre = input("Ingrese el nuevo nombre del producto (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
			newNombre = newNombre.ljust(12, " ")
			newNombre = newNombre.title()
		Borrar()
		print("MODIFICACIÓN DE NOMBRE DE PRODUCTO")
		print()
		print()
		print("¿Está seguro de que desea cambiar el nombre [", x.nombre, "] por [", newNombre, "]?")
		res = input("(S | N): ")
		res = res.upper()
		while res != 'S' and res != 'N':
			print()
			print("Error. Ingrese 'S' o 'N' para continuar...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("MODIFICACIÓN DE NOMBRE DE PRODUCTO")
			print()
			print()
			print("¿Está seguro de que desea cambiar el nombre [", x.nombre, "] por [", newNombre, "]?")
			res = input("(S | N): ")
			res = res.upper()
		if res == 'S':
			x.nombre = newNombre
			alprod.seek(puntProd,0)
			pickle.dump(x, alprod)
			alprod.flush()
			print()
			print("Nombre del Producto actualizado correctamente...")
		else:
			print()
			print("Operación cancelada con éxito...")
		print()
		input("Presione [Enter] para continuar...")
		Borrar()
		print("MODIFICACIÓN DE NOMBRE DE PRODUCTO")
		print()
		print()
		newNombre = input("Ingrese el nuevo nombre del producto (Máximo 12 caracteres) - (Ingrese [**] para finalizar): ")
		newNombre = newNombre.ljust(12, " ")
		newNombre = newNombre.title()


#Módulo que muestra el conjunto de productos registrados en el sistema.
def pantallaProd():
	alprod.seek(0,0)
	while os.path.getsize(afprod) > alprod.tell():
		Prod = pickle.load(alprod)
		if Prod.Estado == "True ":
			print()
			print("Código del Producto: ", Prod.cod)
			print("Nombre del Producto: ", Prod.nombre)
			print("Precio del Producto: $", Prod.precio.strip('0').strip('.'), "[ARS]")
			print("Proveedor del Producto: ", nombreProv(Prod.codProveedor))
			print()
#Módulo que permite modificar el proveedor de un producto.
def modifProvProd(x):
	Borrar()
	print("MODIFICACIÓN DEL PROVEEDOR DEL PRODUCTO")
	print()
	print()
	pantallaProv()
	print()
	newProv = input("Ingrese el código del nuevo proveedor (Ingrese [0] para finalizar): ")
	while newProv != '0':
		if BuscarCodProv(newProv) > -1:
			Borrar()
			print("MODIFICACIÓN DEL PROVEEDOR DEL PRODUCTO")
			print()
			print()
			print("¿Está seguro de que desea modificar el proveedor [", x.codProveedor, "] por [", newProv, "]?")
			res = input("(S | N): ")
			res = res.upper()
			while res != 'S' and res != 'N':
				print()
				print("Error. Ingrese 'S' o 'N' para continuar.")
				print()
				input('Presione [Enter] para continuar...')
				Borrar()
				print("MODIFICACIÓN DEL PROVEEDOR DEL PRODUCTO")
				print()
				print()
				print("¿Está seguro de que desea modificar el proveedor [", x.codProveedor, "] por [", newProv, "]?")
				res = input("(S | N): ")
				res = res.upper()
			if res == 'S':
				x.codProveedor = newProv
				alprod.seek(puntProd, 0)
				pickle.dump(x, alprod)
				alprod.flush()
				print()
				print("Proveedor modificado con éxito...")
			else:
				print()
				print("Operación cancelada con éxito")
			print()
			input('Presione [Enter] para continuar...')
		else:
			print()
			print("El código ingresado es incorrecto. Inténtelo nuevamente...")
			print()
			input('Presione [Enter] para continuar...')
		Borrar()
		print("MODIFICACIÓN DEL PROVEEDOR DEL PRODUCTO")
		print()
		print()
		pantallaProv()
		print()
		newProv = input("Ingrese el código del nuevo proveedor (Ingrese [0] para finalizar): ")

#Módulo que permite modificar el precio del producto seleccionado.
def modifPrecioProd(x):
	band = True
	while band:
		Borrar()
		print("MODIFICACIÓN DEL PRECIO DEL PRODUCTO")
		print()
		print()
		newPrice = input("Ingrese el nuevo precio del producto (En pesos [ARS]) - (Ingrese [0] para finalizar): ")
		if len(newPrice)>10:
			Borrar()
			print("\n Error. Ingrese valores numéricos < 100000 \n Inténtelo nuevamente.")
			print()
			input("Presione [Enter] para continuar...")
		elif newPrice =="0":	
			band = False
		else:
			try:
				newPrice = round(float(newPrice),2)
				if newPrice < 0:
					print()
					print("Error. Ingrese valores mayores que 0...")
					print()
					input('Presione [Enter] para continuar...')
				else:
					band = False
			except:
				Borrar()
				print("\n Error. Ingrese valores numéricos. Inténtelo nuevamente.")
				input("\n Presione [Enter] para continuar...")
	if newPrice != "0":
		newPrice = str(newPrice)
		newPrice = newPrice.rjust(8, "0")
		print()
		print("¿Está seguro de que desea modificar el precio del producto [", x.nombre, "] de [", x.precio, "] ARS a [", newPrice, "] ARS?")
		res = input("(S | N): ")
		res = res.upper()
		while res != 'S' and res != 'N':
			print()
			print("Ingrese [S] o [N] para continuar...")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("MODIFICACIÓN DEL PRECIO DEL PRODUCTO")
			print()
			print()
			print("¿Está seguro de que desea modificar el precio del producto [", x.nombre, "] de [", x.precio, "] ARS a [", newPrice, "] ARS?")
			res = input("(S | N): ")
			res = res.upper()
		if res == 'S':
			x.precio = newPrice
			alprod.seek(puntProd, 0)
			pickle.dump(x, alprod)
			alprod.flush()
			print()
			print("Precio modificado con éxito...")
		else:
			print()
			print("Operación cancelada con éxito...")
		print()
		input('Presione [Enter] para continuar...')
				

#2do Módulo del menú "Productos". Permite modificar los productos registrados en el sistema.
def ModifProd():
	Borrar()
	print("MODIFICAR PRODUCTO")
	print()
	print()
	if os.path.getsize(afprod) == 0 or buscoProdAlta() == -1:
		print("No se encontraron productos registrados en el sistema. Para utilizar esta función, registre al menos un producto con la opción [Agregar Producto].")
		print()
		input("Presione [Enter] para continuar...")
	else:
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")
		while codProd.isdigit()==False:
			print()
			print("Error. El dato ingresado no es un número. Inténtelo nuevamente...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("MODIFICAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")
		while buscarCodProd(codProd) == -1 and codProd != "0":
			print()
			print("El código del producto ingresado no se encuentra registrado. Inténtelo nuevamente...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("MODIFICAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")
		while codProd != "0":
			alprod.seek(puntProd,0)
			Prod = pickle.load(alprod)
			Borrar()
			print("MODIFICAR PRODUCTO")
			print("[", Prod.nombre, "]")
			print()
			print()
			print("1- Nombre del Producto")
			print()
			print("2- Proveedor del Producto")
			print()
			print("3- Precio del Producto")
			print()
			print("0- Volver al menú anterior")
			print()
			opcion2()
			while op2 != 0:
				if op2 == 1:
					modifNomProd(Prod)
				elif op2 == 2:
					modifProvProd(Prod)
				else:
					modifPrecioProd(Prod)
				Borrar()
				print("MODIFICAR PRODUCTO")
				print("[", Prod.nombre, "]")
				print()
				print()
				print("1- Nombre del Producto")
				print()
				print("2- Proveedor del Producto")
				print()
				print("3- Precio del Producto")
				print()
				print("0- Volver al menú anterior")
				print()
				opcion2()
				OrdenarProductos()
			Borrar()
			print("MODIFICAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")
			while codProd.isdigit()==False:
				print()
				print("Error. El dato ingresado no es un número. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar...")
				Borrar()
				print("MODIFICAR PRODUCTO")
				print()
				print()
				pantallaProd()
				print()
				codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")
			while buscarCodProd(codProd) == -1 and codProd != "0":
				print()
				print("El código del producto ingresado no se encuentra registrado. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar...")
				Borrar()
				print("MODIFICAR PRODUCTO")
				print()
				print()
				pantallaProd()
				print()
				codProd = input("Ingrese el código del producto que desea modificar (Ingrese [0] para volver al menú anterior): ")

#3er Módulo del menú "Productos". Elimina los productos indicados por el usuario. Pueden ser recuperados haciendo uso de la opción "Agregar Producto" del menú "Productos".
def ElimProd():
	Borrar()
	print("ELIMINAR PRODUCTO")
	print()
	print()
	if os.path.getsize(afprod) == 0 or buscoProdAlta() == -1:
		print("No se encontraron productos registrados en el sistema. Para utilizar esta función, registre al menos un producto con la opción [Agregar Producto].")
		print()
		input("Presione [Enter] para continuar...")
	else:
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")
		while codProd.isdigit()==False:
			print()
			print("Error. El dato ingresado no es un número. Inténtelo nuevamente...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("ELIMINAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")
		while buscarCodProd(codProd) == -1 and codProd != "0":
			print()
			print("El código del producto ingresado no se encuentra registrado. Inténtelo nuevamente...")
			print()
			input("Presione [Enter] para continuar...")
			Borrar()
			print("ELIMINAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")
		while codProd != "0":
			alprod.seek(puntProd,0)
			Prod = pickle.load(alprod)
			Borrar()
			print("ELIMINAR PRODUCTO")
			print()
			print()
			print("¿Está seguro de que desea eliminar el producto [", Prod.nombre, "] del sistema? En caso de que desee volver a registrarlo, diríjase a la opción [Agregar Producto].")
			res = input("(S | N): ")
			res = res.upper()
			while res != 'S' and res != 'N':
				print()
				print("Error. Ingrese [S] o [N] para continuar con la operación...")
				print()
				input('Presione [Enter] para continuar...')
				Borrar()
				print("ELIMINAR PRODUCTO")
				print()
				print()
				print("¿Está seguro de que desea eliminar el producto [", Prod.nombre, "] del sistema? En caso de que desee volver a registrarlo, diríjase a la opción [Agregar Producto].")
				res = input("(S | N): ")
				res = res.upper()	
			if res == 'S':
				Prod.Estado = "False"
				alprod.seek(puntProd, 0)
				pickle.dump(Prod, alprod)
				alprod.flush()
				print()
				print("Producto eliminado con éxito...")
			else:
				print()
				print("Operación cancelada con éxito...")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("ELIMINAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")
			while codProd.isdigit()==False:
				print()
				print("Error. El dato ingresado no es un número. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar...")
				Borrar()
				print("ELIMINAR PRODUCTO")
				print()
				print()
				pantallaProd()
				print()
				codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")
			while buscarCodProd(codProd) == -1 and codProd != "0":
				print()
				print("El código del producto ingresado no se encuentra registrado. Inténtelo nuevamente...")
				print()
				input("Presione [Enter] para continuar...")
				Borrar()
				print("ELIMINAR PRODUCTO")
				print()
				print()
				pantallaProd()
				print()
				codProd = input("Ingrese el código del producto que desea eliminar (Ingrese [0] para volver al menú anterior): ")

#Módulo correspondiente al menú "Administración". Permite modificar las funciones asociadas a los productos con los que trabaja el comercio.
"""
tm = 50
print("","_".center(tm+2,"_"))
print("|","PRODUCTOS".center(tm),"|")
print("|".ljust(tm+2," "),"|")
print("|".ljust(tm+2,"-"),"|")
print("|".ljust(tm+2," "),"|")
print("|","  1- Agregar Producto".ljust(tm),"|")
print("|".ljust(tm+2," "),"|")
print("|","  2- Modificar Producto".ljust(tm),"|")
print("|".ljust(tm+2," "),"|")
print("|","  3- Eliminar Producto".ljust(tm),"|")
print()
"""

"""
	print("","_".center(tmprod+2,"_"))
	print("|","PRODUCTOS".center(tmprod),"|")
	print("|".rjust(tmprod+2,""),"|")
	print("|".ljust(tmprod+2,"-"),"|")
	print("|".rjust(tmprod+2,""),"|")
"""

def Productos():
	Borrar()
	print("PRODUCTOS")
	print()
	print()
	print("1- Agregar Producto")
	print()
	print("2- Modificar Producto")
	print()
	print("3- Eliminar Producto")
	print()
	print("0- Volver al menú anterior")
	print()
	opcion2()
	while op2 != 0:
		if op2 == 1:
			AgregProd()
		elif op2 == 2:
			ModifProd()
		else:
			ElimProd()
		Borrar()
		print("PRODUCTOS")
		print()
		print()
		print("1- Agregar Producto")
		print()
		print("2- Modificar Producto")
		print()
		print("3- Eliminar Producto")
		print()
		print("0- Volver al menú anterior")
		print()
		opcion2()

#-------------------------------------------------------------------------------------------------------------------------------------------------

#1er Módulo del menú principal del programa. Permite al usuario modificar los proveedores y productos asociados a su negocio.
def Admin():
	Borrar()
	print("ADMINISTRACIÓN")
	print()
	print("1- Proveedores")
	print()
	print("2- Productos")
	print()
	print("0- Volver al menú anterior")
	print()
	opcion()
	while op!=0:
		if op==1:
			Proveedores()
		else:
			Productos()
		Borrar()
		print("ADMINISTRACIÓN")
		print()
		print("1- Proveedores")
		print()
		print("2- Productos")
		print()
		print("0- Volver al menú anterior")
		print()
		opcion()

#-------------------------------------------------------------------------------------------------------------------------------------------------
  	
#1er Módulo del menú "Stock". Permite visualizar el registro de productos y su respectivo stock. Además, informa si es necesario reponer el stock al llegar a su cantidad mínima.
def VerStock():
	Borrar()
	print("VER STOCK")
	print()
	print()	
	a,b,c,d=Tamaño(tm)
	alprod.seek(0,0)
	print("|".ljust(tm," "),"|")
	print("|".ljust(tm,"-"),"|")
	print("|".ljust(tm," "),"|")
	print("|","Producto".center(a),"|","Precio".center(b),"|","Cantidad".center(c),"|")
	while os.path.getsize(afprod) > alprod.tell():
		prod = pickle.load(alprod)
		if prod.Estado == "True ":
			if int(prod.stock)<int(prod.cantMin):
				reponer =  str(int(prod.cantMax)-int(prod.stock))
			else:
				reponer = "NO"
			print("|",prod.nombre.strip().center(a),"|",prod.precio.strip('0').center(b),"|",prod.stock.strip('0').center(c),"|",reponer.center(d),"|")
	print("|","_".center(a,"_"),  "|","_".center(b,"_"),"|","_".center(c,"_"),"|","_".center(d,"_"),"|")
	print()
	print()
	input("Presione [Enter] para volver...")

#2do Módulo del menú "Stock". Permite incrementar el stock de los productos registrados en el sistema.
def AgregarStock():
	Borrar()
	print("AGREGAR STOCK")
	print()
	print()
	pantallaProd()
	print()
	codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")
	while codProd.isdigit()	== False:
		print()
		print("Error. No ingrese letras ni caracteres.")
		print()
		input('Presione [Enter] para continuar...')
		Borrar()
		print("AGREGAR STOCK")
		print()
		print()
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")
	while buscarCodProd(codProd) == -1 and codProd != "0":
		print()
		print("El código de producto ingresado no se encuentra registrado en el sistema. Inténtelo nuevamente.")
		print()
		input('Presione [Enter] para continuar...')
		Borrar()
		print("AGREGAR STOCK")
		print()
		print()
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")
	while codProd != "0":
		Borrar()
		print("AGREGAR STOCK")
		print()
		print()
		newStock = input("Ingrese la cantidad del producto que desea agregar al stock: ")
		while newStock.isdigit() == False:
			print()
			print("Error. No ingrese letras ni caracteres.")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("AGREGAR STOCK")
			print()
			print()
			newStock = input("Ingrese la cantidad del producto que desea agregar al stock: ")
		newStock = int(newStock)
		while newStock < 1:
			print()
			print("Error. Ingrese valores mayores que 0.")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("AGREGAR STOCK")
			print()
			print()
			newStock = int(input("Ingrese la cantidad del producto que desea agregar al stock: "))
		alprod.seek(puntProd, 0)
		Prod = pickle.load(alprod)
		Prod.stock = int(Prod.stock)
		Prod.stock += newStock
		Prod.stock = str(Prod.stock)
		Prod.stock = Prod.stock.rjust(4, "0")
		alprod.seek(puntProd, 0)
		pickle.dump(Prod, alprod)
		alprod.flush()
		print()
		print("Stock del producto [", Prod.nombre, "] incrementado con éxito. El total actual es: ", Prod.stock, ".")
		print()
		input('Presione [Enter] para continuar...')
		Borrar()
		print("AGREGAR STOCK")
		print()
		print()
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")
		while codProd.isdigit()	== False:
			print()
			print("Error. No ingrese letras ni caracteres.")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("AGREGAR STOCK")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")
		while buscarCodProd(codProd) == -1 and codProd != "0":
			print()
			print("El código de producto ingresado no se encuentra registrado en el sistema. Inténtelo nuevamente.")
			print()
			input('Presione [Enter] para continuar...')
			Borrar()
			print("AGREGAR STOCK")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto al que desea incrementarle el stock (Ingrese [0] para finalizar): ")

#2do Módulo del menú principa del programa. Permite al usuario modificar y visualizar el stock asociado a sus productos.
def Stock():
	Borrar()
	print("STOCK")
	print()
	print("1- Ver Lista de Stock")
	print()
	print("2- Agregar Stock")
	print()
	print("0- Volver al menú anterior")
	print()
	opcion()
	while op!=0:
		if op == 1:
			VerStock()
		else:
			AgregarStock()
		Borrar()
		print("STOCK")
		print()
		print("1- Ver Lista de Stock")
		print()
		print("2- Agregar Stock")
		print()
		print("0- Volver al menú anterior")
		print()
		opcion()

#-------------------------------------------------------------------------------------------

#Módulo del menú principal del programa.

def menuPrincipal():
	Borrar()
	print("Menú Principal")
	print()
	print()
	print("1- Administración")
	print()
	print("2- Stock")
	print()
	print("0- Finalizar el programa")
	print()
	opcion()
	while op!=0:
		if op == 1:
			Admin()
		elif op == 2:
			Stock()
		Borrar()
		print("Menú Principal")
		print()
		print()
		print("1- Administración")
		print()
		print("2- Stock")
		print()
		print("0- Finalizar el programa")
		print()
		opcion()
	Borrar()
	print("Sesión Finalizada")
	print()
	print("Developed by SBSolutions")

def programaPrincipal():
	CrearCarpeta(carpeta)
	abrir()
	menuPrincipal()
	cerrar()

programaPrincipal()