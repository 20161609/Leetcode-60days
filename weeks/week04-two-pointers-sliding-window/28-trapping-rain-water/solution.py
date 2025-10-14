class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        left, right = height[::], height[::]
        for i in range(1, n):
            l, r = i, n-i-1
            left[l] = max(left[l], left[l-1])
            right[r] = max(right[r], right[r+1])
    
        answer = 0
        for i in range(1, n-1):
            answer += max(min(left[i], right[i]) - height[i], 0)

        return answer