class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(li):
            if len(li)==0:
                return [[]]
            first=li[0]
            rest=li[1:]
            all_perm=[]
            perm_w_f=recursion(rest)
            for perm in perm_w_f:
                for i in range(len(perm)+1):
                    new=perm[:i]+[first]+perm[i:]
                    all_perm.append(new)
            return all_perm
        return recursion(nums)