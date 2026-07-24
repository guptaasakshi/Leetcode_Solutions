from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048  # Since nums[i] <= 1500 < 2^11

        pair = [False] * MAX

        n = len(nums)

        # All possible nums[i] ^ nums[j] where i <= j
        for i in range(n):
            for j in range(i, n):
                pair[nums[i] ^ nums[j]] = True

        ans = [False] * MAX

        # (nums[i] ^ nums[j]) ^ nums[k]
        for x in range(MAX):
            if pair[x]:
                for num in nums:
                    ans[x ^ num] = True

        return sum(ans)