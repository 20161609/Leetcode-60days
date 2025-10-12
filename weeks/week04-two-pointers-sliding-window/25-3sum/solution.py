from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()        
        pos, neg = {}, {}
        pos_size, neg_size = 0, 0
        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1
            elif x < 0:
                if not x in neg:
                    neg[x] = 0
                neg[x] += 1
                neg_size += 1
            elif x > 0:
                if not x in pos:
                    pos[x] = 0
                pos[x] += 1
                pos_size += 1

        answer = []
        # [zero, zero, zero]
        if zeros >= 3:
            answer.append([0,0,0])
        
        # [neg, zero, pos]
        if zeros > 0:
            for x in pos:
                if -x in neg:
                    answer.append([-x, 0, x])

        # [neg, neg, pos]
        # duplicate
        for x in neg:
            if neg[x] >= 2 and (-2 * x) in pos:
                answer.append([x, x, (-2 * x)])
        # differnce
        for x,y in combinations(neg.keys(), 2):
            if (-x-y) in pos:
                answer.append([min(x,y), max(x,y), -x-y])

        # [neg, neg, pos]
        # duplicate
        for x in pos:
            if pos[x] >= 2 and (-2*x) in neg:
                answer.append([(-2 * x), x, x])
        # differnce
        for x,y in combinations(pos.keys(), 2):
            if (-x-y) in neg:
                answer.append([-x-y, min(x,y), max(x,y)])

        return answer