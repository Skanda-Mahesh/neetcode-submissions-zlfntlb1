# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root]) if root is not None else collections.deque()

        while q:
            cur = None
            for _ in range(len(q)):
                cur = q.popleft()
                q.append(cur.left) if cur.left is not None else None
                q.append(cur.right) if cur.right is not None else None
            res.append(cur.val)

        return res