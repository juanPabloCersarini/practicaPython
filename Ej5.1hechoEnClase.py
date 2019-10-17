def esLetra(x):
    return (x>="a" and x<="z") or (x>="A" and x<="Z")

def buscarPalabra(txt):
    i=0
    pri=""
    ult=""
    while i <len(txt):
        pal=""
        while i<len(txt) and not esLetra(txt[i]):
            i+=1
        while i<len(txt) and esLetra(txt[i]):
            pal=pal+txt[i]
            i+=1
        if pri=="":
            pri=pal
            ult=pal
        else:
            ult=pal
        i+=1
    return pri==ult    
        
def main():
    txt = "hola, que + tal, hola"
    print(buscarPalabra(txt))
    
main()