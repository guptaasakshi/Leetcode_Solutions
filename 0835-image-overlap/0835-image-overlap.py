class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        size = len(A) - 1
        largest_overlap = 0
        for i in range(2 * size + 1):
            for j in range(2 * size + 1):
                i = size - i if i > size else i
                j = size - j if j > size else j
                overlap = 0
                for x in range(size + 1):
                    for y in range(size + 1):
                        if 0 <= x + i <= size and 0 <= y + j <= size and A[x][y] and A[x][y] == B[x+i][y+j]:
                            overlap += 1
                largest_overlap = max(largest_overlap, overlap)
        return largest_overlap