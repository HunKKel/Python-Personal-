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
#Funcion borrar adaptada para SO linux, windows y apple
def Borrar():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

#Módulo con el que establecemos las rutas de guardado de los archivos a utilizar y abrimos los archivos lógicos asociados.

def abrir():
	global afprod, alprod, afprov, alprov
	afprod = "SBS_Software\Productos.dat"
	if os.path.exists(afprod)==True:
		alprod = open(afprod, "r+b")
	else:
		alprod = open(afprod, "w+b")
	afprov = "SBS_Software\Proveedores.dat"
	if os.path.exists(afprov)==True:
		alprov = open(afprov, "r+b")
	else:
		alprov = open(afprov, "w+b")

carpeta = "SBS_Software"
def CrearCarpeta(carpeta):
	if not os.path.exists(carpeta):
		os.makedirs(carpeta)
	
#Busquedas
def BusquedaNombreProveedor(nom):
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
def BuscarCodProveedor(cod):
	prov = PROVEEDOR()
	pos = 0
	alprov.seek(0,0)
	prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and prov.cod != cod:
		pos = pos + 1
		prov = pickle.load(alprov)
	if prov.cod != cod:
		pos = -1
	return pos


def CargaProveedor(prov):
	#el puntero ya esta acomodado (al entrar a la funcion)
	#realizar validaciones 
	#codigo y nombre se cargan afuera de la funcion
	prov.mail = input("ingrese el mail del proveedor:").ljust(40)
	prov.telefono = input("ingrese el telefono del proveedor:").rjust(14, ' ')
	prov.ciudad = input("ingrese la ciudad del proveedor:").ljust(20)
	prov.calle = input("ingrese la calle del proveedor:").ljust(20)
	prov.numCalle = input("ingrese la altura:").rjust(4, '0')
def ModProveedor(prov):
	print("Antiguo nombre del proveedor: ", prov.nombre)
	aux = input("ingrese el nuevo nombre del proveedor:").ljust(12)
	if BusquedaNombreProveedor(aux) != -1:
		Borrar()
		print("El proveedor ", aux.strip()," ya existe")
	else:
		prov.nombre = aux
	print("Antiguo mail del proveedor: ", prov.mail)
	aux = input("ingrese el nuevo mail del proveedor:").ljust(40)
	#validacion
	if aux == aux:
		prov.mail = aux
	else:
		print()
	print("Antiguo telefono del proveedor: ", prov.telefono)
	aux = input("ingrese el telefono del proveedor:").rjust(14, ' ')
	if aux == aux:
		prov.telefono = aux
	else:
		print()
	print("Antigua ciudad del proveedor: ", prov.ciudad)
	aux = input("ingrese la ciudad del proveedor:").ljust(20)
	if aux == aux:
		prov.ciudad = aux
	else:
		print()
	print("Antigua calle del proveedor: ", prov.calle)
	prov.calle = input("ingrese la calle del proveedor:").ljust(20)
	if aux == aux:
		prov.calle = aux
	else:
		print()
	print("Antigua altura del proveedor: ", prov.numCalle)
	aux = input("ingrese la altura:").rjust(4, '0')
	if aux == aux:
		prov.numCalle = aux
	else:
		print()
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
				prov.cod = str(os.path.getsize(afprov)//tmprov + 2).rjust(8, '0')
				pickle.dump(prov,alprov)
				alprov.flush()
				Borrar()
				print("Proveedor agregado exitosamente.")
		else:
			prov.nombre = aux.ljust(12)
			CargaProveedor(prov)
			prov.cod = "1".rjust(8, '0')
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
			print("|",prov.cod.center(8," "),"|",prov.nombre.strip().center(15," "),"|",prov.mail.strip().center(42," "),"|",prov.telefono.center(12," "),"|")
		print("|".ljust(90,"_"),"|")
#2do Módulo del menú "Proveedores". Permite al usuario modificar datos de los proveedores registrados en el sistema.
def ModifProv():
	if os.path.getsize(afprov) > 0:
		seguir = " "
		while seguir != "N":
			Borrar()
			print("","_".ljust(90,"_"))
			print("|".ljust(90," "),"|")
			print("|","MODIFICAR PROVEEDORES".center(88),"|")
			VerProv()
			cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(8,'0')
			cont = 1
			seguir = " "
			while BuscarCodProveedor(cod) == -1 and seguir != "N":
				Borrar()
				print("","_".ljust(90,"_"))
				print("|".ljust(90," "),"|")
				print("|","MODIFICAR PROVEEDORES".center(88),"|")
				VerProv()
				print("| No existe ningun proveedor con el codigo ingresado".ljust(88),"|")
				cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(8,'0')
				cont = cont + 1 
				if cont >= 4:
					Borrar()
					print("","_".ljust(90,"_"))
					print("|".ljust(90," "),"|")
					print("|","MODIFICAR PROVEEDORES".center(88),"|")
					VerProv()
					print("  Ha ingresado un sódigo inexistente demasiadas veces")
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
						cod = input("| Ingrese el código del proveedor que desea modificar: ").rjust(8,'0')
			if seguir != "N":
				alprov.seek(tmprov*(int(cod.strip())-1))
				prov = pickle.load(alprov)
				ModProveedor(prov)
				alprov.seek(tmprov*(int(cod.strip())-1))
				pickle.dump(prov,alprov)
				Borrar()
				print("","_".ljust(90,"_"))
				print("|".ljust(90," "),"|")
				print("|","MODIFICAR PROVEEDORES".center(88),"|")
				VerProv()
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
	while op1 != 0:
		if op1 == 1:
			Borrar()
			AgregProv()
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
			print(x)
			print(Prod.nombre)
			puntProd = alprod.tell()
			Prod = pickle.load(alprod)
		if x == Prod.nombre:
			return puntProd
		else:
			return -1

#Módulo en el que se ingresa y valida el precio de un producto. Utilizado en la función "Agregar Producto" del menú "Productos".

def ingresaPrecioProducto():
	global precio
	precio = input("Ingrese el precio del producto a registrar (en pesos [ARS]): ")
	while precio.isdigit()==False:
		print()
		print("Error. Ingrese valores numéricos. Inténtelo nuevamente.")
		print()
		input("Presione [Enter] para continuar...")
		Borrar()
		precio = input("Ingrese el precio del producto a registrar (en pesos [ARS]): ")
	precio = int(precio)
	while precio<=0:
		print()
		print("Error. Ingrese valores mayores que 0.")
		print()
		input("Presione [Enter] para continuar...")
		Borrar()
		precio = int(input("Ingrese el precio del producto a registrar (en pesos [ARS]): "))

#Módulo de búsqueda del código del proveedor en el archivo "ProveedoresARCHIVO.dat"
def buscarCodProv(x):
	global puntProv
	alprov.seek(0,0)
	puntProv = alprov.tell()
	Prov = pickle.load(alprov)
	while os.path.getsize(afprov) > alprov.tell() and (x != Prov.cod):
		puntProv = alprov.tell()
		Prov = pickle.load(alprov)
	if x == Prov.cod:
		return puntProv
	else:
		return -1

#Módulo en el que se elige el proveedor del que se obtuvo el producto a registrar. Luego, se obtiene el código del proveedor.
def ingresaCodigoProveedor():
	global codProv
	Borrar()
	alprov.seek(0,0)
	while os.path.getsize(afprov) > alprov.tell():
		Prov = pickle.load(alprov)
		print()
		print("Código de Proveedor: ", Prov.cod)
		print("Nombre del Proveedor: ", Prov.nombre)
		print()
	print()
	codProv = input("Ingrese el código del proveedor del producto a registrar: ")
	while buscarCodProv(codProv) == -1:
		print()
		print("El código ingresado no corresponde a un proveedor registrado. Inténtelo nuevamente...")
		print()
		input("Presione [Enter] para continuar...")
		Borrar()
		alprov.seek(0,0)
		while os.path.getsize(afprov) > alprov.tell():
			Prov = pickle.load(alprov)
			print()
			print("Código de Proveedor: ", Prov.cod)
			print("Nombre del Proveedor: ", Prov.nombre)
			print()
		print()
		codProv = input("Ingrese el código del proveedor del producto a registrar: ")
	
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
					codProd = 1
				#Si ya hay 1 o más productos registrados, el sistema otorgará como código el número que le sigue al último producto del registro
				else:
					alprod.seek(0,0)
					Prod = pickle.load(alprod)
					tamRegProd = alprod.tell()
					cantRegProd = (os.path.getsize(afprod))//(tamRegProd)
					puntUltimoProducto = ((cantRegProd)-1)*tamRegProd
					alprod.seek(puntUltimoProducto, 0)
					Prod = pickle.load(alprod)
					Prod.cod = int(Prod.cod)
					codProd = Prod.cod + 1
				ingresaPrecioProducto()
				ingresaCodigoProveedor()
				alprod.seek(0,2)
				Prod.cod = codProd
				Prod.nombre = nomProd
				Prod.precio = precio
				Prod.codProveedor = codProv
				pickle.dump(Prod, alprod)
				alprod.flush()
				print()
				print("Producto registrado con éxito...")
			#En este caso, el producto ya se encuentra registrado. En consecuencia, muestra una advertencia al usuario.
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
 
#Módulo que muestra el conjunto de productos registrados en el sistema.
def pantallaProd():
	alprod.seek(0,0)
	while os.path.getsize(afprod) > alprod.tell():
		Prod = pickle.load(alprod)
		print()
		print("Código del Producto: ", Prod.cod)
		print("Nombre del Producto: ", Prod.nombre)
		print("Proveedor del Producto: ", nombreProv(Prod.codProveedor))
		print()

#Módulo de búsqueda del código de un producto en el archivo "ProductosARCHIVO.dat".
def buscarCodProd(x):
	global puntProd
	alprod.seek(0,0)
	puntProd = alprod.tell()
	Prod = pickle.load(alprod)
	while os.path.getsize(afprod) > alprod.tell() and (x != Prod.cod):
		puntProd = alprod.tell()
		Prod = pickle.load(alprod)
	if x == Prod.cod:
		return puntProd
	else:
		return -1

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

#Módulo que muestra el conjunto de proveedores registrados en el sistema.
def pantallaProv():
	alprov.seek(0,0)
	while os.path.getsize(afprov) > alprov.tell():
		Prov = pickle.load(alprov)
		print()
		print("Código del Proveedor: ", Prov.cod)
		print("Nombre del Proveedor: ", Prov.nombre)
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
		if buscarCodProv(newProv) != -1:
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

#2do Módulo del menú "Productos". Permite modificar los productos registrados en el sistema.
def ModifProd():
	Borrar()
	print("MODIFICAR PRODUCTO")
	print()
	print()
	if os.path.getsize(afprod) == 0:
		print("No se encontraron productos registrados en el sistema. Para utilizar esta función, registre al menos un producto con la opción [Agregar Producto].")
		print()
		input("Presione [Enter] para continuar...")
	else:
		pantallaProd()
		print()
		codProd = input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): ")
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
			codProd = input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): ")
		codProd = int(codProd)
		while buscarCodProd(codProd) == -1 and codProd != 0:
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
			codProd = int(input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): "))
		while codProd != 0:
			alprod.seek(puntProd,0)
			Prod = pickle.load(alprod)
			Borrar()
			print("MODIFICAR PRODUCTO")
			print("[", Prod.nombre, "]")
			print()
			print()
			print("1- Nombre del Producto")
			print()
			print("2- Proveedor del Produco")
			print()
			print("0- Volver al menú anterior")
			print()
			opcion()
			while op != 0:
				if op == 1:
					modifNomProd(Prod)
				else:
					modifProvProd(Prod)
				Borrar()
				print("MODIFICAR PRODUCTO")
				print("[", Prod.nombre, "]")
				print()
				print()
				print("1- Nombre del Producto")
				print()
				print("2- Proveedor del Produco")
				print()
				print("0- Volver al menú anterior")
				print()
				opcion()
			Borrar()
			print("MODIFICAR PRODUCTO")
			print()
			print()
			pantallaProd()
			print()
			codProd = input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): ")
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
				codProd = input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): ")
			codProd = int(codProd)
			while buscarCodProd(codProd) == -1 and codProd != 0:
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
				codProd = int(input("Ingrese el código del producto que desea modificar (Ingrese 0 para volver al menú anterior): "))

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

#Módulo con el que cierro los archivos lógicos utilizados a lo largo del programa.
def cerrar():
	alprov.close()
	alprod.close()

def programaPrincipal():
	CrearCarpeta(carpeta)
	abrir()
	menuPrincipal()
	cerrar()

programaPrincipal()