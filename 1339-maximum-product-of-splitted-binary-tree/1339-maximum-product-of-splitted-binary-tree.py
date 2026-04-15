class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        self.max_product = 0
        
        # Step 2: compute subtree sums and max product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            curr_sum = node.val + left + right
            
            # product after split
            self.max_product = max(
                self.max_product,
                curr_sum * (total - curr_sum)
            )
            
            return curr_sum
        
        dfs(root)
        
        return self.max_product % MOD