def pedirNumero():
    num=int(input("Ingrese Número: "))
    return num

def convertir(num):
    diaEnSeg = 24*60*60
    hsEnSeg = 60*60
    dias = int(num/diaEnSeg)
    calculoH = num%diaEnSeg
    horas = int(calculoH/hsEnSeg)
    calculoM = calculoH%hsEnSeg
    minutos =int(calculoM/60)
    segundos = calculoM%60
    print(dias,"dia(s),",horas, "hora(s),",minutos,"minuto(s),",segundos,"segundo(s)")
    
def main():
    numero=pedirNumero()
    convertir(numero)

main()
