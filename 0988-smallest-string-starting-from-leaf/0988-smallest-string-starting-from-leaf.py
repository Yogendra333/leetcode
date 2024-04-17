class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None

        def dfs(root,curr):
            nonlocal ans
            if not root:
                return 

            curr=chr(root.val + ord('a'))+curr
            if not root.left and not root.right:
                if not ans or curr<ans:
                    ans = curr
            dfs(root.left,curr)
            dfs(root.right,curr)

        dfs(root,"")
        return ans
        