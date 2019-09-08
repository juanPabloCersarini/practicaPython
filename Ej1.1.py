def pedirNumero():
    num=int(input("Ingrese Número: "))
    return num

def mostrarDato(num):
    print("Usted ingresó: ", num)
    
def main():
    num=pedirNumero()
    mostrarDato(num)
    
main()