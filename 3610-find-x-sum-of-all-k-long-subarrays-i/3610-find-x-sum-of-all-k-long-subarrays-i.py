class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        i=0
        j=k
        res=[]
        print(nums[i:j])
        while j<=len(nums):
            sub=nums[i:j]
            dic={}
            for num in sub:
                dic[num]=dic.get(num,0)+1
            sort=sorted(dic.items(),key=lambda x: (-x[1],-x[0]))
            s=0
            cnt=0
            for key,val in sort:
                s+=key*val
                cnt+=1
                if cnt==x:
                    break
            res.append(s)
            i+=1
            j+=1
        return res