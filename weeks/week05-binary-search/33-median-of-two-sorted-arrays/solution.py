class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not (len(nums1) <= len(nums2)):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1

        while left <= right:
            i = (left + right) // 2
            j = (n1 + n2 + 1)//2 - i

            # Calculate min, max from left or right
            maxLeft1 = float('-inf') if i == 0 else nums1[i-1]
            minRight1 = float('inf') if i == n1 else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j-1]
            minRight2 = float('inf') if j == n2 else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Correctly separated..
                if (n1 + n2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = i - 1
            else: # maxLeft1 == minRight2
                left = i + 1
