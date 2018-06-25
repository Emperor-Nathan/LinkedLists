from stack import *
def revKElements(input_string, k):
    s=Stack()
    n=0
    r=''
    p=''
    while n<k:
        s.push(input_string[n])
        n+=1
    while n<len(input_string)-1:
        r+=input_string[n]
        r+=','
        n+=1
    r+=input_string[n]
    for a in s:
        p+=a.data
        p+=','
    p+=r
    return p
i=input('Enter the list of numbers: ')
k=int(input('Enter k: '))
i+=','
l=[]
s=''
for a in i:
    if a in '0123456789':
        s+=a
    elif a==',':
        l.append(s)
        s=''
print(revKElements(l,k))
