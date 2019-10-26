def histograma(txt):
    aux=""
    for letra in txt:
        if letra not in aux:
            aux=aux+letra
    for car1 in aux:
        conCar=0
        for car2 in txt:
            if car1==car2:
                conCar+=1
        print(car1, "-->" ,conCar)
        
def main():
    histograma("hola que haces como estas")
    
main()