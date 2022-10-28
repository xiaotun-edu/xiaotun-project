class TreeNode(object):
    def __init__(self,val = -1,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree(object):
    def __init__(self,root=None):
        self.root=root

    def add(self,val):
        node = TreeNode(val=val)
        if self.root=None:#根节点
            self.root=node
        else:
            quene=[self.root]
            while quene:
                cur=quene.pop(0)#返回删除的元素，是个结构
                if cur.left=None:
                    cur.left=node
                    return
                else:
                    quene.append(cur.left)
                if cur.right=None:
                    cur.right=node
                    return
                else:
                    quene.append(cur.right)
    def Inordertraversal(self,root,type=1):

        #
        res=[]
        stack=[]
        cur=root
        if type ==1:
            while stack or res:
                while cur:
                   res.append(cur.val)
                   stack.append(cur)
                   cur=cur.left
                cur=stack.pop()
                cur=cur.right
            print(res)
            return  res
        elif type==2:
            while stack or res:
                while cur:
                    stack.append(cur)
                    cur=cur.left
                cur=stack.pop()
                res.append(cur.val)
                cur=cur.right
            print(res)
            return res
        elif type==3:
            while stack or res:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur=cur.right
                cur=stack.pop()
                cur.left
            print(res)
            return res[::-1]

    def mirror(self,root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)

    def maxdepth(self,root):
        if root=None:
            return 0
        left_high=self.maxdepth(root.left)
        right_high=self.maxdepth(root.right)
        return max(left_high,right_high)+1











