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
            print(node.data)
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data)

    def levelOrder(self, node):
        if node is None:
            return

        Q = queue.Queue()
        Q.put(node)

        while not Q.empty():
            node = Q.get()
            print(node.data, end=" ")

            if node.left is not None:
                Q.put(node.left)
            if node.right is not None:
                Q.put(node.right)


    def getNodeCount(self, node):
        count = 0
        if node is not None:
            count = 1 + self.getNodeCount(node.left) + self.getNodeCount(node.right)

        return count

    def isExternal(self, node):
        return node.left is None and node.right is None

    def getLeafCount(self, node):
        count = 0
        if node is not None:
            if self.isExternal(node):
                return 1
            else:
                count = self.getLeafCount(node.left) + self.getLeafCount(node.right)
            return count

    def getHeight(self, node):
        if node is None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1