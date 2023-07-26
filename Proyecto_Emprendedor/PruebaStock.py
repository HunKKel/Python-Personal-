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
#print ("|"," B - STOCK".ljust(tm),"|")
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
		self.cod = "0".rjust(8,'0')
		self.nombre = "".ljust(12)
		self.precio = "0".rjust(8,'0')
		self.codProveedor = "".ljust(12)
		self.stock = "0".rjust(8,'0')
		self.cantMax = "0".rjust(8,'0')
		self.cantMin = "0".rjust(8,'0')

class PROVEEDOR:
	def __init__(self):
		self.cod = "0".rjust(8,'0')
		self.nombre = "".ljust(12)
		self.mail = "".ljust(40)
		self.telefono = "0".rjust(14, ' ')
		self.ciudad = "".ljust(20)
		self.calle = "".ljust(20)
		self.numCalle = "0".rjust(4, '0')

afprov = "ProveedoresARCHIVO.dat"
afprod = "ProductosARCHIVO.dat"

tmprov = 254
tmprod = 196	

#Funcion borrar adaptada para SO linux, windows y aple
def Borrar():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

#Módulo con el que establecemos las rutas de guardado de los archivos a utilizar y abrimos los archivos lógicos asociados.

def abrir():
	global afprod, alprod, afprov, alprov
	afprod = "Productos.dat"
	if os.path.exists(afprod)==True:
		alprod = open(afprod, "r+b")
	else:
		alprod = open(afprod, "w+b")
	afprov = "Proveedores.dat"
	if os.path.exists(afprov)==True:
		alprov = open(afprov, "r+b")
	else:
		alprov = open(afprov, "w+b")

carpeta = "SBS_Software"
def CrearCarpeta(carpeta):
	if not os.path.exists(carpeta):
		os.makedirs(carpeta)
	
#Busquedas
def busquedaNombreProveedor(nom):
	prov = PROVEEDOR()
	pos = 0
	alprov.seek(0,0)
	prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and prov.nombre != nom:
		pos = pos + 1
		prov = pickle.load(alprov)
	if prov.nombre != nom:
		pos = -1
	return pos

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

#1er Módulo del menú "Proveedores". Permite registrar proveedores en el sistema.
def AgregProv():
	Borrar()
	prov = PROVEEDOR()
	opA = ""
	while opA != "N":
		aux = input("ingrese el nombre del proveedor:").ljust(12)
		if os.path.getsize(afprov)>0:
			if busquedaNombreProveedor(aux) != -1:
				Borrar()
				print("El proveedor ", aux.strip()," ya existe")
			else:
				prov.nombre = aux.ljust(12)
				#hacer validaciones
				prov.mail = input("ingrese el mail del proveedor:").ljust(40)
				prov.telefono = input("ingrese el telefono del proveedor:").rjust(14, ' ')
				prov.ciudad = input("ingrese la ciudad del proveedor:").ljust(20)
				prov.calle = input("ingrese la calle del proveedor:").ljust(20)
				prov.numCalle = input("ingrese la altura:").rjust(4, '0')
				prov.cod = str(os.path.getsize(afprov)//tmprov + 2).rjust(8, '0')
				pickle.dump(prov,alprov)
				alprov.flush()
				Borrar()
				print("Proveedor agregado exitosamente.")
		else:
			#hacer validaciones
			prov.nombre = aux.ljust(12)
			#hacer validaciones
			prov.mail = input("ingrese el mail del proveedor:").ljust(40)
			prov.telefono = input("ingrese el telefono del proveedor:").rjust(14, ' ')
			prov.ciudad = input("ingrese la ciudad del proveedor:").ljust(20)
			prov.calle = input("ingrese la calle del proveedor:").ljust(20)
			prov.numCalle = input("ingrese la altura:").rjust(4, '0')
			prov.cod = "1".rjust(8, '0')
			pickle.dump(prov,alprov)
			alprov.flush()
			Borrar()
			print("Proveedor agregado exitosamente.")
		opA = input("desea agregar otro proveedor? (S/N): ").upper()
		while opA!= "S" and opA!= "N":
			Borrar()
			opA = input("desea agregar otro proveedor? (S/N): ").upper()

#2do Módulo del menú "Proveedores". Permite al usuario modificar datos de los proveedores registrados en el sistema.
def ModifProv():
	print()
#3er Módulo del menú "Proveedores". Visualiza los proveedores registrados en el sistema junto con sus datos.
def VerProv():
	Borrar()
	if os.path.getsize(afprov) == 0:
		print("no hay proveedores cargados")
	else:	
		print("","_".ljust(90,"_"))
		print("|".ljust(90," "),"|")
		print("|","Proveedores registrados".center(88),"|")
		print("|".ljust(90," "),"|")
		print("|".ljust(90,"-"),"|")
		print("|  Código  |       Nombre    |                    Mail                    |    Teléfono    |")
		alprov.seek(0)
		while os.path.getsize(afprov) > alprov.tell():
			prov = pickle.load(alprov)
			print("|",prov.cod.center(8," "),"|",prov.nombre.strip().center(15," "),"|",prov.mail.strip().center(42," "),"|",prov.telefono.center(12," "),"|")
		print()
		print()
		input("Presione [Enter] para continuar...")


#4to Módulo del menú "Proveedores". Permite eliminar proveedores del sistema. Estos pueden ser recuperados a través de la opción "Agregar Proveedor" del menú "Proveedores".
def ElimProv():
	print()
	

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
	while op1!=0:
		if op1 == 1:
			AgregProv()
		elif op1 == 2:
			ModifProv()
		elif op1 == 3:
			VerProv()
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

#1er Módulo del menú "Productos". Permite registrar nuevos productos en el sistema. 
def AgregProd():
	print()

#2do Módulo del menú "Productos". Permite modificar los productos registrados en el sistema.
def ModifProd():
	print()

#3er Módulo del menú "Productos". Elimina los productos indicados por el usuario. Pueden ser recuperados haciendo uso de la opción "Agregar Producto" del menú "Productos".
def ElimProd():
	print()

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

def Productos():
	Borrar()
	print("","_".center(tm+2,"_"))
	print("|","PRODUCTOS".center(tm),"|")
	print("|".rjust(tm+2,""),"|")
	print("|".ljust(tm+2,"-"),"|")
	print("|".rjust(tm+2,""),"|")
	print("1- Agregar Producto")
	print()
	print("2- Modificar Producto")
	print()
	print("3- Eliminar Producto")
	print()
	print("0- Volver al menú anterior")
	print()
	opcion2()
	while op2!=0:
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
	print()

#2do Módulo del menú "Stock". Permite incrementar el stock de los productos registrados en el sistema.
def AgregarStock():
	print()

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

#Módulo y menú principal del programa.

def menuPrincipal():
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

#Módulo con el que cierro los archivos lógicos utilizados a lo largo del programa.
def cerrar():
	alprov.close()
	alprod.close()

def programaPrincipal():
	abrir()
	menuPrincipal()
	cerrar()

programaPrincipal()