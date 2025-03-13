#Used ChatGPT for a quick translation from java to python

#Provides methods for basic AVL tree operations
import AVLNode
class AVLTreeClass:
    # Get the height of the node
    def height(self, node):
        return 0 if node is None else node.height

    # Calculate balance factor of the node
    def get_balance(self, node):
        return 0 if node is None else self.height(node.left) - self.height(node.right)

    # Right rotate subtree rooted with y
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        # Return new root
        return x

    # Left rotate subtree rooted with x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        # Return new root
        return y

    # Insert a node into the AVL tree and balance it
    def insert(self, node, key):
        # Perform normal BST insertion
        if node is None:
            return AVLNode.AVLNodeClass(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node  # Duplicate keys are not allowed

        # Update height of this ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Get the balance factor
        balance = self.get_balance(node)

        # If the node is unbalanced, then there are 4 cases
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  # Return the (unchanged) node pointer

    # Inorder traversal of the AVL tree
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    # Preorder traversal of the AVL tree
    def preorder_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # Postorder traversal of the AVL tree
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=" ")
