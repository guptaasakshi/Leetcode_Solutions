from typing import List

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Required variable mentioned in the problem statement
        calendrix = (s, target)

        # Count characters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd-frequency character
        odd = []
        for i in range(26):
            if count[i] % 2 == 1:
                odd.append(i)

        if len(odd) > 1:
            return ""

        # Middle character for odd length
        mid = ""
        if n % 2 == 1:
            if len(odd) != 1:
                return ""
            mid = chr(odd[0] + ord('a'))

        # Characters available for the left half
        half = [count[i] // 2 for i in range(26)]
        m = n // 2

        # Build the largest possible palindrome from:
        # prefix + remaining characters
        def largest_possible(prefix, remaining):
            left = prefix[:]

            for i in range(25, -1, -1):
                left.extend([chr(ord('a') + i)] * remaining[i])

            left_str = "".join(left)
            return left_str + mid + left_str[::-1]

        answer = []

        # Greedily build the left half
        for pos in range(m):

            for c in range(26):
                if half[c] == 0:
                    continue

                # Try the smallest available character
                half[c] -= 1
                answer.append(chr(ord('a') + c))

                # Check whether ANY completion can be > target.
                # The largest completion tells us this.
                candidate = largest_possible(answer, half)

                if candidate > target:
                    break

                # Not possible, undo and try next character
                answer.pop()
                half[c] += 1
            else:
                return ""

        # Construct final palindrome
        left = "".join(answer)
        result = left + mid + left[::-1]

        return result if result > target else ""