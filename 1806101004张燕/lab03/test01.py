class BiTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_BiTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BiTNodes(t.left) + count_BiTNodes(t.right)


def sum_BiTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BiTNodes(t.left) + sum_BiTNodes(t.right)


def preorder(t):
    if t is None:
        return
    print(t.data)
    preorder(t.left)
    preorder(t.right)


def inorder(t):
    if t is None:
        return
    inorder(t.left)
    print(t.data)
    inorder(t.right)


def postorder(t):
    if t is None:
        return
    postorder(t.left)
    postorder(t.right)
    print(t.data)




class BiTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = BiTNode(data)
        else:
            self.add_helper(self.root, data)

    def add_helper(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = BiTNode(data)
            else:
                self.add_helper(node.left, data)
        elif data >= node.data:
            if node.right is None:
                node.right = BiTNode(data)
            else:
                self.add_helper(node.right, data)


if __name__ == '__main__':
    tree = BiTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)

    print(count_BiTNodes(tree.root))
    print(sum_BiTNodes(tree.root))

    inorder(tree.root)
    preorder(tree.root)
    postorder(tree.root)

deef foo(n):

