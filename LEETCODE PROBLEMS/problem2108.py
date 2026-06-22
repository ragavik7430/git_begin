class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=1
        for i in words:
            if i==i[::-1]:
                f=0
                return i
        if f==1:
            return ""
           
#Example 1:
#Input: words = ["abc","car","ada","racecar","cool"]
#Output: "ada"