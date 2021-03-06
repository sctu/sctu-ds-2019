class BiTNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    #统计树所有节点
    def count_BiTNodes(t):
        if t is None:
            return 0
        else:
            return 1+BiTNode.count_BiTNodes(t.left)+BiTNode.count_BiTNodes(t.right)

    #对树的所有节点进行求和
    def sum_BiTNodes(t):
        if t is None:
            return 0
        else:
            return t.data+BiTNode.sum_BiTNodes(t.left)+BiTNode.sum_BiTNodes(t.right)

    #先序遍历
    def preorder(t):
        if t is None:
            return

        print(t.data,end=" ")
        BiTNode.preorder(t.left)
        BiTNode.preorder(t.right)

    #中根序遍历
    def inorder(t):
        if t is None:
            return
        BiTNode.inorder(t.left)
        print(t.data,end=" ")
        BiTNode.inorder(t.right)

    #后序遍历
    def postorder(t):
        if t is None:
            return
        BiTNode.postorder(t.left)
        BiTNode.postorder(t.right)
        print(t.data,end=" ")

class BiTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root is None:
            self.root=BiTNode(data)
        else:
            self.add_helper(self.root,data)

    def add_helper(self,node,data):
        if data<=node.data:
            if node.left is None:
                node.left=BiTNode(data)
            else:
                self.add_helper(node.left,data)
        elif data>=node.data:
            if node.right is None:
                node.right=BiTNode(data)
            else:
                self.add_helper(node.right,data)

#按照层次遍历
class Solution:
    def PrintFromTopBottom(self,root):
        outlist=[]
        queue=[]
        while queue!=0 and root:
            outlist.append(queue[0].val)
            if queue[0].left!=None:
                queue.append(queue[0].left)
            elif queue[0].right!=None:
                queue.append(queue[0].right)
            queue.pop(0)
        return outlist

if __name__=="__main__":
    tree=BiTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    tree.add(4)

    print(BiTNode.count_BiTNodes(tree.root))
    print(BiTNode.sum_BiTNodes(tree.root))

    BiTNode.preorder(tree.root)
    BiTNode.inorder(tree.root)
    BiTNode.postorder(tree.root)
