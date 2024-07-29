class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key


class BSTree:
    def __init__(self):
        self.root = None

    def buildBST(self, data, k):
        for i in range(k):
            self.insert(data[i])
    def insertRec(self, tmp, new_number):
        if (tmp is None):
            tmp = Node(new_number)
        elif (new_number < tmp.key):
            tmp.lChild = self.insertRec(tmp.lChild, new_number)
        elif (new_number > tmp.key):
            tmp.rChild = self.insertRec(tmp.rChild, new_number)
        return tmp

    def insert(self, new_number):
        self.root = self.insertRec(self.root, new_number)

    def height(self, parent: Node | None) -> int:
        if not parent or not parent.lChild and not parent.rChild:
            return 0

        return 1 + max(self.height(parent.lChild), self.height(parent.rChild))

    def leaf_count_higher_than_10(self, parent: Node | None) -> int:
        if not parent:
            return 0

        if not parent.lChild and not parent.rChild and parent.key > 10:
            return 1

        return (self.leaf_count_higher_than_10(parent.lChild) +
                self.leaf_count_higher_than_10(parent.rChild))

    def leaf_count(self, parent: Node | None) -> int:
        if not parent:
            return 0

        if not parent.lChild and not parent.rChild:
            return 1

        return self.leaf_count(parent.lChild) + self.leaf_count(parent.rChild)

    def leaf_sum(self, parent: Node | None) -> int:
        if not parent:
            return 0

        if not parent.lChild and not parent.rChild:
            return parent.key

        return self.leaf_sum(parent.lChild) + self.leaf_sum(parent.rChild)

    def min(self, parent: Node | None) -> int | None:
        if not parent:
            return None

        current: Node = self.root
        while current.lChild:
            current = current.lChild
        return current.key

    def max(self, parent: Node | None) -> Node | None:
        if not parent:
            return None

        current: Node = self.root
        while current.rChild:
            current = current.rChild
        return current

    def remove(self, node: Node, parent: Node | None) -> None:
        if parent:
            if node.key < parent.key:
                parent.lChild = self.remove(parent.lChild, node)
            elif node.key > parent.key:
                parent.rChild = self.remove(parent.rChild, node)
            else:
                if not parent.lChild:
                    return parent.rChild
                if not parent.rChild:
                    return parent.lChild

                min_larger_node: Node = self.min(parent.rChild)
                parent.key = min_larger_node.key
                parent.rChild = self.remove(parent.rChild, min_larger_node)
        return parent

    def preOrder(self, tmp):
        if (tmp is not None):
            print(tmp.key)
            self.preOrder(tmp.lChild)
            self.preOrder(tmp.rChild)

    def printTree1(self):
        self.preOrder(self.root)

    def inOrder(self, tmp):
        if (tmp is not None):
            self.inOrder(tmp.lChild)
            print(tmp.key)
            self.inOrder(tmp.rChild)

    def printTree2(self):
        self.inOrder(self.root)

    def postOrder(self, tmp):
        if (tmp is not None):
            self.postOrder(tmp.lChild)
            self.postOrder(tmp.rChild)
            print(tmp.key)

    def printTree3(self):
        self.postOrder(self.root)


    # ========================================================
    # This function is used for Question 1
    def f1(self):
        # value k is used to store the result
        k = 0
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        k = self.leaf_count(self.root)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(k)

    # This function is used for Question 2
    def f2(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.insert(self.height(self.root) ** 2)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.printTree2()
    
    # This function is used for Question 3
    def f3(self):
        # value k is used to store the result
        k = 0
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        k += self.min(self.root)
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(k)

    # This function is used for Question 4
    def f4(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        self.remove(self.max(self.root), self.root)

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.printTree2()


    # this function is used for Question 5
    def f5(self):
        # value k is used to store the result
        k = 0
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------

        k = f'{self.leaf_sum(self.root) / self.leaf_count(self.root):.1f}'

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(k)



def processing():
    print("Do you want to run Q2?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    t = BSTree()
    data = [20, 10, 40, 15, 30, 7, 50, 17, 34, 26, 29, 3, 8, 12, 49]
    size = int(input("Input the size of tree (amount of nodes - from 1 to 15):   "))
    while (size <1 or size >15):
        size = int(input("Please input the size of tree (amount of nodes - from 1 to 15):   "))
    t.buildBST(data, size)

    if n == 1:
        print("OUTPUT:")
        t.f1()

    if n == 2:
        print("OUTPUT:")
        t.f2()

    if n == 3:
        print("OUTPUT:")
        t.f3()

    if n == 4:
        print("OUTPUT:")
        t.f4()

    if n == 5:
        print("OUTPUT:")
        t.f5()


if __name__ == '__main__':
    processing()