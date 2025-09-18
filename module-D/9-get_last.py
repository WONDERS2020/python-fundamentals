#!/usr/bin/python3
""" A module that gets the last item on the list"""

LinkedList = __import__("8-create-linkedlist").LinkedList


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    my_list.print_list()
    print(my_list.print_last())