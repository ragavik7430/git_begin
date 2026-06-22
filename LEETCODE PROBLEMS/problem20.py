class Solution:
    def isValid(self, s: str) -> bool:
        m={')':'(','}':'{',']':'['}
        st=[]
        for char in s:
            if char in m.values():
                st.append(char)
            elif char in m:
                if not st or m[char]!=st.pop():
                    return False
        return not st
#Example 1:
#Input: s = "()"
#Output: true