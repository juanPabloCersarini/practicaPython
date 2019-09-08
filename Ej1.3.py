def pedirNum():
    n1 = int(input("Ingresar Número 1: "))
    n2 = int(input("Ingresar Número 2: "))
    return n1,n2

def sumar(n1,n2):
    suma = n1+n2
    return suma

def restar(n1,n2):
    resta = n1-n2
    return resta

def multiplicar(n1,n2):
    mult = n1*n2
    return mult

def dividir(n1,n2):
    div = n1/n2
    return div

def mostrarResultados(suma,resta,div,mult):
    print("La suma: ", suma)
    print("La resta: ", resta)
    print("La división: ", div)
    print("La multiplicación: ", mult)
    
def main():
    a,b=pedirNum()
    s=sumar(a,b)
    r=restar(a,b)
    d=dividir(a,b)
    m=multiplicar(a,b)
    print("Los resultados para ",a, " y " ,b, " son:")
    mostrarResultados(s,r,d,m)
    
main()