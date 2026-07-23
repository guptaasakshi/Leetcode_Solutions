from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return n

        bits = max(nums).bit_length()
        return 1 << bits