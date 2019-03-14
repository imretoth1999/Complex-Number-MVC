'''
Created on 27 Nov 2017

@author: tothi
'''
from Domain.ComplexNumber import ComplexNumber
from UI.UserInput import user_input
class ComplexNumberMenu():
    def __init__(self,ctrl):
        self.__ctrl = ctrl
    @staticmethod
    def printMenu():
        '''
        We show the menu 
        '''
        print('Input -2 for clearing the repository')
        print('Input -1 for adding an complex number')
        print("Input 0 for exiting the program")
        print('Input 1 for viewing the real part of the complex numbers')
        print('Input 2 for viewing the imaginary part of the complex numbers')
        print('Input 3 for viewing the complex numbers')
        print('Input 4 for viewing the polar forms of the complex numbers')
        print('Input 5 for viewing the conjugate of the complex numbers')
        print('Input 6 for multiplying the complex numbers by a real number')
        print('Input 7 for multiplyng the complex numbers by a imaginary number')
        print('Input 8 for adding two complex numbers')
        print('Input 9 for multiplying two complex numbers')
        print('Input 10 for showing the matrix representation of the numbers')
        print('Input 11 for getting the numbers at a given power')
        print('Input 12 for finding the square root of the numbers')
        print('Input 13 for finding the exponential form of the numbers')
        print(".....................................................")
    def menu(self):
        self.__ctrl.read_nr('numbers.txt')
        while True:
            ComplexNumberMenu.printMenu()
            command = user_input()
            if command == -2:
                self.__ctrl.useclear()
            if command == -1:
                self.__ctrl.createNumber(user_input(),user_input())
            elif command == 0:
                exit()
            elif command == 1:
                self.__ctrl.use1()
            elif command == 2:
                self.__ctrl.use2()
            elif command == 3:
                self.__ctrl.use3()
            elif command == 4:
                self.__ctrl.use4()
            elif command == 5:
                self.__ctrl.use5()
            elif command == 6:
                self.__ctrl.use6()
            elif command == 7:
                self.__ctrl.use7()
            elif command == 8:
                self.__ctrl.use8()
            elif command == 9:
                self.__ctrl.use9()
            elif command == 10:
                self.__ctrl.use10()
            elif command == 11:
                self.__ctrl.use11()
            elif command == 12:
                self.__ctrl.use12()
            elif command == 13:
                self.__ctrl.use13()