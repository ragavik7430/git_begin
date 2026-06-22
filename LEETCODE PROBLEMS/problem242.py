class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true