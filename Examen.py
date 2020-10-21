'''import numpy as np
a = np.array([2,1, 2,2, 4])
b = np.array([2, 1,2, 2, 4])
n=0
m=0
#a[n]*b[m]
#res = a * b
#print(res)
for ele in a:
    for ili in b:
        if a[1]*b[1]=="maso":
            print("hola")

        res = a * b'''
val=True



op=input("Que operacion deseas realizar \nSeparar letras y Numeros L: "
         "\nlogica ingresa A:\nsalir s:")
while val==True:
    if op.lower()=="l":
        palabra = input("Ingresa cadena")
        letra = []
        nume = []
        n = 0
        numeros = "12345678990"
        oracion = "abcdefghijklmnopqrstuvyxwzñ"
        longitud = len(palabra)
        while n <= len(palabra) - 1:
            if palabra[n] in numeros:
                nume.append(palabra[n])
            if palabra[n] in oracion:
                letra.append(palabra[n])
            n += 1
        print(nume)
        print(letra)

    op = input("Que operacion deseas realizar \nSeparar letras y Numeros L: "
         "\nlogica ingresa A:\nsalir s:")
    #val=False

    if op.lower()=="n":

        op = input("Que operacion deseas realizar \nlogia ingresa L: "
                   "\nAritmetica ingresa A:\nSepararletras y numeros n:\nsalir s:")
    elif op.lower()=="a":
        p = [True, False]
        q = [True, False]

        # Tabla de verdad de or

        print('x\ty\tx  y')
        print('-' * 22)
        for x in p:
            for y in q:
                print(x, y, x or y, sep='\t')
        print()
        #segundo arreglo y bucle
        print('-' * 22)
        for x in p:
            for y in q:
                print(x, y, x and y, sep='\t')

        print()
        print('x\ty\tx  y', )
        print('-' * 22)
        for x in p:
            for y in q:
                print(y, x, y and x, sep='\t')
        print()

        op = input("Que operacion deseas realizar \nSeparar letras y Numeros L: "
         "\nlogica ingresa A:\nsalir s:")
    elif op.lower()=="s":
        print("fin")
        val=False
    elif op!="l" or op!="a" or op!="n" or op!="s":
        print("esa opcion no existe\nIngresa otra opcion valida")
        op = input("Que operacion deseas realizar \nlogia ingresa L: "
                   "\nAritmetica ingresa A:\nSepararletras y numeros n:\nsalir s:")
        #val=False