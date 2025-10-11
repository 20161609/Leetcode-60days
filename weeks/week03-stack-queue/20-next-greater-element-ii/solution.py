# Paste your final accepted LeetCode solution here
from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = deque([])        
        for i in range(n*2):
            i %= n
            while stack and nums[stack[-1]] < nums[i]:
                answer[stack.pop()] = nums[i]
            stack.append(i)
        return answer
