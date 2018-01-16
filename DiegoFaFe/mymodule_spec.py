# -*- coding: utf-8 -*-

from expects import *
import mymodule

with description('FizzBuzz'):
    with it('inputs 1 returns 1'):
        mymodule.return_1_if_number_is_1()
    with it('inputs 2 returns 2'):
        mymodule.return_2_if_number_is_2()
    with it('inputs 3 returns Fizz'):
        mymodule.return_Fizz_if_number_is_3()
