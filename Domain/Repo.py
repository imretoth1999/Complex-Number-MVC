'''
Created on 27 Nov 2017

@author: tothi
'''
class ComplexRepository:
    '''
    Manage a list of Complex objects
    '''
    def __init__(self):
        self.__repo = []
    def store(self, number):
        '''
        Input: a complex object
        Output: we append the object to the repository
        '''
        self.__repo.append(number)
    def size(self):
        return len(self.__repo)
    def delete_everything(self):
        self.__repo.clear()
    def iterate(self):
        return self.__repo
    def add_nr(self, c):
        self.__repo.append(c)