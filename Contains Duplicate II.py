class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers_tracker = {}
        for index, num in enumerate(nums):
            if num in numbers_tracker and index - numbers_tracker[num] <=k:
                return True
            numbers_tracker[num] = index

        return False
