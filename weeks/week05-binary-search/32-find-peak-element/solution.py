from collections import deque

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        front, rear = 0, n-1
        while front < rear:
            mid = (front + rear) // 2
            if nums[mid] < nums[mid+1]:
                front = mid+1
            else:
                rear = mid

        return (front+rear)//2