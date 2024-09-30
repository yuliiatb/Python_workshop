#calculadora

operacion = 0
while (operacion !=5):
     
    operacion = input("\nElige una opción. Pulsa el número de la operación:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\n")
    if operacion == "5":
        print(f"---Salimos del programa---")
        break

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if operacion == "1":
        print(f" {num1} + {num2} = {num1+num2}")
        #break
    if operacion == "2":
        print(f" {num1} - {num2} = {num1-num2}")
        #break
    if operacion == "3":
        print(f" {num1} * {num2} = {num1*num2}")
        #break
    if operacion == "4":
        try:
            num1/num2
            print(f" {num1} / {num2} = {num1/num2}")
        except ZeroDivisionError:
            print("¡No se puede dividir entre cero!")
                   
    