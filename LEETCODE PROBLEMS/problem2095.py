class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m_w=0
        for i in accounts:
            w=0
            for m in i:
                w+=m
            m_w= max(m_w,w)
        return m_w
#Example 1:
#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6