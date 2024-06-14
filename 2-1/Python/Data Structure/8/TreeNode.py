import queue

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, node):
        if node is not None:
            print(f"[{node.data}]", end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(f"[{node.data}]", end=" ")
            self.inOrder(node.right)
    
    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(f"[{node.data}]", end=" ")

    def levelOrder(self, node):
        if node is None:
            return

        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print(f"[{node.data}]", end=" ")

            if node.left is not None:
                Q.put(node.left)

            if node.right is not None:
                Q.put(node.right)

    def getNodeCount(self, node):
        count = 0
        if node != None:
            count = 1 + self.getNodeCount(node.left) \
                      + self.getNodeCount(node.right)
        return count
    
    def isExternal(self, node):
        return node.left == None and node.right == None
    
    def getLeafCount(self, node):
        count = 0
        if node != None:
            if self.isExternal(node):
                return 1
            else:
                count = self.getLeafCount(node.left) + self.getLeafCount(node.right)
        return count

    def getHeight(self, node):
        if node == None:
            return 0
        
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1


if __name__ == "__main__":
    T = BinaryTree()
    
    N4 = TreeNode("D")
    N5 = TreeNode("E")
    N6 = TreeNode("F")
    N2 = TreeNode("B", N4, N5)
    N3 = TreeNode("C", N6)
    N1 = TreeNode("A", N2, N3)
    T.root = N1

    print("Pre:  ", end=""); T.preOrder(T.root); print()
    print("In:   ", end=""); T.inOrder(T.root); print()
    print("Post: ", end=""); T.postOrder(T.root); print()
    print("Level:", end=""); T.levelOrder(T.root); print()

    print(f"Number of Nodes : {T.getNodeCount(N1)}")
    print(f"Number of Leaves: {T.getLeafCount(N1)}")
    print(f"Number of Height: {T.getHeight(N1)}")

