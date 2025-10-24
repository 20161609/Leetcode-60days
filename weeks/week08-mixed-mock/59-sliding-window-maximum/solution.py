from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        n = len(nums)
        answer, dq = deque(), []
        for i in range(n):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()
            
            if i >= k - 1:
                answer.append(nums[dq[0]])

        return answer
