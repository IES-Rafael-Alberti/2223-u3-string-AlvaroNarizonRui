"""
Ejercicio 3.0.1¶
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás 
hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
"""
def reverso(cadena) -> str:
    contenedor_letras = ""
    contador = len(cadena)-1
    while contador >= 0:
        contenedor_letras += cadena[contador] + "\n"
        contador -= 1
    return contenedor_letras

if __name__ == "__main__":
    #Entrada
    cadena = input("Ingresa una cadena : ")
    #Procesamiento
    cadena_reversa = reverso(cadena)
    #Salida
    print(f"La cadena que introdujiste : {cadena} \n Resultado: \n{cadena_reversa}")
