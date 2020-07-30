from collections import deque as dq


def balance(string):
    stack1 = Stack('')
    len_mas = 0
    for letter in string:

        try:
            if letter == '(' or letter == '{' or letter == '[':
                stack1.push(letter)
            elif '(' == stack1.peek() and letter == ')':
                stack1.pop()
            elif '{' == stack1.peek() and letter == '}':
                stack1.pop()
            elif '[' == stack1.peek() and letter == ']':
                stack1.pop()
            else:
                len_mas = 10
                break
            len_mas = stack1.size()
        except IndexError:
            len_mas = 10
            break

    if len_mas == 0:
        print('Сбалансированно')
    else:
        print('Небалансированно')


class Stack:

    def __init__(self, iterable=None):
        self.stack = dq(iterable)

    def is_empty(self):
        if len(self.stack):
            return False    #вернет False, если не пустой
        return True     #вернет True, если пустой

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        self.stack.pop()

    def peek(self):
        top_elem = self.stack.pop()
        self.stack.append(top_elem)
        return top_elem

    def size(self):
        return len(self.stack)


###############begin#########################
if __name__ == '__main__':
    list_of_strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']# примеры из задания

    for item in list_of_strings:
        balance(item)

