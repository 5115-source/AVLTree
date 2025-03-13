#Used ChatGPT for a quick translation from java to python

#Represents a single node in the AVL tree
class AVLNodeClass:
    def __init__(self, data):
        self.key = data
        self.height = 1  # Height of leaf node is 1
        self.left = None
        self.right = None
