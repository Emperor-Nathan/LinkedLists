class Node:
    def __init__(self, value, next=None):
        self.data=value
        self.next=next
class Stack:
    def __init__(self):
        self.bot=None
        self.top=None
    def __iter__(self):
        c=self.top
        while c:
            yield c
            c=c.next
    def isEmpty(self):
        if self.bot==None:
            return True
        return False
    def push(self, data):
        a=Node(data)
        if self.isEmpty():
            self.top=a
            self.bot=a
        else:
            a.next=self.top
            self.top=a
    def pop(self):
        a=self.top
        b=a.next
        a.next==None
        self.top=b
    def peek(self):
        return self.top.data
    def size(self):
        n=0
        x=self.top
        while x!=None:
            n+=1
            x=x.next
        return n
    def __str__(self):
        s=''
        for x in self:
            s+=str(x.data)
            if x.next!=None:
                s+='\n'
        return s
list=Stack()
list.push(42)
list.push(23)
list.push(1)
list.push(30)
list.push(89)
