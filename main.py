from stack_func import isempty, push, pop


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.start = None

    def is_empty(self):
        if self.start is None:
            print("list is empty")
            return None

    def insert(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
        else:
            x = self.start
            while x.next is not None:
                x = x.next
            x.next = new_node

    def remove(self):
        if self.start is None:
            print("list is empty")
        else:
            val = self.start.value
            self.start = self.start.next
            return val


def palindrome_checker(string, stack):
    for char in string:
        push(stack, char)
        SLList.insert(char)
    while not isempty(stack):
        char_from_stack = pop(stack)
        char_from_list = SLList.remove()
        if char_from_stack != char_from_list:
            print("Expression is not a palindrome, sorry")
            break
    if isempty(stack):
        print("Expression is a palindrome!")


SLList = SinglyLinkedList()
Stack = [None] * 20
pal_string = input("enter your text to check if it's a palindrome: \n")
palindrome_checker(pal_string, Stack)
