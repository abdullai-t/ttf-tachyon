class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = max_sum = sum(nums[:k])
        for num in range(len(nums[k:])):
            window_sum  = ((window_sum)-nums[num]+ nums[num+k])
            max_sum = max(window_sum, max_sum)
        return max_sum/k
