# -*- coding: utf-8 -*-

from expects import *

class FizzBuzz:
    num1 = 3
    num2 = 5
    def __init__(self):
        pass

    def calculate(self, number):
        if number == 1:
            return 1
        elif number ==2:
            return 2
        else:
             return 'Fizz'

def return_1_if_number_is_1():
    x = FizzBuzz()
    expect(x.calculate(1) == 1).to(be_true)

def return_2_if_number_is_2():
    x = FizzBuzz()
    expect(x.calculate(2) == 2).to(be_true)

def return_Fizz_if_number_is_3():
    x = FizzBuzz()
    expect(x.calculate(3) == 'Fizz').to(be_true)