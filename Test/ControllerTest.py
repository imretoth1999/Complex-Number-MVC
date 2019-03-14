'''
Created on 27 Nov 2017

@author: tothi
'''
from unittest import TestCase, main
from Domain.Repo import ComplexRepository
from Controller.ComplexNumberController import ComplexNumberController
class testComplexNumberController(TestCase):
    repo = ComplexRepository()
    ctrl = ComplexNumberController(repo)
    ctrl.createNumber(3, 4)
    try:
        ctrl.CreateNumber('fp',3)
        assert False
    except:
        assert True
if __name__ == '__main__':
    main()
