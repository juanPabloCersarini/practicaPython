def ingresarFecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    return dia,mes,anio

def esBisiesto(dia, mes, anio):
    if dia > 0 and dia <= 31:
        res = True
    if mes >= 0 or mes <= 12:
        res = True
    if (((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (dia > 30)):
        res = False
    if (mes==2) and ((dia==0) or (dia >29)):
        res = False
    else:
        if(((anio%4==0) and (anio%100!=0)) or (anio%400==0)):
            res = True
        else:
            res = False
    return res

def main():
    d,m,a=ingresarFecha()
    buleana = esBisiesto(d,m,a)
    if buleana == False:
        print("La fecha es incorrecta")
    else:
        print("La fecha es correcta")
    
main()