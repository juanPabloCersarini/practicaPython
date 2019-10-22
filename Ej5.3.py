def aMin(cad):
    cadMin=""
    for letra in cad:
        if letra>="A" and letra<="Z":
            cadMin += chr(ord(letra)+32)
        else:
            cadMin += letra
    return cadMin

def contarCorto(largo,corto):
    lenLargo=len(largo)
    acumCorto=0
    i=0
    while i <lenLargo:
        if largo[i:i+len(corto)]==corto:
            acumCorto+=1
            i+=len(corto)
        else:
            i+=1
    print(corto , "se encuentra ", acumCorto, " veces")
def main():
    txtLargo= "Hola Manola cuantas olas"
    txtLargo2=aMin(txtLargo)
    txtCorto="ola"
    txtCorto2=aMin(txtCorto)
    contarCorto(txtLargo2,txtCorto2)
    
main()