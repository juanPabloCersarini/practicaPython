def limiteInferior():
    inf = int(input("Ingrese Límite inferior: "))  
    return inf

def limiteSuperior():
    sup = int(input("Ingrese Límite superior: "))
    return sup

def salto():
    salto = int(input("Ingrese salto: "))
    return salto

def paridad():
    paridad = int(input("Ingrese paridad -> '0 (par), 1 (Impar), 2 (ambos)': "))
    return paridad

def validar(inf,sup,valor):
    if (valor>inf and valor<=sup):
        datoCorrecto = True
    else:
        datoCorrecto = False
    return datoCorrecto
        
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
    inf=limiteInferior()
    correcto=validar(0,100,inf)
    while not correcto:
        inf = int(input("Error, ingrese valor (1 - 100): "))
        correcto=validar(0,100,inf)
    sup = limiteSuperior()
    correcto=validar(0,100,sup)
    while not correcto:
        sup = int(input("Error, ingrese valor (1 - 100): "))
        correcto=validar(0,100,sup)
    elSalto = salto()
    par = paridad()
    correcto = validar(-1,3,par)
    while not correcto:
        par = int(input("Error, ingrese valor (0 - 3): "))
        correcto=validar(-1,3,par)
    secuencia(inf,sup,elSalto,par)
    
main()