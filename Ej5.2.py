def esLetra(x):
    return (x>="a" and x<="z") or (x>="A" and x<="Z")

def buscarFrase1(txt):
    i=0
    
    frase1=""
    frase2=""
    while i <len(txt):
        pal=""
        while i<len(txt) and not esLetra(txt[i]):
            i+=1
        while i<len(txt) and esLetra(txt[i]):
            pal=pal+txt[i]
            i+=1      
        i+=1
        frase1=frase1+pal
    return frase1  

def convMayAMin(frase1):
    fraseMin=""
    for letra in frase1:
        if (letra>="a") and (letra<="z"):
            fraseMin = fraseMin +chr(ord(letra)-32)
        else:
            fraseMin = fraseMin+letra
    return fraseMin
def buscarFrase2(fr1):
    frase2=fr1[::-1]
    return frase2

def main():
    txt = "Solo di sol a LOS idolos"
    fr1= buscarFrase1(convMayAMin(txt))
    print(fr1)
    print("")
    
    fr2 =buscarFrase2(fr1)
    print(fr2)
    if (fr1==fr2):
        print("SON IGUALES")
    else:
        print("NO APLICA")
    
main()
