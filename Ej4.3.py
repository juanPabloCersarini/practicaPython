def datos():
    inf = int(input("Ingrese Límite inferior: "))
    sup = int(input("Ingrese Límite superior: "))
    salto = int(input("Ingrese salto: "))
    paridad = int(input("Ingrese paridad -> '0 (par), 1 (Impar), 2 (ambos)': "))
    return inf,sup,salto,paridad
    
def secuencia(inf,sup,salto,paridad):
    for x in range(inf,sup+1,salto):
        if (paridad ==0):
            if (x%2==0):
                print(x)
        elif (paridad==1):
            if (x%2!=0):
                print(x)
        else:
            print(x)
       
def main():
    inf,sup,salto,paridad=datos()
    secuencia(inf,sup,salto,paridad)
    
main()