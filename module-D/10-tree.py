#!/usr/bin/python3
""" A module that create a binary tree """
class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None


class Binarytree:
    def __init__ (self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value < root.value:
            if root.left == None:
                root.left = Node(value)
            else:
                self._insert(root.left, value)
        else:
            if root.right == None:
                root.right = Node(value)
            else:
                self._insert(root.right, value)

    def print_tree(self, current):
        if current:
            self.print_tree(current.left)
            print(current.value)
            self.print_tree(current.right)
        else:
            print("Empty Branch")


if __name__ == "__main__":
    binary = Binarytree()
    binary.insert(1)
    binary.insert(2)
    binary.insert(3)
    binary.insert(4)
    binary.insert(5)
    print(binary.root.right.value)
    print(binary.root.right.right.value)
    print(binary.root.right.right.right.value)
    print(binary.root.right.right.right.right.value)
    #binary.print_tree(binary)