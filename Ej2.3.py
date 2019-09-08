
def pedirLado():
    ladoCuadrado = int(input("Ingrese el lado: "))
    return ladoCuadrado

def areaCirc(radio):
    areaCirculo = 3.14 * (radio*radio)
    return areaCirculo

def areaCuad (lado):
    areaCuadrado = lado*lado
    return areaCuadrado

def areaNegra(ladoCuadrado):
    areaCuadrado=areaCuad(ladoCuadrado)
    radioGde = ((ladoCuadrado/3)*2)/2
    radioChico = (ladoCuadrado/3)/2
    circuloGde = areaCirc(radioGde)
    circuloChico = areaCirc(radioChico)
    areaNegra= areaCuadrado - circuloGde - (circuloChico*2)
    porcentajeArea = (areaNegra*100)/areaCuadrado
    print("El area negra es {0:.2f}".format(areaNegra),"y es un " "{0:.2f}{1:<1}".format(porcentajeArea,"%"),"del área total del cuadrado")

def main():
    lado=pedirLado()
    areaNegra(lado)
    
main()
