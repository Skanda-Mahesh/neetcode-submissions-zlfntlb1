# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None: 
            return "N" 
        queue = collections.deque([root])
        ans = []

        while queue: 
            cur = queue.popleft()

            if cur: 
                ans.append(str(cur.val))
            else:
                ans.append("N")
                continue

            if cur.left:
                queue.append(cur.left)
            else:
                queue.append(None)
            if cur.right:
                queue.append(cur.right)
            else:
                queue.append(None)
            
        string = ",".join(ans)
        print(string)
        return string
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == 'N':
            return None
        index = 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if vals[index] != 'N':
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index+= 1

            if vals[index] != 'N':
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index+= 1
        return root



