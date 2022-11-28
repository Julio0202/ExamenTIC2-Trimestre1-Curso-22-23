def funcionInterfaz():
    print("1 - Sumar")
    print("2 - Salir")
def funcionSuma(num1,num2):
    return num1+num2
contador=0
while contador!=2:
    try:
        funcionInterfaz()
        contador = int(input())
    except:
        if contador !=int:
            print("Intentalo de nuevo")
    if contador == 1:
        try:
            print("Dime el primer numero")
            num1 = int(input())
            print("Dime el segundo numero")
            num2 = int(input())
            print("La suma es",funcionSuma(num1,num2))
        except: 
            if num1 and num2 != int:
                print("Intentalo de nuevo")
print("Ha acabado el programa")
