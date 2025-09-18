#!/usr/bin/python3
""" A module that crete an iterator classs"""

class NumberIterator:
    """ a class that create an iterator clas"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
        
if __name__ == "__main__":
    """ main function to test the number iterator"""
    number_iterator = NumberIterator(1, 5)
    print(dir(number_iterator.__iter__()))


    #print(list(number_iterator))