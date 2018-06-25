from stack import *
def strrev(input_string):
    ls=Stack()
    s=''
    for a in input_string:
        ls.push(a)
    for a in ls:
        s+=a.data
        ls.pop()
    return s
n=input('Enter the string to be reversed: ')
print('Reversed String:',strrev(n))
