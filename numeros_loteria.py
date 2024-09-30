''' Manejo de errores
Introducir 5 números ganadores de la primitiva; los números deben ser enteros entre 1 y 49;
si el número no cumple con las condiciones, el programa muestra error correspondiente y pide introducir otro número
El programa muestra los números ganadores en orden. 
'''
num_ganador = []

while (len(num_ganador) != 5):
    try:  
        numero = input("---> Escribe un número ganador de la primitiva (entre 1 y 49): ")
        
        try: 
            numero = int(numero)

        except ValueError as e:
            try:
                float(numero) 
            except ValueError:
                raise ValueError("El valor debe ser un número.")
            raise ValueError("Los números no pueden ser decimales.")
            #numero = int(numero)

        if numero < 1 or numero > 49:
            raise ValueError("El número debe estar entre 1 y 49.")
        
        num_ganador.append(numero)
        num_ganador.sort()

    except ValueError as e:
        print(f"Error: {e}")

print(num_ganador) 