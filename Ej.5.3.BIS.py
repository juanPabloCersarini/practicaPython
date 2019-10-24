def cambiarMinXMay(pal):
    palNueva=""
    for letra in pal:
        if letra =="a":
            palNueva=palNueva+chr(ord(letra)-32)
        elif letra =="e":
            palNueva=palNueva+chr(ord(letra)-32)
        elif letra =="i":
            palNueva=palNueva+chr(ord(letra)-32)
        elif letra=="o":
            palNueva=palNueva+chr(ord(letra)-32)
        elif letra=="u":
            palNueva=palNueva+chr(ord(letra)-32)
        else:
            palNueva+=letra
    print(palNueva)
    
def main():
    pal="francisco"
    cambiarMinXMay(pal)
    
main()