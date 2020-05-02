def minletraRep(txt):
    conCar=0
    carMin=""
    canCarMin=0
    for car1 in txt:
        conCar=0
        for car2 in txt:
            if car1==car2:
                conCar+=1
        if carMin !="":
            if canCarMin < conCar:
                canCarMin = conCar
                carMin=car1
        else:
            conCarMin=conCar
            carMin =car1
    print(carMin,"->",conCarMin)
    
def main():
    txt="aaabbbbbbbbcccccccccccccc"
    minletraRep(txt)
    
main()