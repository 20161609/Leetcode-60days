from collections import deque

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)//2
        if goal*2 != sum(nums):
            return False

        dp = [1] + [0] * goal
        queue = deque()
        for num in nums:
            if num > goal:
                return False
            for x in range(goal+1):
                if dp[x-num] == 1:
                    queue.append(x)
            while queue:
                dp[queue.pop()] = 1
                if dp[goal] == 1:
                    return True
        return dp[goal] == 1
    