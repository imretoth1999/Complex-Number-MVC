'''
Created on 21 Nov 2017

@author: tothi
'''
import math
class ComplexNumber:
    '''
    This class takes two arguments, the real part of the complex number and the imaginary part
    RESTRICTION: The real part and imaginary part must be integers
    '''


    def __init__(self, real, imag):
        '''
        We initialise the class with the given arguments
        
        '''
        self.__real = real
        self.__imag = imag 
    def __str__(self):
        '''
        We show the form of the complex number
        '''
        if self.__imag >= 0:
            return str(self.__real) + ' +' + str(self.__imag) + 'i'
        return str(self.__real) + ' ' + str(self.__imag)  + 'i'
    def getRealPart(self):
        '''
        We return the real part
        '''
        return self.__real
    def getImagPart(self):
        '''
        We return the imaginary part
        '''
        return self.__imag
    def setRealPart(self,real):
        '''
        We set the real part with the given argument
        '''
        self.__real = real
    def setImagPart(self,imag):
        '''
        We set the imaginary part with the given argument
        '''
        self.__imag = imag
    def getModulus(self):
        '''
        We return the modulus
        '''
        return int(math.sqrt(self.__real**2 + self.__imag**2))
    def getArgument(self):
        '''
        We return the argument
        '''
        return round(math.degrees(math.atan(self.__imag/self.__real)),2)
    def getArgumentFull(self):
        '''
        We return the argument with full digits
        '''
        return math.acos(self.__real/self.getModulus())
    def getPolarForm(self):
        '''
        We return the polar form using the modulus and argument
        '''
        return str(self.getModulus()) + '(cos(' + str(self.getArgument()) + ') + isin(' + str(self.getArgument()) + '))'
    def getConjugate(self):
        '''
        We return the conjugate
        '''
        aux = -self.__imag
        if aux >= 0:
            return str(self.__real) + ' +' + str(aux) + 'i'
        return str(self.__real) + ' ' + str(aux) + 'i'
    def multiplyReal(self,nr):
        '''
        We multiply by a real number
        '''
        res = ComplexNumber(self.__real*nr,self.__imag*nr)
        return res
    def multiplyImag(self,img):
        '''
        We multiply by an imaginary number
        '''
        multiply = ComplexNumber(-self.__imag *img, self.__real * img)
        return multiply
    def addNumbers(self,other):
        '''
        We add two complex numbers
        '''
        res = ComplexNumber(self.__real + other.getRealPart(),self.__imag + other.getImagPart())
        return res
    def multiplyNumbers(self,other):
        '''
        We multiply two complex numbers
        '''
        res = ComplexNumber(self.__real * other.getRealPart() - self.__imag * other.getImagPart(),self.__real * other.getImagPart() + other.getRealPart() * self.__imag) 
        return res
    def matrixComplex(self):
        '''
        We return the matrix representation
        '''
        
        return [[self.__real,-self.__imag],[self.__imag,self.__real]]
    def powerComplex(self,p):
        '''
        We return the number at a given power
        '''
        if p < 0:
            raise ValueError
        c = ComplexNumber(int((self.getModulus()**p) * math.cos(p*self.getArgument())),int((self.getModulus()**p)*math.sin(p*self.getArgument())))
        return c
    def squarerootComplex(self):
        '''
        We return the square root of the number
        '''
        c = ComplexNumber(int(math.sqrt(self.getModulus()*math.cos(self.getArgumentFull()/2),)),int(math.sqrt(self.getModulus()*math.sin(self.getArgumentFull()/2))))
        return c
    def exponentialComplex(self):
        '''
        We return the exponential form of the number
        '''
        a = math.cos(int(self.__imag))
        b = math.sin(int(self.__imag))
        c = ComplexNumber(a,b)
        d = 1
        for i in range(int(self.__real)):
            d = d*math.e
        c=c.multiplyReal(d)
        return c