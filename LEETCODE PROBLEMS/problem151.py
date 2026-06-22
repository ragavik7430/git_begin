class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
#Example 1:
#Input: s = "Hello World"
#Output: "World Hello"