def tablaConFor(num):
    for x in range(1,11):
        print(num," x ", x,"=", num*x)
        
def tablaConWhile(num):
    i = 1
    while i<=10:
        print(num," x ", i,"=", num*i)
        i+=1

def main():
    print("---TABLA CON FOR----")
    tablaConFor(4)
    print("----TABLA CON WHILE----")
    tablaConWhile(4)

main()