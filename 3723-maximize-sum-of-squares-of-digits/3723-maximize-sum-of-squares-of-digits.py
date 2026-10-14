class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        result = []

        while num > 0:
            digit = min(9, sum)
            result.append(str(digit))
            sum -= digit
            num -= 1

        return "".join(result)