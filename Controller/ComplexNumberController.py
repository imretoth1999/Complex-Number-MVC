'''
Created on 27 Nov 2017

@author: tothi
'''
from Domain.ComplexNumber import ComplexNumber
from UI.UserInput import user_input
import re 
class ComplexNumberController():
    '''
    Controller for operations on Complex Number list
    '''
    def __init__(self, repo):
        self.__repo = repo
    def createNumber(self,real = 0,imag = 0):
        '''
        Creates an object Complex Number
        Input:The real part and the imaginary part of the number
        Output: the number created and stored into the repo
        '''
        
        c = ComplexNumber(real,imag)
        self.__repo.store(c)
    def addNumber(self,c):
        self.__repo.store(c)
    def useclear(self):
        self.__repo.delete_everything()
        print("The repository was cleared")
        print(".....................................................")
    '''   
    def read_nr(self,filename):
        try:
            filename = open(filename, "r")
            c1 = filename.read()
            filename.close()
            c1 = [line.split() for line in c1.split("\n")]
            c1 = [[int(y) for y in x] for x in c1]
            for item in c1:
                self.__repo.add_nr(ComplexNumber(item[0],item[1]))
        except :
            print('Error while opening the file')
            print('Fix the error then try again')
            exit()
    '''
    def read_nr(self,filename):
        '''
        We read the numbers from a file
        We split the text and we find the numbers using a regex
        '''
        try:
            filename = open(filename,'r')
            c1 = filename.read()
            filename.close()
            c1 = [line.split() for line in c1.split('\n')]
            for item in c1:
                nr = re.findall('\d+', str(item))
                if len(nr) > 2:
                    raise IOError
                self.__repo.add_nr(ComplexNumber(nr[0],nr[1]))
        except IOError :
            print('Error while opening the file')
            print('Fix the error then try again')
            exit()
    
    def use1(self):
        '''
        We get the real parts from the complex numbers
        '''
        try:
            f = open('Rez.txt','a')
            for elem in self.__repo.iterate():
                f.write(str(elem.getRealPart()))
                f.write('\n')
            f.write("These were the real parts\n")
            f.close()
        except:
            print('Error while writing the file')
            exit()
        
    def use2(self):
        '''
        We get the imaginary parts from the complex numbers
        '''
        try:
            f = open('Rez.txt','a')
            for elem in self.__repo.iterate():
                f.write(str(elem.getImagPart()))
                f.write('i\n')
            f.write("These were the imaginary parts\n")
            f.close
        except:
            print('Error while writing the file')
            exit()

    def use3(self):
        '''
        List the numbers
        '''
        try:
            f = open('Rez.txt','a')
            for elem in self.__repo.iterate():
                f.write(str(elem))
                f.write('\n')
            f.write("These were the numbers stored\n")
            f.close()
        except:
            print('Error while writing the file')
            exit()

    def use4(self):
        '''
        Show the polar form of every complex number
        '''
        try:
            f = open('Rez.txt','a')
            for elem in self.__repo.iterate():
                f.write(str(elem.getPolarForm()))
                f.write('\n')
            f.write('These were the polars forms\n')
            f.close()
        except:
            print('Error while writing the file')
            exit()


    def use5(self):
        '''
        Show the conjugate of every complex number
        '''
        try:
            f = open('Rez.txt','a')
            for elem in self.__repo.iterate():
                f.write(str(elem.getConjugate()))
                f.write('\n')
            f.write('These were the conjugate forms\n')
            f.close()
        except:
            print('Error while writing the file')
            exit()

    def use6(self):
        '''
        We multiply  the complex numbers by a given real number
        '''
        try:
            n = user_input()
            l = self.__repo.iterate()
            f = open('Rez.txt','a')
            for i in range(len(l)):
                f.write(str(l[i].multiplyReal(n)))
                l[i] = l[i].multiplyReal(n)
                f.write('\n')
            f.write('These were the numbers multiplyed by the chosen real number\n')
            f.close()
        except:
            print('Error while writing the file')
            exit()

        
    def use7(self):
        '''
        We multiply the complex numbers by a given imaginary number
        '''
        try:
            n = user_input()
            l = self.__repo.iterate()
            f = open('Rez.txt','a')
            for i in range(len(l)):
                f.write(str(l[i].multiplyImag(n)))
                l[i] = l[i].multiplyImag(n)
                f.write('\n')
            f.write('These were the numbers multiplyed by a given imaginary number')
            f.close()
        except:
            print('Error while writing the file')
            exit()

    def use8(self):
        '''
        We add two complex numbers
        '''
        c1 = ComplexNumber(user_input(),user_input())
        print('We add two complex numbers:')
        l = self.__repo.iterate()
        for i in range(len(l)):
            print('For the number : ',l[i])
            print("The result is: ",l[i].addNumbers(c1))
            l[i] = l[i].addNumbers(c1)
        print(".....................................................")
    def use9(self):
        '''
        We multiply two complex numbers
        '''
        c1 = ComplexNumber(user_input(),user_input())
        print('We multiply two complex numbers:')
        l = self.__repo.iterate()
        for i in range(len(l)):
            print('For the number : ',l[i])
            print("The result is: ",l[i].multiplyNumbers(c1))
            l[i] = l[i].multiplyNumbers(c1)
        print(".....................................................")
    def use10(self):
        '''
        We get the matrix representation of the complex numbers
        '''
        l = self.__repo.iterate()
        for i in range(len(l)):
            print('The matrix representation of : ',l[i])
            matrix = l[i].matrixComplex()
            print(matrix[0])
            print(matrix[1])
        print(".....................................................")
    def use11(self):
        '''
        We get the number at a given power
        '''
        l = self.__repo.iterate()
        p = user_input()
        for i in range(len(l)):
            print('The number: ',l[i],'at the power ',p,'is:')
            l[i] = l[i].powerComplex(p)
            print(l[i])
        print(".....................................................")
    def use12(self):
        '''
        We get the square root of the given number
        '''
        l = self.__repo.iterate()
        for i in range(len(l)):
            print('The square root of the number ',l[i],' is ',l[i].squarerootComplex())
            l[i] = l[i].squarerootComplex()
        print(".....................................................")
    def use13(self):
        '''
        We get the exponential form
        '''
        l = self.__repo.iterate()
        for i in range(len(l)):
            #print('The square root of the number ',l[i],' is ',l[i].exponentialComplex())
            l[i] = l[i].exponentialComplex()
        print(".....................................................")