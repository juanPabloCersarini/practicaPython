def pedirNum():
    numero = int(input("ingrese nro a invertir -> "))
    return numero
                 
def invertirNum(numero):
    invertido = 0

    while numero > 0 :
        resto = numero % 10
        invertido = (invertido * 10) + resto
        numero = int(numero/10)
    return invertido

def esCapicua(numero):
    inv = invertirNum(numero)
    if (numero == inv):
        esCapi = True
    else:
        esCapi = False
    return esCapi

def main():
    n = pedirNum()
    capicua = esCapicua(n)
    if capicua:
        print("El número es capicúa")
    else:
        print("El número no es capicúa")

main()