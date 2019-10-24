def esLetra(letra):
    return (letra>="a" and letra<="z") or (letra>="A" and letra<="Z")

def palMasVoc(texto):
    i=0
    vocalesPal=0
    palBuscada=""
    while i<len(texto):
        #vocales=0
        pal=""
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        while i<len(texto) and esLetra(texto[i]):
            pal+=texto[i]
            i+=1
        i+=1   
        vocales=0
        for letra in pal:
             if letra=="a" or letra=="A":
                    vocales+=1
             elif letra=="e" or letra=="E":
                    vocales+=1
             elif letra=="i" or letra=="I":
                    vocales+=1
             elif letra=="o" or letra=="O":
                    vocales+=1
             elif letra=="u" or letra=="U":
                    vocales+=1
        if(vocales>vocalesPal):
             vocalesPal=vocales
             palBuscada=pal
    return palBuscada

def mostrarEnMayMin(palabra):
    minus=""
    may=""
    for letra in palabra:
        if letra>="A" and letra<="Z":
            minus+=chr(ord(letra)+32)
        elif letra>="a" and letra<="z":
            may+=chr(ord(letra)-32)
    print("En mayusculas: ",may)
    print("")
    print("En minúsculas: ",minus)
def main():
    texto= "La funcion del iframe es cargar INFORMACION que no se encuentra dentro de ese html sino en otro lugar, sin embargo pasa a mostrarla dentro del primero."
    palabra=palMasVoc(texto)
    mostrarEnMayMin(palabra)
    
main()