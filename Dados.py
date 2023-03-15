print("-------------------------------------------------")
print("----------------------Dados----------------------")
print("-------------------------------------------------")

c = int(input(" Digite el numero del dado: "))

if 1 <= c <= 6:
    if c == 1:
        print("La cara inversa del 1 es 6") 

    elif c == 2:
        print("La cara inversa del 2 5 ")

    elif c == 3:
        print("La cara inversa del 3 es 4 ")

    elif c == 4:
        print("La cara inversa del 4 es 3 ")

    elif c == 5:
        print(" La cara inversa del 5 es 2 ")

    else:
        print(" La cara inversa del 6 es 1 ")

    
else :
    print("El numero no pertenece al dado ")