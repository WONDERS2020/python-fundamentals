#/usr/bin/python3
""" A function that finds the biggest of a list"""
def max_integer(my_list=[]):
    if len(my_list) ==0:
        return max(my_list)
    
    mylist = [1, 90, 2, 13, 34, 5, -13, 3, -99]
    result = max_integer(mylist)
    print(result)

    #mylist[4] = 10
    mylist.remove(3)
    print(mylist)