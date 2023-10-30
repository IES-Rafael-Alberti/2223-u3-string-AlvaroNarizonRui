"""
Ejercicio 3.0.4¶
Hay un método de cadenas llamado count que es similar a find()
Escribe el código necesario para invocar al método count() y contar el número de veces que una letra aparece en “banana”.
"""
if __name__ == "__main__":
    palabra = "banana"
    #Entrada
    letra = input("Escribe una letra que buscar : ")
    #Procesamiento
    letras = palabra.count(letra)
    #Salida
    print(f"La letra {letra} aparece en la palabra {palabra} {letras} veces")