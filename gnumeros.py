from timeit import *
from tkinter import *
import sys
import random

sys.setrecursionlimit(9000)
#print(sys.getrecursionlimit())

ventana1=Tk()
ventana1.title("Generador de numeros")
ventana1.geometry("300x200")

#Generar los numeros aleatorios con una estrucura de datos de conjunto (hash set)
def gnumeros ():        
    num_min = -10000000
    num_max = 10000000
    n = 1000000

    numeros_randoms = set()

    while len(numeros_randoms) < n:
        numeros_randoms.add(random.randint(num_min, num_max))

    # guardar los numeros generados en un archivo de texto
    with open("numeros4.txt", "w") as f:
        for number in numeros_randoms:
            f.write(str(number) + "\n")

#Ordenar los numeros utilizando el metodo Quicksort
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivote = nums[len(nums) // 2]
    left_nums = [num for num in nums if num < pivote]
    mid_nums = [num for num in nums if num == pivote]
    right_nums = [num for num in nums if num > pivote]
    return quicksort(left_nums) + mid_nums + quicksort(right_nums)

def ordenar_numeros():
    #Leer el archivo de texto de los numeros aleatorios
    with open("numeros4.txt", "r") as f:
        numeros = [int(linea.strip()) for linea in f]

    numeros_ordenados = quicksort(numeros)
    
    #guardar los numeros ordenados en un nuevo archivo de texto
    with open("numeros_ordenados.txt", "w") as f:
        for numero in numeros_ordenados:
            f.write(str(numero) + "\n")

#widgets
btn1 = Button(ventana1, text="Generar numeros", command=gnumeros) 
btn1.pack()

btn2 = Button(ventana1, text="Ordenar numeros", command=ordenar_numeros)
btn2.pack()

ventana1.mainloop()