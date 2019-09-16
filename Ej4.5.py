def pedirNum():
    numero = int(input("ingrese cantidad -> "))
    return numero

def esPrimo(num):
    if ((2** (num - 1)) % num) == 1 or num == 2:
        resultado = True
    else:
        resultado = False
    return resultado

def primerosPrimos(nro):
    cantCol=1
    colNecesarias=10
    for x in range(1,nro):
        if esPrimo(x):
            if cantCol == colNecesarias:
                print("{:>6}".format(x),end="\n")
                cantCol=1
            else:
                print("{:>6}".format(x),end="")
                cantCol+=1
    print("")

def primerosNPrimos(nro):
    cantCol=1
    colNecesarias=10
    posiblePrimos=1
    cantPrimos=0
    while cantPrimos < nro:
        if esPrimo(posiblePrimos):
            cantPrimos+=1
            if cantCol == colNecesarias:
                print("{:>6}".format(posiblePrimos),end="\n")
                cantCol=1
            else:
                print("{:>6}".format(posiblePrimos),end="")
                cantCol+=1
        posiblePrimos+=1
            

def main():
    n = pedirNum()
    print("\nPrimos entre 1 y",n,"\n")
    primerosPrimos(n)
    print("\nLos primeros",n,"primos\n")
    primerosNPrimos(n)

main()