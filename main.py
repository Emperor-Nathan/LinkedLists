class Node(object):
    def __init__(self, content):
        if content is None:
            raise ValueError('Node must have content')
        self.c = content
        self.n = None
    @property
    def content(self):
        return self.c
    @content.setter
    def content(self, val):
        self.c = val
    @property
    def next(self):
        return self.n
    @next.setter
    def next(self, val):
        self.n = val
class SinglyList(object):
    def __init__(self):
        self.h = None
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    @property
    def head(self):
        return self.h
    @head.setter
    def head(self, val):
        self.h = val
    def isEmpty(self):
        return self.head == None
    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
#ex00
def print_list(list_head):
    a=list_head
    while a.next!=None:
        print(a.content)
        a=a.next
    print(a.content)
#ex01
def add_tail(list_head, val):
    a=list_head
    while a.next!=None:
        a=a.next
    a.next=Node(val)
#ex02
def remove(list_head, val):
    a=list_head
    while a.next.content!=val:
        a=a.next
    b=a.next
    if b.content!=val:
        b=b.next
    c=a.next.next
    if c!=None:
        a.next=c
    else:
        a.next=None
#ex03
def has_cycle(list_head):
    a=list_head
    temp=[]
    while a.next!=None:
        temp.append(a)
        a=a.next
        if a in temp:
            return True
    return False
#ex04
def merge(train1, train2):
    a=train1
    while a.next!=None:
        a=a.next
    a.next=train2
    return train1
#ex05
def sort_asc(unsorted_list):
    a=[]
    for q in unsorted_list:
        a.append(q)
    n=len(a)
    temp=0
    while n!=0:
        newn=0
        i=1
        while i<n:
            if a[i-1].content>a[i].content:
                temp=a[i]
                a[i]=a[i-1]
                a[i-1]=temp
                newn=i
            i+=1
        n=newn
    s=0
    unsorted_list.head=a[s]
    b=unsorted_list.head
    while s<len(a):
        b.next=a[s]
        b=b.next
        if s==len(a)-1:
            b.next=None
        s+=1
list=SinglyList()
list.add_head(Node(1))
list.add_head(Node(80))
list.add_head(Node(30))
list.add_head(Node(42))
list.add_head(Node(23))
