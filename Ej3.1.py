def pedirDatos():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese e,segundo número: "))
    signo = input("Ingrese la operación (+,-,*,/,//,**): ")
    return num1,num2,signo

def operar(num1,num2,signo):
    if signo == "+":
        res = num1 + num2
    elif signo == "-":
        res = num1 - num2
    elif signo == "*":
        res = num1*num2
    elif signo == "/":
        res = num1/num2
    elif signo == "//":
        res = num1//num2
    elif signo == "**":
        res = num1**num2
    return res 

def mostrar(n1,n2,s,res):
    print(n1,s,n2,"=",res)
    
def main():
    n1,n2,s = pedirDatos()
    res=operar(n1,n2,s)
    mostrar(int(n1),int(n2),s,int(res))
          
main()