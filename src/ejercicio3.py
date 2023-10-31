"""
Ejercicio 3.0.3¶
Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""
def cuenta(cadena,letra) -> int:
    contador = 0
    for i in cadena:
        if i == letra:
            contador += 1
    return contador

if __name__ == "__main__":
    #Entrada
    cadena = input("Escribe una palabra o cadena: ")
    letra = input("Escribe una letra que buscar : ")
    #Procesamiento
    contador = cuenta(cadena,letra)
    #Salida
    print(f"La letra {letra} aparece en la palabra {cadena} {contador} veces")