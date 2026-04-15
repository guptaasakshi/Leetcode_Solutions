class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (char, count)

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])

            # Remove if count reaches k
            if stack[-1][1] == k:
                stack.pop()

        # Build result string
        result = ""
        for ch, count in stack:
            result += ch * count

        return result