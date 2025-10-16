class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        front, rear = 0, n-1
        if target < nums[front]:
            return front
        elif nums[rear] < target:
            return rear + 1
        else:
            while front+1<rear and nums[front] < target < nums[rear]:
                mid = (front + rear) // 2
                if nums[mid] < target:
                    front = mid
                elif nums[mid] > target:
                    rear = mid
                else:
                    return mid

        if target <= nums[front]:
            return front
        elif nums[front] < target <= nums[rear]:
            return rear
        else:
            return rear + 1
