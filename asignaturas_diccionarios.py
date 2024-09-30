#Crear un diccionario con asignatiras; el usuario introduce las notas; el programa muestra la asignatura que hay que repetir

asignaturas = {"Matemáticas": None, "Física": None, "Química": None, "Historia": None, "Lengua": None}

for clave, valor in asignaturas.items():
    valor=int(input(f"Introduce la nota para : {clave}: ")) #como al principio es un None, hay que invertirlo al int
    asignaturas[clave]=valor #guardar esto en el diccionario; llegar al valor con corchetes

for clave, valor in asignaturas.items(): 
    es_aprobada = valor>=5

    if not es_aprobada:
        print(f"Tienes que repetir: {clave}")

