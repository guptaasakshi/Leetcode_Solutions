from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))  # sorted string as key
            mp[key].append(word)
        
        return list(mp.values())