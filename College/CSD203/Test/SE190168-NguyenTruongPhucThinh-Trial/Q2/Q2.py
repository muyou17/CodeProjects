class Phone:
    def __init__(self, code, make, amount, price):
        self.code = code
        self.make = make
        self.amount = amount
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.amount}, {'%.3f' % self.price}"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class qNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enQueue(self, data):
        node = qNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def deQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data


class BSTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, data):
        self.root = BSTree.insertNode(self.root, data)

    def insertNode(node, data):
        if node is None:
            return Node(data)
        if data.code < node.data.code:
            node.left = BSTree.insertNode(node.left, data)
        elif data.code > node.data.code:
            node.right = BSTree.insertNode(node.right, data)
        return node

    def visit(self, p):
        if p is None:
            return
        print(f"{p.data}")

    def preOrder(self, p):
        if p is None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)

    def preVisit(self):
        self.preOrder(self.root)
        print()

    def inOrder(self, p):
        if p is None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)

    def inVisit(self):
        self.inOrder(self.root)
        print()

    def postOrder(self, p):
        if p is None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)

    def postVisit(self):
        self.postOrder(self.root)
        print()

    def breadth_first(self):
        if self.isEmpty():
            return
        mq = MyQueue()
        mq.enQueue(self.root)
        while not mq.isEmpty():
            p = mq.deQueue()
            self.visit(p)
            if p.left is not None:
                mq.enQueue(p.left)
            if p.right is not None:
                mq.enQueue(p.right)

    def computeHeight(self, node):
        if node is None:
            return 0
        left_height = self.computeHeight(node.left)
        right_height = self.computeHeight(node.right)
        return max(left_height, right_height) + 1

    def postOrder2(self, p):
        if p is None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if p.data.amount > 50:
            self.visit(p)

    def postVisit2(self):
        self.postOrder2(self.root)
        print()

    def deleteLeaf(self, node):
        if node is None:
            return None

        if node.left or node.right:
            node.left = self.deleteLeaf(node.left)
            node.right = self.deleteLeaf(node.right)
            return node


    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Find the height of given Binary Search Tree (BST).
            Hint:
                (1) Implement a 'computeHeight()' function to calculate the height of the tree.
                    Note: The height of an empty tree is 0 and the height of a tree with
                    single node is 0.
                (2) Recursively calculate the height of the left and the right subtrees
                    of a node and assign height to the node as max of the heights of two
                    children plus 1.
            With the data provided, the output after running this function will be:
                OUTPUT:
                3
        """
        Tree_Height = 0
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        Tree_Height += self.computeHeight(self.root)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(Tree_Height)

    # This function is used for Question 2
    def f2(self):
        """
            Question 2: Perform the Post-Order traverse on the BST, but ONLY visit nodes
            that contains Phone's amount > 50.
            Hint:
                (1) You should create 2 new functions 'postVisit2' and 'postOrder2'
                    with similar content to the two functions "postVisit" and "postOrder"
                    (available in this file) to perform the requirement.
                (2) Call the 'postVisit2' function in the f2() to perform them.
            With the data provided, the output after running these two functions will
            be:
                OUTPUT:
                100, Apple, 72, 8.540
                156, Samsung, 100, 3.555
                123, Apple, 60, 3.762

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.postVisit2()
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Insert into the current tree a new Phone which code = 111, 
            make = 'FPTPhone', amount = 10, price = k, where k is height
            of the current tree before insertion.
            Hint:
                Call the 'insert' function (available in this file) in the f3() to
                insert the new_Phone with price = float(Tree_Height in Question 1)
                into the tree.
            With the data provided, the output after running this function will be:
                OUTPUT:
                123, Apple, 60, 3.762
                110, Vivo, 10, 7.590
                100, Apple, 72, 8.540
                111, FPTPhone, 10, 2.000
                156, Samsung, 100, 3.555
                234, BPhone, 4, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.insert(Phone(111, 'FPTPhone', 10, self.computeHeight(self.root)))
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Decrease the Phone's price of root by 20 percents.
           
            With the data provided, the output after running this function will be:
                OUTPUT:
                123, Apple, 60, 3.010
                110, Vivo, 10, 7.590
                156, Samsung, 100, 3.555
                100, Apple, 72, 8.540
                234, BPhone, 4, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        if self.root:
            self.root.data.price *= 0.8

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def f5(self):
        """
            Question 5: Remove all leaf nodes from the given Binary Search Tree (BST).
            Hint:
                (1) Leaf nodes have neither left child nor right child.
                (2) Implement a 'deleteLeaf' function to remove all leaf nodes
                    from the given BST.
                (3) Call the 'deleteLeaf' function in the f5() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                123, Apple, 60, 3.762
                110, Vivo, 10, 7.590
                156, Samsung, 100, 3.555

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        self.deleteLeaf(self.root)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    tree = BSTree()
    tree.insert(Phone(123, 'Apple', 60, 3.762))
    tree.insert(Phone(156, 'Samsung', 100, 3.555))
    tree.insert(Phone(110, 'Vivo', 10, 7.590))
    tree.insert(Phone(100, 'Apple', 72, 8.540))
    tree.insert(Phone(234, 'BPhone', 4, 3.690))

    print("Do you want to run Q2?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        tree.f1()

    if n == 2:
        print("OUTPUT:")
        tree.f2()

    if n == 3:
        print("OUTPUT:")
        tree.f3()

    if n == 4:
        print("OUTPUT:")
        tree.f4()

    if n == 5:
        print("OUTPUT:")
        tree.f5()
    # end main


# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================