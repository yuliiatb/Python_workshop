''' Craer un archivo "fichero.txt" y escribir unas lineas.
El programa escribirá las lineas pares del archivo creado a un nuevo archivo e imprimirá las lineas impares
'''

file_object = open("fichero.txt", "r") 
lines = file_object.readlines()
for line in lines:
    print(lines)

another_file = open("lineas_pares.txt", "w") #no lo tenía antes, se crea durante la ejecucion
with open("lineas_pares.txt", mode="w") as another_file:
    #another_line = another_file.readlines() #no hace falta leer este archivo; al principio no existe
    
    #index - posicion de cada linea; line - cada línea
    #enumerate - método que enumera las lineas; evitar crear un índice y añadir/restar 1 para iterar las lineas
    #start - para que empiece la enumeración de 1, no de linea[0]
    for index, line in enumerate(lines, start=1): 
        
        if index%2==0:
            another_file.write(line) #pares - se escriben en otro archivo
        else:
            print(line) #impares - se muestran por pantalla
