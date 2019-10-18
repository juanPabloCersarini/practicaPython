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
        
def buscarFrase2(fr1):
    i=-(len(fr1)-1)
    frase2=""
    while i<=0:
       frase2=frase2+fr1[i-1]
       i=i+1
    return frase2

def main():
    txt = "solo di sol a los idolos"
    fr1= buscarFrase1(txt)
    fr2 =buscarFrase2(fr1)
    if (fr1==fr2):
        print("SON IGUALES")
    else:
        print("NO APLICA")
    
main()
