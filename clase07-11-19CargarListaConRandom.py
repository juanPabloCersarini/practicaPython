from random import randint

def azar(inf,sup):
    return randint(inf,sup)
def cargarListaAle(lst,cant,inf,sup):
    #.append() agrega al final
    #.insert(i,x) agrega en posicion
    #.pop() borra el ultimo
    #.pop(i) borra el contenido de la posición (retorna el contenido que borra)
    #.remove(contenido) borra el contenido donde se encuentra
    i=0
    val=azar(inf,sup)
   # while val!= 0:
    #   lst.append(val)
     #  i+=1
      # val=azar(0,20)
    while i<cant:
        
        lst.append(val)
        i+=1
        val=azar(inf,sup)
       
def main():
    lst=[]
    cargarListaAle(lst,10,0,5)
    print(lst)
    
main()