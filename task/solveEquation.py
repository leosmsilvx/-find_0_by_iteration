import math
from robocorp.tasks import task
import instructions

@task
def teste():
    result = eval('10**-3')
    print(result)


def calculate_function(function_str, x) -> str:
    try:
        result = eval(function_str)
        return result
    except Exception as error:
        return f"Erro ao calcular a função: {error}"

def iteraction(function_str, a, b, e) -> str:
    expected_error = eval(e)
    xi = 0

    while expected_error < abs(b-a):
        fa = calculate_function(function_str, a)
        fb = calculate_function(function_str, b)

        if(fa*fb) > 0:
            return (f'Não há uma raiz entre {a} e {b}')

        xi = (a+b)/2
        fxi = calculate_function(function_str, xi)

        if (fa * fxi) < 0:
            b = xi
        else:
            a = xi

    return (f'A raíz é {xi}.')

    #result = calculate_function(function_str, a)

@task
def inputs() -> None:
    instructions.show_instructions()
    function_str = input("Entre com a função f(x): ")
    a = float(input("Entre com o valor de a: "))
    b = float(input("Entre com o valor de b: "))
    e = input("Entre com o valor de euler(erro): ")

    final_result = iteraction(function_str, a, b, e)

    print(final_result)
