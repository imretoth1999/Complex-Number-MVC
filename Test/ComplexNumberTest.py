'''
Created on 21 Nov 2017

@author: tothi
'''
from unittest import TestCase, main
from Domain.ComplexNumber import ComplexNumber

class ComplexNumberTest(TestCase):
    def test_gets_sets_str(self):
        complex = ComplexNumber(1,2)
        complex1 = ComplexNumber(1,-1)
        self.assertEqual(complex.getRealPart(), 1)
        self.assertEqual(complex.getImagPart(), 2)
        self.assertEqual(complex1.getRealPart(), 1)
        self.assertEqual(complex1.getImagPart(), -1)
        self.assertEqual(str(complex),'1 +2i')
        complex.setRealPart(4)
        complex.setImagPart(-100)
        self.assertEqual(complex.getRealPart(), 4)
        self.assertEqual(complex.getImagPart(), -100)
        self.assertEqual(str(complex),'4 -100i')
    def test_modulus_argument_polar(self):
        complex = ComplexNumber(3,4)
        self.assertEqual(complex.getModulus(), 5)
        self.assertAlmostEqual(complex.getArgument(), 53.13)
        self.assertEqual(complex.getPolarForm(),'5(cos(53.13) + isin(53.13))')
        complex.setRealPart(-4)
        complex.setImagPart(-3)
        self.assertEqual(complex.getModulus(),5)
        self.assertAlmostEqual(complex.getArgument(),36.87)
        self.assertEqual(complex.getPolarForm(),'5(cos(36.87) + isin(36.87))')
    def test_conjugate(self):
        complex = ComplexNumber(3,4)
        self.assertEqual(complex.getConjugate(), '3 -4i')
        complex.setImagPart(-4)
        self.assertEqual(complex.getConjugate(), '3 +4i')
    def test_multiply(self):
        complex = ComplexNumber(3,4)
        multiply = complex.multiplyReal(3)
        self.assertEqual(multiply.getRealPart(), 9)
        self.assertEqual(multiply.getImagPart(), 12)
        multiply = complex.multiplyImag(3)
        self.assertEqual(multiply.getRealPart(), -12)
        self.assertEqual(multiply.getImagPart(), 9)
        complex.setRealPart(-3)
        complex.setImagPart(-4)
        multiply = complex.multiplyReal(3)
        self.assertEqual(multiply.getRealPart(), -9)
        self.assertEqual(multiply.getImagPart(), -12)
        multiply = complex.multiplyImag(3)
        self.assertEqual(multiply.getRealPart(), 12)
        self.assertEqual(multiply.getImagPart(), -9)
    def test_addNumbers(self):
        c1 = ComplexNumber(3,4)
        c2 = ComplexNumber(1,1)
        c3 = c1.addNumbers(c2)
        self.assertEqual(c3.getRealPart(), 4)
        self.assertEqual(c3.getImagPart(), 5)
        c4 = ComplexNumber(-1,2)
        c5 = ComplexNumber(2,-4)
        c6 = c4.addNumbers(c5)
        self.assertEqual(c6.getRealPart(),1)
        self.assertEqual(c6.getImagPart(), -2)
    def test_multiplyNumbers(self):
        c1 = ComplexNumber(3,4)
        c2 = ComplexNumber(1,1)
        c3 = c1.multiplyNumbers(c2)
        self.assertEqual(c3.getRealPart(), -1)
        self.assertEqual(c3.getImagPart(), 7)
        c4 = ComplexNumber(-1,2)
        c5 = ComplexNumber(2,-4)
        c6 = c4.multiplyNumbers(c5)
        self.assertEqual(c6.getRealPart(),6)
        self.assertEqual(c6.getImagPart(), 8)
    def test_matrixRepresentation(self):
        c1 = ComplexNumber(3,4)
        c2 = ComplexNumber(1,1)
        self.assertEqual(c1.matrixComplex(), [[3,-4],[4,3]])
        self.assertEqual(c2.matrixComplex(), [[1,-1],[1,1]])
        c4 = ComplexNumber(-1,2)
        c5 = ComplexNumber(2,-4)
        self.assertEqual(c4.matrixComplex(),[[-1,-2],[2,-1]])
        self.assertEqual(c5.matrixComplex(), [[2,4],[-4,2]])
    def test_powerComplex(self):
        c1 = ComplexNumber(3,4)
        c3 = c1.powerComplex(3)
        self.assertEqual(c3.getRealPart(),-84)
        self.assertEqual(c3.getImagPart(), 92)
        c2 = ComplexNumber(100,32)
        c4 = c2.powerComplex(0)
        self.assertEqual(c4.getRealPart(),1)
        self.assertEqual(c4.getImagPart(), 0)
        try:
            c1.powerComplex(-1)
            assert False
        except:
            assert True
    def test_squarerootComplex(self):
        c1 = ComplexNumber(3,4)
        c2 = c1.squarerootComplex()
        self.assertEqual(c2.getRealPart(), 2)
        self.assertEqual(c2.getImagPart(), 1)
        c2 = ComplexNumber(1,0)
        c2 = c2.squarerootComplex()
        self.assertEqual(c2.getRealPart(),1)
        self.assertEqual(c2.getImagPart(), 0)
    def test_exponentialComplex(self):
        c1 = ComplexNumber(3,4)
        c2 = c1.exponentialComplex()
        self.assertAlmostEqual(c2.getRealPart(),-13,0)
        self.assertAlmostEqual(c2.getImagPart(), -15,0)
        c2 = ComplexNumber(1,0)
        c2 = c2.exponentialComplex()
        self.assertAlmostEqual(c2.getRealPart(),2.7,0)
        self.assertAlmostEqual(c2.getImagPart(), 0,0)
        
if __name__ == '__main__':
    main()
        