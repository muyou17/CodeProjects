class Juice:
    def __init__(self, code, make, unit, volume, price):
        self.code = code
        self.make = make
        self.unit = unit
        self.volume = volume
        self.price = price
    
    def __repr__(self):
        return f"{self.code}, {self.make}, {self.unit}, {self.volume}, {'%.3f' % self.price}"

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getNode(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def addFirst(self, ID, name, unit, volume, price):
        new_node = Node(Juice(ID, name, unit, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addLast(self, ID, name, unit, volume, price):
        new_node = Node(Juice(ID, name, unit, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, prev_node, new_node):
        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is None:
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
            print()

    def loadData(self):
        self.addLast('001', 'coconut', 7, '390ml', 175.0)
        self.addLast('002', 'orange', 3, '320ml', 168.0)
        self.addLast('005', 'lemon', 1, '320ml', 220.0)
        self.addLast('012', 'carrot', 6, '600ml', 218.0)
        self.addLast('025', 'strawberry', 12, '390ml', 175.0)

    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Insert at the beginning of the current list a new Juice
            with ID = '019', name = 'guava', unit = 4, volume = '390ml', price = 177.0
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                019, guava, 4, 390ml, 177.000
                001, coconut, 7, 390ml, 175.000
                002, orange, 3, 320ml, 168.000
                005, lemon, 1, 320ml, 220.000
                012, carrot, 6, 600ml, 218.000
                025, strawberry, 12, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.addFirst('019', 'guava', 4, '390ml', 177.0)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Juice('NEW', 'apple', 3, '330ml', 112.0))
        """
            Question 2: Using the new_node initialized above, write your code to insert 
            the new_node to the third position of the current list.
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                001, coconut, 7, 390ml, 175.000
                002, orange, 3, 320ml, 168.000
                NEW, apple, 3, 330ml, 112.000
                005, lemon, 1, 320ml, 220.000
                012, carrot, 6, 600ml, 218.000
                025, strawberry, 12, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        self.addAfter(self.getNode(1), new_node)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Increase the Juice's price by 20 percents for the nodes with unit < 5
            The linked list after changed is:
                OUTPUT:
                001, coconut, 7, 390ml, 175.000
                002, orange, 3, 320ml, 201.600
                005, lemon, 1, 320ml, 264.000
                012, carrot, 6, 600ml, 218.000
                025, strawberry, 12, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        current = self.head
        while current:
            if current.data.unit < 5:
                current.data.price += current.data.price * 0.2
            current = current.next
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Sort the linked list in an ascending order according to
            Juice's unit. 
            
            The linked list after change is:
                OUTPUT:
                005, lemon, 1, 320ml, 220.000
                002, orange, 3, 320ml, 168.000
                012, carrot, 6, 600ml, 218.000
                001, coconut, 7, 390ml, 175.000
                025, strawberry, 12, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        if self.head is None:
            return None

        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data.unit > q.data.unit:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        """
            Question 5: Delete the first node in the linked list with Juice's value < 600.0
            (value = unit * price)
            The linked list after change is:
                OUTPUT:
                001, coconut, 7, 390ml, 175.000
                005, lemon, 1, 320ml, 220.000
                012, carrot, 6, 600ml, 218.000
                025, strawberry, 12, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        current = self.head
        previous = None
        while current:
            value = current.data.price * current.data.unit
            if value < 600:
                if previous:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                else:
                    self.head = current.next
                    self.tail = None
                break
            else:
                previous = current
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