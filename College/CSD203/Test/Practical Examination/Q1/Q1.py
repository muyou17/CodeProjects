class Drink:
    def __init__(self, code, make, amount, volume, price):
        self.code = code
        self.make = make
        self.amount = amount
        self.volume = volume
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.amount}, {self.volume}, {'%.3f' % self.price}"


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count: int = 0
        cursor: Node = self.head
        while cursor:
            count += 1
            cursor = cursor.next
        return count

    def getIndex(self, node) -> int | None:
        index: int = 0
        cursor: Node = self.head
        while cursor:
            if cursor == node:
                return index
            cursor = cursor.next
            index += 1

    def getNode(self, index: int) -> Node | None:
        if index < 0:
            index += len(self)
        cursor: Node = self.head
        while cursor:
            if self.getIndex(cursor) == index:
                return cursor
            cursor = cursor.next

    def addFirst(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addLast(self, code, make, amount, volume, price):
        new_node = Node(Drink(code, make, amount, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addBefore(self, node, index):
        before: Node = self.getNode(index - 1)
        print(before)
        if not self.head:
            self.head = node
            self.tail = node
        elif index == 0:
            self.addFirst(node)
        else:
            cursor: Node = self.head
            while cursor:
                if cursor == before:
                    node.next = cursor.next
                    cursor.next = node
                    return None
                cursor = cursor.next

    def removeLast(self):
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                cursor: Node = self.head
                while cursor.next.next:
                    cursor = cursor.next
                self.tail = cursor
                cursor.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            print()

    def loadData(self, size):
        data = ['PS021', 'Pepsi', 10, '390ml', 10,
                'MD033', 'Mirinda', 45, '320ml', 12,
                'SP005', 'Schweppes', 8, '320ml', 10,
                '2C017', 'Coca-Cola', 20, '600ml', 15,
                'MD029', 'Mirinda', 14, '390ml', 18,
                'SP002', 'Bohuc', 18, '320ml', 12,
                '2C014', 'Teaplus', 23, '600ml', 12,
                'MD026', 'Soda', 16, '390ml', 15,
                '2C018', 'C2', 23, '600ml', 12,
                'MD020', 'Lavie', 16, '330ml', 6]
        for i in range(size):
            self.addLast(data[5*i], data[5*i+1], data[5*i+2], data[5*i+3], data[5*i+4])

    # This function is used for Question 1
    def f1(self):
        S1 = Drink('2C014', 'Coca-Cola', 10, '600ml', 12)
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        cursor = self.head
        while cursor:
            if cursor.data.code == S1.code:
                return None
            cursor = cursor.next

        self.addFirst(S1)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Drink('NEWNODE', 'Sprite', 15, '390ml', 12))
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        self.addBefore(new_node, -1)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        # We use t to store the Drink object with maximum amount
        t = None
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        t = self.head.data
        cursor = self.head
        while cursor:
            if t.amount < cursor.data.amount:
                t = cursor.data
            cursor = cursor.next

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(t, end=' ')

    # This function is used for Question 4
    def f4(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        self.removeLast()

        if self.head is None:
            return None

        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data.price > q.data.price:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        # We use t to store the Drink object satisfying the requirement  
        t = None
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        value: float = float('inf')
        cursor: Node = self.head
        while cursor:
            pivot: Node = self.head
            lvalue: float = 0
            rvalue: float = 0
            while pivot != cursor:
                lvalue += pivot.data.amount
                pivot = pivot.next
            pivot = pivot.next
            while pivot:
                rvalue += pivot.data.amount
                pivot = pivot.next
            difference: float = abs(lvalue - rvalue)
            if difference < value:
                value = difference
                t = cursor.data
            cursor = cursor.next
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(t, end=' ')


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))
    
    lst = LinkedList()
    size = int(input("Input the size of list (amount of nodes - from 1 to 10):\nsize =   "))
    while (size < 1 or size > 10):
        size = int(input("Please input the size of list (amount of nodes - from 1 to 10):\nsize =   "))
    lst.loadData(size)
    

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n == 2:
        print("OUTPUT:")
        lst.f2()

    if n == 3:
        print("OUTPUT:")
        lst.f3()

    if n == 4:
        print("OUTPUT:")
        lst.f4()

    if n == 5:
        print("OUTPUT:")
        lst.f5()


# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================