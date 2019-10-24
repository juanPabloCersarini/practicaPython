def minYmay(txt):
    palNueva=""
    for x in txt:
        if x>="a" and x<="z":
            palNueva+=chr(ord(x)-32)
        elif x>="A" and x<="Z":
            palNueva+=chr(ord(x)+32)
    print(palNueva)
    
def cantVocales(txt):
    vocales=0
    for x in txt:
        if x=="a" or x=="A":
            vocales+=1
        elif x=="e" or x=="E":
            vocales+=1
        elif x=="i" or x=="I":
            vocales+=1
        elif x=="o" or x=="O":
            vocales+=1
        elif x=="u" or x=="U":
            vocales+=1
    print(vocales)
    
def main():
    palabra = "MurCIElagO"
    minYmay(palabra)
    cantVocales(palabra)

main()