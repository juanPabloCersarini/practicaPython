def ingresarInt(msj):
    print(msj,end="")
    x=int(input())
    return x

def cargarLista(lst):
    #.append() agrega al final
    #.insert(i,x) agrega en posicion
    #.pop() borra el ultimo
    #.pop(i) borra el contenido de la posición (retorna el contenido que borra)
    #.remove(contenido) borra el contenido donde se encuentra
    i=0
    val=ingresarInt("["+str(i)+"]: ")
    while val!= 0:
       lst.append(val)
       i+=1
       val=ingresarInt("["+str(i)+"]: ")
       
def main():
    lst=[]
    cargarLista(lst)
    print(lst)
    
main()