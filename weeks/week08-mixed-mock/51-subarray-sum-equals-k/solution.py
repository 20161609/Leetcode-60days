from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        box = defaultdict(int)
        box[0] = 1
        answer, prev = 0, 0
        for num in nums:
            prev += num
            answer += box[prev-k]
            box[prev] += 1

        return answer