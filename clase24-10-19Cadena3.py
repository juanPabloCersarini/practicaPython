def esLetra(letra):
    return (letra>="a" and letra<="z" or letra>="A" and letra<="Z")

def contarPal(txt):
    i=0
    while i<len(txt):
        pal = ""
        while i<len(txt) and esLetra(txt[i]):
            pal+=txt[i]
            i+=1
        if pal != "":
            if len(pal)%2==1:
                print(pal)
        i+=1
        
def main():
    print(contarPal("Hola que tal como estas"))
    
main()