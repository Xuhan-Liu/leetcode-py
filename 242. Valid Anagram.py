class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = dict()
        for i in range(len(s)):
            val = map.get(s[i], 0)
            map[s[i]] = val + 1
        for j in range(len(t)):
            val = map.get(t[j], 0)
            if val == 0:
                return False
            map[t[j]] = val - 1
        return True
