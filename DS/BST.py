class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = node(data)
        if self.root == None:
            self.root = newNode
        else:
            temp = self.root
            while True:
                if data > temp.data:
                    if temp.right == None:
                        temp.right = newNode
                        break
                    else:
                        temp = temp.right
                else:
                    if temp.left == None:
                        temp.left = newNode
                        break
                    else:
                        temp = temp.left

    def search(self, data):
        if self.root == None:
            print("Empty Tree")
        else:
            temp = self.root
            while temp != None:
                if temp.data == data:
                    print("Element is Present")
                    return
                else:
                    if data > temp.data and temp.right != None:
                        temp = temp.right
                    elif data < temp.data and temp.left != None:
                        temp = temp.left
                    else:
                        print("Element is not Present")
                        temp = None

    def inorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            stack = []
            temp = self.root
            result = []
            while temp or stack:
                while temp:
                    stack.append(temp)
                    temp = temp.left
                temp = stack.pop()
                result.append(temp.data)
                temp = temp.right
            print(result)

    def preorder(self):
        stack = [self.root]
        result = []
        while stack:
            temp = stack.pop()
            result.append(temp.data)

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)

        print(result)

    def postorder(self):
        if self.root == None:
            print("Empty Tree")
        else:
            stack1 = [self.root]
            stack2 = []
            result = []
            while stack1:
                temp = stack1.pop()
                stack2.append(temp)

                if temp.left:
                    stack1.append(temp.left)

                if temp.right:
                    stack1.append(temp.right)

            while stack2:
                result.append(stack2.pop().data)
            print(result)

    def delete_iterative(self, data):
        if not self.root:
            print("Empty Tree")
            return

        parent = None
        current = self.root

        # Find the node and its parent
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if not current:
            print("Element not found")
            return

        # Case 1: Node with no children
        if not current.left and not current.right:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: Node with two children
        elif current.left and current.right:
            successor = self.get_min(current.right)
            val = successor.data
            self.delete_iterative(successor.data)
            current.data = val

        # Case 3: Node with one child
        else:
            child = current.left if current.left else current.right
            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    # Recursive deletion (commented as requested)
    # def delete_recursive(self, node, data):
    #     if not node:
    #         return node
    #     if data < node.data:
    #         node.left = self.delete_recursive(node.left, data)
    #     elif data > node.data:
    #         node.right = self.delete_recursive(node.right, data)
    #     else:
    #         if not node.left:
    #             return node.right
    #         elif not node.right:
    #             return node.left
    #         temp = self.get_min(node.right)
    #         node.data = temp.data
    #         node.right = self.delete_recursive(node.right, temp.data)
    #     return node

# Test the implementation
t = BST()
t.insert(10)
t.insert(8)
t.insert(12)
t.insert(11)
t.insert(14)
print("Inorder traversal before deletion:")
t.inorder()
t.delete_iterative(12)
print("Inorder traversal after deleting 12:")
t.inorder()
t.search(12)
