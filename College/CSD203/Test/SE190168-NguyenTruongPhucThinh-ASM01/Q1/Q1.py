class Beverage :
    def __init__(self, code, brand, unit, volume, price):
        self.code = code
        self.brand = brand
        self.unit = unit
        self.volume = volume
        self.price = price
    
    def __repr__(self):
        return f"{self.code}, {self.brand}, {self.unit}, {self.volume}, {'%.3f' % self.price}"

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def addFirst(self, code, brand, unit, volume, price):
        new_node = Node(Beverage(code, brand, unit, volume, price))

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def addLast(self, code, brand, unit, volume, price):
        new_node = Node(Beverage (code, brand, unit, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, prev_node, new_node):
        if prev_node is None:
            return None

        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is None:
            self.head = new_node

    def addAfterThird(self, new_node):
        third_node = self.get_node(2)
        self.addAfter(third_node, new_node)

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
            print()

    def loadData(self):
        self.addLast('PS021', 'Pepsi', 'Carton of 24 bottles', '390ml', 175.0)
        self.addLast('MD033', 'Mirinda', 'Carton of 24 cans', '320ml', 168.0)
        self.addLast('SP005', 'Schweppes', 'Carton of 24 cans', '320ml', 220.0)
        self.addLast('2C017', 'Coca-Cola', 'Carton of 24 bottles', '600ml', 218.0)
        self.addLast('MD020', 'Mirinda', 'Carton of 24 bottles', '390ml', 175.0)
    
    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Insert at the beginning of the current list a new Beverage  which 
            code = NEWNODE, brand = '7-Up', unit = 'Carton of 24 cans', volume = '330ml', price = 168.0  
            Hint: 
                (1) Implement an 'addFirst' function that inserts a new Beverage  
                    into the current list's first position.
                (2) Call the 'addFirst' function in the f1() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                NEWNODE, 7-Up, Carton of 24 cans, 330ml, 168.000 
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000 
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000 
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000 
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000 
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000 
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.addFirst('NEWNODE', '7-Up', 'Carton of 24 cans', '330ml', 168.0)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Beverage('SR007', 'Sprite', 'Carton of 24 bottles', '390ml', 112.0))
        """
            Question 2: Using the new_node initialized above, write your code to insert 
            the new_node after the third node (which index is 2) of the current list.
            Hint: 
                (1) Use the 'get_node' function given in this file to find the 
                    third_node (which index is 2).
                (2) Implement an 'addAfter' function with 2 parameters new_node, 
                    third_node above to insert new_node after third_node.
				(3)	Call the 'addAfter' function in the f2() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                NEWNODE, Sprite, Carton of 24 bottles, 390ml, 112.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.addAfterThird(new_node)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Find the last node in the linked list that has Beverage 's brand
            start with 'M', if such a node is found, then set the price of Beverage  in
            this node to 999.0.
            Hint:
                (1) Use str.startswith(start) to find the last node in a linked list
                    whose Beverage 's brand begins with 'M'
                (2) Update the node's Beverage  price to 999.0
            Example: if the linked list before change is
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 159.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 999.000
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        current = self.head
        last_m = None

        while current:
            if current.data.brand.startswith('M'):
                last_m = current
            current = current.next

        if last_m:
            last_m.data.price = 999.0

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Remove the first node, then sort the linked list in an ascending 
            order according to Beverage 's price.
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        

        if self.head is not None:
            self.head = self.head.next

        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next

        nodes.sort(key=lambda beverage: beverage.price)

        self.head = None
        self.tail = None
        for beverage in nodes:
            self.addLast(beverage.code, beverage.brand, beverage.unit, beverage.volume, beverage.price)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        """
            Question 5: Delete all nodes in the linked list with Beverage 's brand = 'Mirinda'.
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        

        prev = None
        current = self.head

        while current:
            if current.data.brand == 'Mirinda':
                if prev:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                else:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None
                current = current.next
            else:
                prev = current
                current = current.next

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    lst = LinkedList()
    lst.loadData()
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n ==2:
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