class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tot=0
        m_val=float('inf')
        strt=0
        for i in range(len(nums)):
            tot+=nums[i]
            while tot>=target:
                m_val=min(m_val,i-strt+1)
                tot-=nums[strt]
                strt+=1
        return m_val if m_val!=float('inf') else 0