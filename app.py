'''
Created on 27 Nov 2017

@author: tothi
'''
from Domain.Repo import ComplexRepository
from Controller.ComplexNumberController import ComplexNumberController
from UI.Menu import ComplexNumberMenu 
from Domain.ComplexNumber import ComplexNumber
def start():
    repo = ComplexRepository()
    ctrl = ComplexNumberController(repo)
    ui = ComplexNumberMenu(ctrl)
    ui.menu()
#start()
c = ComplexNumber(5,2)
print(c.exponentialComplex())