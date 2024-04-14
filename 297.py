# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        res = ""
        my_q = deque()
        my_q.append(root)
        while my_q:
            curr = my_q.popleft()
            if curr:
                res += str(curr.val)+"#"
                my_q.append(curr.left)
                my_q.append(curr.right)
            else:
                res+="None#"
        print(res)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        n=len(data)
        if n==0:
            return None
        data=data.split("#")
        t=root=TreeNode(data[0])
        data.pop()
        q=deque([root])
        i=1
        while q:
            node=q.popleft()
            s=data[i]
            if s!='None':
                node.left=TreeNode(s)
                q.append(node.left)
            else:
                node.left=None
            i+=1
            s=data[i]
            if s!='None':
                node.right=TreeNode(s)
                q.append(node.right)
            else:
                node.right=None  
            i+=1
        return t
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))