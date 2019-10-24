def esLetra(letra):
    return (letra>="a" and letra<="z") or (letra>="A" and letra<="Z")

def contarPalabras(texto):
    i=0
    cantLetra=0
    cantPal=0
    while i<len(texto):
        
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        while i<len(texto) and esLetra(texto[i]):
            i+=1
            cantLetra+=1
        cantPal+=1
        i+=1
    print("Palabras: ",cantPal)
    print("Letras: ",cantLetra)

def contarVocalesYCons(texto):
    vocales=0
    cons=0
    i=0
    soloLetras=""
    while i<len(texto):
        while i<len(texto) and not esLetra(texto[i]):
            i+=1
        while i<len(texto) and esLetra(texto[i]):
            soloLetras+=texto[i]
            i+=1
        i+=1
    for letra in soloLetras:
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
             else:
                 cons+=1
    print("Vocales:", vocales)
    print("Consonantes:",cons)

def main():
    texto="Aunque no lo veamos el sol siempre esta"
    contarPalabras(texto)
    contarVocalesYCons(texto)
    
    
main()