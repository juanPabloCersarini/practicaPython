def esLetra(x):
    return (x>="a" and x<="z") or (x>="A" and x<="Z")

def evaluar(texto):
    i=0
    largo=len(texto)
    cantPal=0
    palMin=largo
    palMax=0
    palabraCorta=""
    palabraLarga=""
    while i<largo:
        pal=""
        while i<largo and not esLetra(texto[i]):
            i+=1
        while i<largo and esLetra(texto[i]):
            pal=pal+texto[i]
            i+=1      
        i+=1
        if len(pal)<palMin:
            palabraCorta=pal
            palMin=len(palabraCorta)
        if len(pal)>palMax:
            palabraLarga=pal
            palMax=len(palabraLarga)
        cantPal+=1
    print("Cantidad de palabras: ",cantPal, "\nLa mas corta: ",palabraCorta, "\nLa mas larga: ",palabraLarga)
def main():
    texto=input("Ingresar un texto: ")
    evaluar(texto)
    
main()
    