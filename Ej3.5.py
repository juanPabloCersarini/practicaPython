def datos():
    sueldo = float(input("Ingrese el sueldo Base: "))
    hijosBool = input("Tiene hijos (s/n)?: ")
    categ = input("Ingrese categoría (1 - 9): ")
    return sueldo, hijosBool, categ

def bono(sueldo):
    if sueldo > 2000:
        bono = sueldo * 0.20
    else:
        bono = sueldo * 0.15
    return bono

def hijos(hijosBool):
    if hijosBool == "s":
        tieneHijos = True
    else:
        tieneHijos = False
    return tieneHijos

def plusH(sueldo,tieneHijos):
    if tieneHijos:
        plusH=sueldo*0.05
    else:
        plusH=0
    return plusH

def plusC(sueldo,categ):
    if (categ<="3"):
        plusC=sueldo*0.10
    elif (categ>="4") and (categ<="6"):
        plusC=sueldo*0.12
    else:
        plusC=sueldo*0.20
    return plusC

def plus(sueldo,tieneH,cat):
    if (tieneH):
        plusHijos = plusH(sueldo,tieneH)
        plusCateg = plusC(sueldo,cat)
        if (cat<="6"):
            plus = plusHijos+plusCateg
        else:
            plus = plusCateg
    else:
        plus = plusC(sueldo,cat)
    return plus

def main():
    sueldo,h,categoria = datos()
    elBono = bono(sueldo)
    tieneHijos = hijos(h)
    elPlus = plus(sueldo,tieneHijos,categoria)
    aPagar = sueldo + elBono + elPlus
    print("")
    print("El sueldo total será de:", aPagar)

main()