import math
from robocorp.tasks import task
import instructions
from PySimpleGUI import PySimpleGUI as sg
import time
import csv


#======================================================================================
#CALCULATE THE FUNCTION F(X)
#======================================================================================

def calculate_function(function_str, x) -> float:
    try:
        result = eval(function_str, {'x': x, 'math': math, 'sin': math.sin, 'cos': math.cos, 
                                     'tan': math.tan, 'log': math.log, 'log10': math.log10, 
                                     'sqrt': math.sqrt, 'abs': abs})
        return result
    except Exception as error:
        print (f"Erro ao calcular a função: {error}")
        return None

#======================================================================================
#RUN THE ITERACTION METHOD
#======================================================================================

def iteraction(function_str, a, b, e) -> None:
    expected_error = eval(e)
    xi = 0
    total_iteraction = 0
    data = []
    csv_filename = f"csv_iteraction_{int(time.time())}.csv"

    while True:
        fa = calculate_function(function_str, a)
        fb = calculate_function(function_str, b)

        if fa == 0:
            xi = a
            break
        if fb == 0:
            xi = b
            break

        if(fa*fb) > 0:
            return (f'Não há uma raiz entre {a} e {b}')

        total_iteraction += 1

        xi = (a+b)/2
        fxi = calculate_function(function_str, xi)

        data.append([total_iteraction, a, b, xi])

        '''
        print(f"iteração {total_iteraction}:")
        print(f"a: {a}")
        print(f"b: {b}")
        print(f"xi: {xi}")
        '''

        if (fa * fxi) < 0:
            b = xi
        else:
            a = xi

        if expected_error > abs(b-a):
            break

    save_to_csv(csv_filename, data) # CHAMANDO A NOVA FUNÇÂO UTILIZANDO A VARIAVEL QUE ESTAVA EM DESUSO

def save_to_csv(filename, data): #CRIAÇÂO DA FUNÇÂO QUE GERA O ARQUIVO
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Iteraction", "a", "b", "xi"])
        writer.writerows(data)


#======================================================================================
#DISPLAY THE INPUTS AND OUTPUTS FOR THE USER
#======================================================================================

@task
def inputs() -> None:
    print(instructions.text)
    function_str = input("Entre com a função f(x): ")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    e = input("Entre com o valor de euler(erro): ")

    start_time = time.time()
    iteraction(function_str, a, b, e)
    end_time = time.time()
    execution_time = (end_time-start_time) * 1000

    print(f"\nTempo de execução: {execution_time:.2f} ms")
