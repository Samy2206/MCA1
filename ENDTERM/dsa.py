# Q1: Complete Binary Tree with Insertion Operation
class CompleteBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)

    def print_tree(self):
        print("Complete Binary Tree:")
        level, index = 0, 0
        nodes_in_current_level = 1
        while index < len(self.tree):
            print(f"Level {level}:", end=" ")
            for _ in range(nodes_in_current_level):
                if index < len(self.tree):
                    print(self.tree[index], end=" ")
                    index += 1
            print()
            level += 1
            nodes_in_current_level *= 2

# Example usage
tree = CompleteBinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)
tree.insert(70)
tree.print_tree()

# Q2: Binary Search Tree with Insert, Search, and Delete
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        break
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        break
                    temp = temp.right

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def search_iterative(self, data):
        temp = self.root
        while temp:
            if temp.data == data:
                print(f"Element is present: {temp.data}")
                return
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        print("Element is not found")

    def delete(self, data):
        parent, current = None, self.root
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if not current:  # Node not found
            print(f"Node {data} not found in the BST.")
            return

        # Case 1: Node with no children
        if not current.left and not current.right:
            if not parent:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node with one child
        elif current.left is None or current.right is None:
            child = current.left if current.left else current.right
            if not parent:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node with two children
        else:
            successor = self.find_min(current.right)
            current.data = successor.data
            self.delete(successor.data)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

# Example usage
obj = BST()
obj.insert(10)
obj.insert(60)
obj.insert(30)
obj.insert(5)
obj.insert(90)
obj.insert(2)
print("After inorder traversal:", end=" ")
obj.inorder_traversal(obj.root)
print('\nAfter searching:', end=" ")
obj.search_iterative(100)
item = int(input("Enter item you want to delete: "))
obj.delete(item)
print(f"After deletion of {item}, inorder traversal:", end=" ")
obj.inorder_traversal(obj.root)

# Q3: Binary Search Tree with Inorder, Preorder, Postorder
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# Example usage
bst = BinarySearchTree()
root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = bst.insert(root, key)

print("Inorder traversal:")
bst.inorder(root)
print("\nPreorder traversal:")
bst.preorder(root)
print("\nPostorder traversal:")
bst.postorder(root)
