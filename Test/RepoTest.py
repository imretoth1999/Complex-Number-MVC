'''
Created on 27 Nov 2017

@author: tothi
'''
from unittest import TestCase, main
from Domain.Repo import ComplexRepository
from Domain.ComplexNumber import ComplexNumber
class ComplexRepositoryTest(TestCase):
    repo = ComplexRepository()
    assert repo.size() == 0
    
    c1 = ComplexNumber(1,2)
    repo.store(c1)
    assert repo.size() == 1
    repo.store(ComplexNumber(130,23))
    assert repo.size() == 2
    repo.delete_everything()
    assert repo.size() == 0


if __name__ == "__main__":
    main()