from functools import lru_cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return nums[i]

            take_left = nums[i] - dfs(i + 1, j)
            take_right = nums[j] - dfs(i, j - 1)

            return max(take_left, take_right)

        return dfs(0, len(nums) - 1) >= 0