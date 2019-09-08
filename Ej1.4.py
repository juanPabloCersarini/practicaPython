def pedirNumero():
    num=float(input("Ingrese Número: "))
    return num

def descomponerNum(num):
    numero=num
    parteEntera = int(num)
    parteDecimal = "{0:.4f}".format(num-parteEntera)
    return numero, parteEntera,parteDecimal

def mostrarResultados(n,e,d):
    print("Los resultados para", n ," son:")
    print("Parte entera: ",e)
    print("Parte decimal: ",d)
    
def main():
    N= pedirNumero()
    n,e,d=descomponerNum(N)
    mostrarResultados(n,e,d)
    
main()