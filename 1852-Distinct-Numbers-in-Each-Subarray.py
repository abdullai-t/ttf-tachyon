    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        arr =[]
        tracker = {}
        for x in nums[:k]:
            if tracker.get(x, None):
                tracker[x] +=1
            else:
                tracker[x] = 1
        
        arr.append(len(tracker.keys()))
       

        for index in range(k,len(nums)):
            tracker[nums[index - k]] -= 1
            if tracker[nums[index - k]] <= 0:
                del tracker[nums[index - k]]

            if tracker.get(nums[index], None):
                tracker[nums[index]] +=1
            else:
                tracker[nums[index]] = 1
            arr.append(len(tracker.keys()))
        
        return arr

