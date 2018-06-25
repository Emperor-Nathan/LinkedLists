from stack import *
def math(list):
    count=0
    sum=0
    product=1
    max=0
    min=list.top.data
    for a in list:
        count+=1
        sum+=a.data
        product*=a.data
        if max<a.data:
            max=a.data
        if min>a.data:
            min=a.data
    mean=sum/count
    print('Total count = ',count,'\nSum = ',sum,'\nProduct = ',product,'\nMean = ',mean,'\nMin = ',min,'\nMax = ',max)
num=input('Enter the numbers: ')
stack=Stack()
n=0
s=''
if num[len(num)-1] in '0123456789':
    num+=', '
while n<len(num):
    if num[n] in '0123456789':
        s+=num[n]
    elif num[n]==',':
        stack.push(int(s))
        s=''
        n+=1
    n+=1
math(stack)
