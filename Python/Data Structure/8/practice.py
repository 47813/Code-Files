def insert_bst(root, node):
    if root is None:
        return node

    if node.key == root.key:
        return root

    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)

    return root