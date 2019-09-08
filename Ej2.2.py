def pedirNumeros():
    num1 = int(input("Ingrese el multiplicando: "))
    num2 = int(input("Ingrese el multiplicador: "))
    return num1, num2

def producto(num1,num2):
    aux=num2%1000
    centena=int(aux/100)
    print(centena,"c")
    aux=aux%100
    decena=int(aux/10)
    print(decena,"d")
    unidad=aux%10
    print(unidad,"u")
    a=int(num1*unidad)
    b=int(num1*decena)
    c=int(num1*centena)
    return a,b,c
       
def mostrar(num1,num2,a,b,c):
    print("")
    print("{0:>10}".format(num1))
    print("{0:<1}{1:>9}".format("x",num2))
    print("----------")
    print("{:>10}".format(a))
    print("{0:<1}{1:>8}{2:<1}".format("+",b,"-"))
    print("{0:>8}{1:>1}".format(c,"--"))
    print("----------")
    print("{0:>10}".format(a+(b*10)+(c*100)))
  
def main():
    a,b = pedirNumeros()
    c,d,e=producto(a,b)
    mostrar(a,b,c,d,e)
    
main()