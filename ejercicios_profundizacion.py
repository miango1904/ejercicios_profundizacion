#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')
    #Realice un programa que solicite por consola 2 números
    #Calcule la diferencia entre ellos e informe por pantalla
    #si el resultado es positivo, negativo o cero.
    print('ingrese un numero')
    numero_1 = int(input())
    print('ingrese otro numero')
    numero_2 = int(input())
    dif = numero_1 - numero_2
    if dif > 0:
        print('dif',dif,'es positivo')
    elif dif < 0:
        print('dif',dif,'es negativo')
    else:
        print('la diferencia es cero')


def ej2():
    print('Ejercicios de práctica con números')
    #Realice un programa que solicite el ingreso de tres números
    #enteros, y luego en cada caso informe si el número es par
    #o impar.
    #Para cada caso imprimir el resultado en pantalla.
    print('ingrese un numero')
    numero_1 = int(input())
    print('ingrese otro numero')
    numero_2 = int(input())
    print('ingrese un numero')
    numero_3 = int(input())
    if numero_1%2==0:
        print('numero_1',numero_1,'es par')
    else:
        print ('numero_1',numero_1,'es impar')
    if numero_2%2==0:
        print('numero_2',numero_2,'es par')
    else:
        print ('numero_2',numero_2,'es impar')
    if numero_3%2==0:
        print('numero_3',numero_3,'es par')
    else:
        print ('numero_3',numero_3,'es impar')
    
    
    
    
    


def ej3():
    print('Ejercicios de práctica con números')

    #Realice una calculadora, se ingresará por línea de comando dos números
    #Luego se ingresará como tercera entrada al programa el símbolo de la operación
    #que se desea ejecutar
    # Suma (+)
    # Resta (-)
    # Multiplicación (*)
    # División (/)
    # Exponente/Potencia (**)
    # Se debe efectuar el cálculo correcto según la operación ingresada por consola
    #Imprimir en pantalla la operación realizada y el resultado

    print('ingrese un numero')
    numero_1 = int(input())
    print('ingrese otro numero')
    numero_2 = int(input())

    print("""
    seleccione su calculo
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los números elegidos
    5) Potencia
    """)
    
    calculo = int(input('seleccione su calculo :'))
    if calculo== 1:
        print (numero_1 + numero_2)
    elif calculo== 2:
        print(numero_1 - numero_2)
    elif calculo== 3:
        print(numero_1 * numero_2)
    elif calculo== 4:
        print(numero_1 / numero_2)
    elif calculo== 5:
        print(numero_1 ** numero_2)
        

      
    
def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    print('ingrese primer palabra')
    primer_palabra = input()

    print('ingrese segunda palabra')
    segunda_palabra = input()

    print('ingrese tercer palabra')
    tercer_palabra = input()
    
    print('seleccione orden 1 ,2')
    orden= int(input ('seleccione orden: '))
    if orden == 1 and primer_palabra < segunda_palabra < tercer_palabra:
        print(primer_palabra, segunda_palabra,tercer_palabra)
    elif orden ==1 and primer_palabra < tercer_palabra < segunda_palabra:
        print (primer_palabra,tercer_palabra,segunda_palabra)
    elif orden == 1 and segunda_palabra< primer_palabra< tercer_palabra:
        print (segunda_palabra,primer_palabra,tercer_palabra)
    elif orden == 1 and segunda_palabra<tercer_palabra<primer_palabra:
        print (segunda_palabra,tercer_palabra,primer_palabra)
    elif orden == 1 and tercer_palabra<primer_palabra<segunda_palabra:
        print(tercer_palabra,primer_palabra,segunda_palabra)
    elif orden == 1 and tercer_palabra<segunda_palabra<primer_palabra:
        print(tercer_palabra,segunda_palabra,primer_palabra)

    caracter1 = len('primer_palabra')
    caracter2 = len('segunda_palara')
    caracter3 = len('tercer_palabra')
    if orden == 2 and caracter1 < caracter2 < caracter3:
        print(primer_palabra,segunda_palabra,tercer_palabra)
    elif orden == 2 and caracter1 < caracter3 < caracter2:
        print(primer_palabra,tercer_palabra,segunda_palabra)
    elif orden == 2 and caracter2 < caracter1 <caracter3:
        print(segunda_palabra,primer_palabra,tercer_palabra)
    elif orden == 2 and caracter2 < caracter3 < caracter1 :
        print(segunda_palabra,tercer_palabra,primer_palabra)
    elif orden == 2 and caracter3 < caracter2 < caracter1:
        print(tercer_palabra,segunda_palabra,primer_palabra)
    elif orden == 2 and tercer_palabra < primer_palabra < segunda_palabra:
        print(tercer_palabra,primer_palabra,segunda_palabra)
        



def ej5():
    print('Ejercicios de práctica con números')

    
    #Realice un programa que solicite ingresar tres valores de temperatura
    #De las temperaturas ingresadas por consola determinar:
    #1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    #2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    #3 - ¿Cuál es el promedio de las temperaturas ingresadas?
   # En cada caso imprimir en pantalla el resultado

    print('ingrese primer valor')
    primer_valor = float (input())

    print('ingrese segundo valor')
    segunda_valor = float (input())

    print('ingrese tercer valor')
    tercer_valor = float (input())
    print('seleccione opcion: 1 , 2, 3 ,1_maxima, 2_minima, 3_promedio')
    opcion = int (input ('seleccione opcion: '))
    if opcion == 1 and primer_valor > segunda_valor > tercer_valor:
        print(primer_valor )
    elif opcion == 1 and primer_valor > tercer_valor > segunda_valor :
        print(primer_valor)
    elif opcion == 1 and segunda_valor > primer_valor > tercer_valor:
        print (segunda_valor)
    elif opcion == 1 and segunda_valor > tercer_valor > primer_valor:
        print(segunda_valor)
    elif opcion == 1 and tercer_valor> primer_valor > segunda_valor:
        print(tercer_valor)
    elif opcion ==1 and tercer_valor > segunda_valor > primer_valor:
        print (tercer_valor)

    if opcion == 2 and primer_valor < segunda_valor < tercer_valor:
        print(primer_valor )
    elif opcion == 2 and primer_valor < tercer_valor < segunda_valor :
        print(primer_valor)
    elif opcion == 2 and segunda_valor < primer_valor < tercer_valor:
        print (segunda_valor)
    elif opcion == 2 and segunda_valor < tercer_valor < primer_valor:
        print(segunda_valor)
    elif opcion == 2 and tercer_valor < primer_valor < segunda_valor:
        print(tercer_valor)
    elif opcion == 2 and tercer_valor < segunda_valor < primer_valor:
        print (tercer_valor)

    pro_medio = (primer_valor + segunda_valor + tercer_valor) / 3

    if opcion == 3 :
        print(pro_medio)
    


    









if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
