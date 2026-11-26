class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]
        