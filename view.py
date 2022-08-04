from fractions import Fraction
import cmath
import sys

def view_data(data,title):
    print(f'{title} = {data}')

def get_value():
    value= int(input('Введите число: '))
    try:
        value = Fraction(value)
        return value
    except ValueError:
        value = complex(value)
        return value

def get_operator():
    oper = input('Введите оператор: ')
    return oper


def get_result(res):
    print(f'Результат: {res}')