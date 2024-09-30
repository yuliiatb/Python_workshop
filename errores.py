'''
num_ganador = []
contador = 5

#def num_positivo(num): #para evitar if-else
#    return num > 0

while (contador != 0):
    
    
    try:
        numero = int(input("Escribe un número ganador de la primitiva: "))
    except ValueError:
        numero = int(input("Debes introducir un número entero. Vuelve a introducirlo: "))
    finally:    
        #while not num_positivo(numero):
        #numero = int(input("Debes introducir un número positivo. Vuelve a introducirlo: "))
        num_ganador.append(numero)
        contador-=1

print(num_ganador)    


funciona, pero no se puede hacer dos errores in a row

num_ganador = []
contador = 5

while (contador != 0):
    
        try:
            numero = int(input("Escribe un número ganador de la primitiva: "))
        except ValueError:
            numero = int(input("Debes introducir un número entero. Vuelve a introducirlo: "))
        finally:    
            num_ganador.append(numero)
            contador-=1

print(num_ganador) 


#otra solucion

def numeros_loteria():
    numeros = []
    while len(numeros)<5:
        try:
            numero = int(input("intro num entre 1 y 49"))
        except ValueError:
            print("Error, vuelve a introducir el num")
    numeros.sort()
    return numeros
print(numeros_loteria())
'''

#otra solucion con varios mensajes
#funcion para captar errores
def leer_numeros(numero_usuario):
    
    try:
        numero=int(numero_usuario) #scope de la variable
        
    except ValueError as e:
        try:
            float(numero_usuario) #no hace falta asignar esto al numero
        except ValueError:
            raise ValueError("El valor no es un número")
        raise ValueError("Los números decimales no valen")
    
    if numero < 1 or numero > 49:
        raise ValueError("Los números tienen que ser enter 1 y 49.")
    
    return numero #si el numero no entra en el if, retorna el numero
        
def numeros_loteria():
    numeros = []
    while len(numeros)<5:
        try:
            numero = leer_numeros(input("Introduce un número entre 1 y 49: "))
            numeros.append(numero) #para que el número se añade a la lista si es correcto
        except ValueError as e:  #"llamar" el error y que se muestre un mensaje en concreto
            print(f"Error: {e}") #e - texto que se asigna en los raise
    
    numeros.sort() #para mostarlos en orden; no es necesario crear una nueva variable, solo llamar este metodo
    return numeros
print(numeros_loteria()) #para que muestre lo que hace la funcion: insertar los numeros y mostrar mensajes de error correctos