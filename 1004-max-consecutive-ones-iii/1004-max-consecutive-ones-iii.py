class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):
            # Expand window: add current element
            if nums[right] == 0:
                zeros += 1
            
            # Contract window: remove elements from left until valid
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update maximum length found so far
            max_length = max(max_length, right - left + 1)
        return max_length