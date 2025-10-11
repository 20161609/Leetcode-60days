class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        cur = 0
        for i in range(1, len(nums)):
            if nums[cur] < nums[i]:
                cur += 1
                nums[cur] = nums[i]
            if nums[cur] == nums[-1]:
                break
                
        return cur+1
