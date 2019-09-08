def pedirLados():
    lado1 = int(input("Ingresar Lado 1: "))
    lado2 = int(input("Ingresar Lado 2: "))
    return lado1,lado2

def calcularArea(lado1, lado2):
    area = lado1*lado2
    return area

def calcularPerimetro(lado1, lado2):
    perimetro = (lado1*2) + (lado2*2)
    return perimetro

def mostrarDatos(a,b):
    print("Area: ", a)
    print("Perímetro: ", b)

def main():
    a,b = pedirLados()
    area=calcularArea(a,b)
    perim=calcularPerimetro(a,b)
    mostrarDatos(area,perim)
    
main()