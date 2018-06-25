class Node:
    def __init__(self, value, next=None):
        self.data=value
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.back=None
    def __iter__(self):
        c=self.back
        while c:
            yield c
            c=c.next
    def isEmpty(self):
        if self.front==None:
            return True
        else:
            return False
    def enqueue(self, data):
        a=Node(data)
        a.next=self.back
        self.back=a
    def dequeue(self):
        a=self.back
        while a.next!=None:
            a=a.next
        a.next=None
        self.front=a
    def front(self):
        return self.front
    def size(self):
        n=0
        a=self.back
        while a!=None:
            a=a.next
            n+=1
        return n
    def __str__(self):
        s=''
        for x in self:
            s+=str(x.data)
            if x.next!=None:
                s+='\n'
        return s
list=Queue()
list.enqueue(42)
list.enqueue(23)
list.enqueue(1)
list.enqueue(30)
list.enqueue(89)
