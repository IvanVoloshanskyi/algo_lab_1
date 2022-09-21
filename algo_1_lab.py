class Node(object):
    def __init__(self, key: int = None):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1


class AvlTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_node(key, self.root)

    def insert_node(self, key, node):

        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert_node(key, node.left)
        else:
            node.right = self.insert_node(key, node.right)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        return self.set_balance(key, node)

    def set_balance(self, key, node):

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            print("Left left situation")
            return self.right_rotate(node)
        if balance < -1 and key > node.right.key:
            print("Right Right situation")
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            print("Left Right ")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            print("Right Left ")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def print_t(self):
        if self.root:
            self.print_tree(self.root)

    def print_tree(self, node):
        if node.left:
            self.print_tree(node.left)

        if node.right:
            self.print_tree(node.right)

        print(node.key)

    def right_rotate(self, node):
        print("Right rotate...", )

        new_right_child = node.left
        right_child = new_right_child.right

        new_right_child.right = node
        node.left = right_child

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_right_child.height = max(self.get_height(new_right_child.left), self.get_height(new_right_child.right)) + 1

        return new_right_child

    def left_rotate(self, node):
        print("Left rotate...", node.key)

        new_left_child = node.right
        right_child = new_left_child.left

        new_left_child.left = node
        node.right = right_child

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        new_left_child.height = max(self.get_height(new_left_child.left), self.get_height(new_left_child.right)) + 1

        return new_left_child


avl = AvlTree()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.print_t()

