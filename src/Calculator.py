from CsvReader import CsvReader
from decimal import *

def addition(a, b):
    a = int(a)
    b = int(b)
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c

def m_division(a, b):
    a = int(a)
    b = int(b)
    c = b / a

    print(c)

    if  len(str(c)) == 17:
        t = float(str(c)[:-6])
    elif len(str(c)) == 19:
        t = float(str(c)[:-9])
    elif len(str(c)) == 12:
        t = float(str(c)[:-2])
    return c



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = m_division(a, b)
        return self.result

