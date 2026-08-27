from typing import List

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Required by the problem statement
        quinorath = (s, target)

        n = len(s)

        # Count frequency of characters in s
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Try to match target from left to right
        matched = 0

        while matched < n:
            idx = ord(target[matched]) - ord('a')

            if count[idx] == 0:
                break

            count[idx] -= 1
            matched += 1

        # Start from the first unmatched position.
        # If the whole target was matched, start from the end
        # because the answer must be strictly greater.
        start = matched if matched < n else n - 1

        # Backtrack from right to left
        for i in range(start, -1, -1):

            # If this position was previously matched,
            # put its character back into the available characters
            if i < matched:
                idx = ord(target[i]) - ord('a')
                count[idx] += 1

            # Find the smallest available character > target[i]
            target_idx = ord(target[i]) - ord('a')

            for j in range(target_idx + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    # Prefix remains equal to target[:i]
                    result = target[:i] + chr(j + ord('a'))

                    # Add remaining characters in sorted order
                    for k in range(26):
                        if count[k] > 0:
                            result += chr(k + ord('a')) * count[k]

                    return result

        return ""