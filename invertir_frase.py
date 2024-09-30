frase = input("Introduce una frase: ")
def invertir(frase):
    mi_frase = frase.upper()
    frase_invertida = mi_frase[::-1] #sobrecarga - porque reversed se utiliza con objetos, no con strings
    return frase_invertida

print(invertir(frase))