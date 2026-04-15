class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in s:
            if t.count(ch) != s.count(ch):
                return False
        return True
