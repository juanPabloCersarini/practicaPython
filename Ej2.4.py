import random

def pedirDatos():
    inf = int(input("Ingrese el límite inferior (número natural): "))
    sup = int(input("Ingrese el límite superior (número natural): "))
    return inf,sup
              
def aleatorio(inf,sup):
    return random.randint(inf,sup)

def main():
    i,s = pedirDatos()
    num1 = aleatorio(i,s)
    print("")
    print("1 - Límite inferior",i,", límite superior",s,". Número generado:",num1)
    num2 = aleatorio(num1,s)
    print("2 - Límite inferior",num1,", límite superior",s,". Número generado:",num2)
    num3=aleatorio(num1,num2)
    print("3 - Límite inferior",num1,", límite superior",num2,". Número generado:",num3)
main()