#Main method for demonstrating the use of the AVLNode and AVLTree classes to manipulate an AVL Tree
#ChatGPT helped a bit with understanding the conceptual side of the newly translated python classes
import AVLTree
import random
def main():
    #Generate a new AVL Tree with an empty root
    avlTree = AVLTree.AVLTreeClass()
    root = None
    
    #Generate random integers and add them to the AVL Tree
    valueCount = 10
    while valueCount > 0:
        #The line below was a bit of a combination of ChatGPT help and code from a previous program
        root = avlTree.insert(root, random.randint(0, 99))
        valueCount -= 1
    
    #Print the different traversal orders of the AVl Tree
    print("I have generated a set of random integers that have been placed into an AVL Tree.")
    print("Now I will ouput them in different traversal orders.")
    print("\nInorder Traversal: ")
    avlTree.inorder_traversal(root)
    print("\n\nPreorder Traversal: ")
    avlTree.preorder_traversal(root)
    print("\n\nPostorder Traversal: ")
    avlTree.postorder_traversal(root)
    print("\n")

if __name__ == "__main__":
    main()