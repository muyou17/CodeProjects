class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.root = None
    # Chú ý:
    # Các bước xây dựng hệ thống cân bằng cây AVL:
    # B1: Tạo hàm lấy chiều cao cây
    # B2: Tạo hàm lấy độ cân bằng của node từ hàm chiều cao từ B1
    # (Tuy theo định nghĩa độ cân bằng bằng chiều cao cây bên phải trừ cây bên trái, ta sẽ định nghĩa ngược lại để dấu của độ cân bằng
    # tương ứng vỡi phép xoay cần thực hiện. Xoay trái khi < 0, xoay phải khi > 0)
    # B3: Tạo hàm xoay trái, xoay phải để gọi trong hàm cân bằng cây ở B4.
    # B4: Tạo hàm cân bằng cây, bao gồm các trường hợp:
    # Right Rotation (xoay phải) : Xảy ra khi độ cân bằng của gốc > 1 và độ cân bằng của gốc.left >= 0
    # Left - Right Rotation (xoay trái rồi xoay phải): Xảy ra khi độ cân bằng của gốc > 1 và độ cân bằng của gốc.left < 0.
    # Left Rotation (xoay trái) : Xảy ra khi độ cân bằng của gốc < 1 và độ cân bằng của gốc.right <= 0
    # Right - Left Rotation (xoay phải rồi xoay trái): Xảy ra khi độ cân bằng của gốc < 1 và độ cân bằng của gốc.right > 0
    # B5: Làm phép insert, delete như cây BínarySearchTree nhưng có thêm bước cân bằng ở cuối
    # (Phép delete sẽ cân định nghĩa thêm một hàm get_min_value_node(node) để xử lý trường hợp xoá node có 2 con)
    def get_height(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        return a

    def rotate_right(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        return a

    def balance_tree(self, node):
        balance = self.get_balance(node)
        if balance > 1:
            #Right Rotation
            if self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            #Left - Right Rotation
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            #Left Rotation
            if self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            #Right - Left Rotation
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node

    def insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return self.balance_tree(node)

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            #Delete with 1 children
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                #Delete with 2 childrens
                temp = self.get_min_value_node(node.right)
                node.key = temp.key
                node.right = self.delete(node.right, temp.key)
        return self.balance_tree(node)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.key), end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def _insert(self, key):
        self.root = self.insert(self.root, key)

    def _delete(self, key):
        self.root = self.delete(self.root, key)


# Example usage
avl_tree = AVLTree()
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    avl_tree._insert(key)

print("Preorder traversal of the AVL tree after insertion:")
avl_tree.pre_order(avl_tree.root)
print()

avl_tree._delete(30)
print("Preorder traversal of the AVL tree after deleting 30:")
avl_tree.pre_order(avl_tree.root)