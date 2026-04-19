class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        from functools import lru_cache
        
        # Get the 7 cell indices visited by the path
        def get_path_indices(directions):
            row, col = 0, 0
            indices = [row * 4 + col]  # starting cell
            for d in directions:
                if d == 'D':
                    row += 1
                else:
                    col += 1
                indices.append(row * 4 + col)
            return indices  # length 7
        
        path = get_path_indices(directions)
        
        def count_up_to(n):
            # Pad n to 16 digits
            s = str(n).zfill(16)
            digits = [int(c) for c in s]
            
            # path_pos: which of the 7 path digits we're tracking
            # last_path_digit: last digit seen along path (-1 if none yet)
            # tight: whether we're still bounded by n
            # started: whether we've placed a non-zero digit yet (for leading zeros)
            
            @lru_cache(maxsize=None)
            def dp(pos, last_path_digit, tight, started):
                if pos == 16:
                    return 1 if started else 0  # must be a valid number
                
                limit = digits[pos] if tight else 9
                result = 0
                
                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    
                    if not started and d == 0:
                        # Still leading zeros, treat as blank
                        result += dp(pos + 1, last_path_digit, new_tight, False)
                    else:
                        # Check if this position is on the path
                        if pos in path:
                            # This digit must be >= last_path_digit
                            if last_path_digit != -1 and d < last_path_digit:
                                continue
                            result += dp(pos + 1, d, new_tight, True)
                        else:
                            result += dp(pos + 1, last_path_digit, new_tight, True)
                
                return result
            
            ans = dp(0, -1, True, False)
            dp.cache_clear()
            return ans
        
        return count_up_to(r) - count_up_to(l - 1)