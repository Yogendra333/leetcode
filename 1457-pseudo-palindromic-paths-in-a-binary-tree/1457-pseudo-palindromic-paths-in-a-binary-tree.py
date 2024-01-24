class Solution:
    def pseudoPalindromicPaths (self, r: Optional[TreeNode]) -> int:
        def f(n, m):
            if n:
                m ^= 1<<n.val
                result = f(n.left, m) + f(n.right, m)
                if n.left == n.right:
                    result += m&(m-1) < 1
            
                return result

            return 0
        
        return f(r, 0)