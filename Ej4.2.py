def datos():
    inf = int(input("Ingrese Límite inferior: "))
    sup = int(input("Ingrese Límite superior: "))
    salto = int(input("Ingrese salto: "))
    return inf,sup,salto
    
def secuenciaConFor(inf,sup,salto):
    for x in range(inf,sup+1,salto):
        print(x)

def secuenciaConWhile(inf,sup,salto):
    while (inf<=sup):
        print(inf)
        inf=inf+salto
        
def main():
    inf,sup,salto=datos()
    secuenciaConFor(inf,sup,salto)
    print("///////////////////////////")
    secuenciaConWhile(inf,sup,salto)
    
main()