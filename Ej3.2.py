def pedirNum():
    num= input("Ingrese un número: ")
    return num

def posNeg(num):
    if num=="0":
        res = "El número es cero y entero"
    else:
        if num > "0" :
            res = "El número es positivo y entero natural"
            if "." in num:
                res = "El número es positivo y real"
        else:
            if "." in num:
                res = "El número es negativo y real"
            else:
                res = "El número es es negativo y entero"
    return res

def main():
    num=pedirNum()
    print("")
    print(posNeg(num))
    
main()