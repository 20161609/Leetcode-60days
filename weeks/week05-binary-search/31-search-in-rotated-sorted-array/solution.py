class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        front, rear = 0, n-1
        if nums[front] > nums[rear]:
            while front+1 < rear:
                mid = (front+rear)//2
                if nums[mid] < nums[front]:
                    rear = mid
                elif nums[mid] > nums[rear]:
                    front = mid
            front, rear = rear, front+n

        if nums[front] == target:
            return front
        elif nums[rear%n] == target:
            return rear%n
        else:
            while front+1 < rear:
                mid = (front+rear)//2
                if nums[mid%n] < target:
                    front = mid
                elif nums[mid%n] > target:
                    rear = mid
                else:
                    return mid % n

        return -1