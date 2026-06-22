class Solution:
    def isPalindrome(self, s):
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]
#Example 1:
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
