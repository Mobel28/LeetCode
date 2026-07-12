class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_dict={num:i+1 for i,num in enumerate(sorted(set(arr)))}
        return [sorted_dict[num] for num in arr]