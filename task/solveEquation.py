import math
from robocorp.tasks import task
import instructions
from PySimpleGUI import PySimpleGUI as sg

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
        return (f"Erro ao calcular a função: {error}")

#======================================================================================
#RUN THE ITERACTION METHOD
#======================================================================================

def iteraction(function_str, a, b, e) -> str:
    expected_error = eval(e)
    xi = 0
    total_iteraction = 0

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

        xi = (a+b)/2
        fxi = calculate_function(function_str, xi)

        if (fa * fxi) < 0:
            b = xi
        else:
            a = xi

        total_iteraction += 1

        if expected_error > abs(b-a):
            break
    
    if total_iteraction == 1:  
        return (f'A raíz é {xi}. Foi necessária {total_iteraction} iteração.')
    
    return (f'A raíz é {xi}. Foram necessárias {total_iteraction} iterações.')


#======================================================================================
#DISPLAY THE INPUTS AND OUTPUTS FOR THE USER
#======================================================================================
'''
@task
def inputs() -> None:
    instructions.show_instructions()
    function_str = input("Entre com a função f(x): ")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    e = input("Entre com o valor de euler(erro): ")

    final_result = iteraction(function_str, a, b, e)

    print(final_result)'''

@task
def interface():
    sg.theme('Reddit')
    layout = [
        [sg.Text(instructions.text)],
        [sg.Text('Entre com a função f(x):',size=(20,1)), sg.Input(key = 'function_str',size=(20,1))],
        [sg.Text("Entre com o valor de a: ",size=(20,1)), sg.Input(key = 'a',size=(20,1))],
        [sg.Text("Entre com o valor de b: ",size=(20,1)), sg.Input(key = 'b',size=(20,1))],
        [sg.Text("Entre com erro permitido(E): ",size=(20,1)), sg.Input(key = 'e',size=(20,1))],
        [sg.Column([[sg.Button('calcular')]], justification='center')], 
        [sg.Text('', key='result', size=(40, 1))]
    ]
    janela = sg.Window('Calculate by iteraction', layout)

    while True:
        events, values = janela.read()
        if events == sg.WINDOW_CLOSED:
            break
        if events == 'calcular':
            function_str = values['function_str']
            a = float(values['a'])
            b = float(values['b'])
            e = values['e']
            final_result = iteraction(function_str, a, b, e)
            janela['result'].update(final_result)