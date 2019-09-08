def ingresarNum():
    n1=int(input("Ingrese el primer número: "))
    n2=int(input("Ingrese el primer número: "))
    n3=int(input("Ingrese el primer número: "))
    return n1,n2,n3

def buscarMayMen(n1,n2,n3):
    if (n1>n2) and (n2>n3):
        mayor=n1
        menor=n3
        promedio = (mayor+menor)/2
        if (promedio == n2):
            res = True
        else:
            res = False
    if (n2>n1) and (n1>n3):
        mayor=n2
        menor=n3
        promedio = (mayor+menor)/2
        if (promedio == n1):
            res = True
        else:
            res = False
    if (n3>n1) and (n1>n2):
        mayor=n3
        menor=n2
        promedio = (mayor+menor)/2
        if (promedio == n1):
            res = True
        else:
            res = False
    if (n1>n2) and (n2<n3):
        mayor=n1
        menor=n2
        promedio = (mayor+menor)/2
        if (promedio == n3):
            res = True
        else:
            res = False
    if (n1<n2) and (n2<n3):
        mayor=n3
        menor=n1
        promedio = (mayor+menor)/2
        if (promedio == n2):
            res = True
        else:
            res = False
    if (n1<n2) and (n3<n2):
        mayor=n2
        menor=n1
        promedio = (mayor+menor)/2
        if (promedio == n3):
            res = True
        else:
            res = False
    if (n1==n2) or (n2==n3):
        res = False
    return res

def main():
    n1,n2,n3=ingresarNum()
    if (buscarMayMen(n1,n2,n3)):
        print("Están igualmente distanciados")
    else:
        print("No están igualmente distanciados")
    
main()
            