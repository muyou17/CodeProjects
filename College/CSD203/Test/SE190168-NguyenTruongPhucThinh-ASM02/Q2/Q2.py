class Finery:
    def __init__(self, code, make, size, price):
        self.code = code
        self.make = make
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.size}, {'%.3f' % self.price}"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class qNode:    
    def __init__(self,data):
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
    
    def postOrder(self,p):
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

   
    # This function is used for Question 1
    def f1(self):
        """
            Question 1: Find the Height of given Binary Search Tree (BST). 
            Hint: 
                (1) Implement a function to calculate the height of the tree. 
                    Note: The height of an empty tree is 0 
                    and the height of a tree with single node is 0.
                (2) Recursively calculate the height of the left and the right subtrees 
                    of a node and assign height to the node as max of the heights of two 
                    children plus 1.
            With the data provided, the output after running this function will be:
                OUTPUT:
                2
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       

        def height(node):
            if node is None:
                return 0
            else:
                left_height = height(node.left)
                right_height = height(node.right)
                return max(left_height, right_height) + 1

        print(height(self.root))

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # This function is used for Question 2
    def f2(self):
        """
            Question 2: Perform the Post-Order traverse on the right branch of the BST, 
            but ONLY visit nodes that has Finery's size lager than 39 and less than 42.
            Hint: 
                (1) You should create 2 new functions 'postVisit2' and 'postOrder2' 
                    with similar content to the two functions "postVisit" and "postOrder" 
                    (available in this file) but only consider the 'size' as in the requirement.
                (2) Call the 'postVisit2' function in the f2() to perform them.
            With the data provided, the output after running these two functions will 
            be:
                OUTPUT:
                SK-SUR263P1, Seiko, 41, 3.555
        """  
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------      

        def postOrder2(p):
            if p is None:
                return None
            postOrder2(p.left)
            postOrder2(p.right)
            if 39 < p.data.size < 42:
                self.visit(p)

        postOrder2(self.root.right)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    # This function is used for Question 3
    def f3(self):
        """
            Question 3: Insert into the current tree a new Finery which code = 'NEWNODE', 
            make = 'Orient', size = 10*k*k, price = k+3, where k is height of the 
            current tree before insertion. 
            Hint:  
                Call the 'insert' function (available in this file) in the f3() to 
                insert the new_Finery with the suitable information. 
       
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                CT-CA7060-88L, Citizen, 42, 8.540
                NEWNODE, Orient, 40, 6.000
                SK-SUR263P1, Seiko, 41, 3.555
                SK-SUR211P1, Seiko, 42, 3.690
      
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        def height(node):
            if node is None:
                return 0
            else:
                left_height = height(node.left)
                right_height = height(node.right)
                return max(left_height, right_height) + 1

        k = height(self.root)
        self.insert(Finery('NEWNODE', 'Orient', 10 * k * k, k + 3))

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def f4(self):
        """
            Question 4: Increase the Citizen Finery's price by 20 percents.
            Hint: 
                (1) You should create a new function 'updateFinery' which body is similar 
                    to the function 'breadth_first' (provided in this file already) for 
                    doing BFS.
                (2) Call the 'updateFinery' function in the f4() to perform it .
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 9.108
                SK-SUR263P1, Seiko, 41, 3.555
                CT-CA7060-88L, Citizen, 42, 10.248
                SK-SUR211P1, Seiko, 42, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        def updateFinery(node):
            if node is None:
                return None
            if node.data.make == 'Citizen':
                node.data.price *= 1.2

            updateFinery(node.left)
            updateFinery(node.right)

        updateFinery(self.root)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def f5(self):
        """
            Question 5: Remove all leaf nodes for the left branch of the given BST.
            Hint: 
                (1) Leaf nodes have no children.
                (2) Implement a 'deleteLeaf' function to remove the leaf nodes.
                (3) Call the 'deleteLeaf' function in the f5() with the suitable input 
                to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                SK-SUR263P1, Seiko, 41, 3.555
                SK-SUR211P1, Seiko, 42, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        def deleteLeaf(node):
            if node is None:
                return None
            if node.left is None and node.right is None:
                return None

            node.left = deleteLeaf(node.left)
            node.right = deleteLeaf(node.right)
            return node

        self.root.left = deleteLeaf(self.root.left)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()
        
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    tree = BSTree()
    tree.insert(Finery('OR-FUNG8003D0', 'Orient', 40, 3.762))
    tree.insert(Finery('SK-SUR263P1', 'Seiko', 41, 3.555))
    tree.insert(Finery('CT-BM7466-81H', 'Citizen', 40, 7.590))
    tree.insert(Finery('CT-CA7060-88L', 'Citizen', 42, 8.540))
    tree.insert(Finery('SK-SUR211P1', 'Seiko', 42, 3.690)) 
    
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

    if n ==2:
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