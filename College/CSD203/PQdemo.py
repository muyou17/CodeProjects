class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

#My Node Class
class MyNode:
    def __init__(self, data, prev, next):   
        self.data = data
        self.prev = prev
        self.next = next

    def displayNode(self):
        print("<"+str(self.data.key)+","+self.data.value+">")


#My Priority Queue as Double Linked List Class
class MyPQ:
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.head is None:
            return True   
        return False

    def Enqueue(self, newdata):
        new_item = MyNode(newdata, None, None)
        
        if self.isEmpty():
             self.head = new_item
             self.tail = new_item         
        else:
            current = self.head
            added = False
            while current is not None:
                if current.data.key > new_item.data.key:
                    new_item.next = current
                    new_item.prev = current.prev
                    if current.prev is not None:
                        current.prev.next = new_item
                    else:
                        self.head=new_item
                    current.prev = current
                    added = True
                    break
                current = current.next 
            if not added:
                new_item.prev = self.tail
                self.tail.next = new_item
                self.tail = new_item

    def Dequeue(self):
        if self.isEmpty():
            return
        else:
            self.head.displayNode()
            self.head = self.head.next 
            if self.head is not None:
                self.head.prev = None
    
    def traversalDisplay(self):
        if self.isEmpty():
            print("List is empty")
            return
        
        current = self.head
        while current is not None:
            current.displayNode()
            current = current.next
    

# Main Program
def main():
    mypq = MyPQ()

    mypq.Enqueue(KeyValue(5,"A"))
    mypq.Enqueue(KeyValue(9,"C"))
    mypq.Enqueue(KeyValue(3,"B"))
    mypq.Enqueue(KeyValue(7,"D"))

    print("Print queue")
    mypq.traversalDisplay()

    print("Dequeue steps")
    mypq.Dequeue()
    mypq.Dequeue()
    mypq.Dequeue()
    mypq.Dequeue()

    print("Queue is empty="+str(mypq.isEmpty()))
   
if __name__ == '__main__':
    main()