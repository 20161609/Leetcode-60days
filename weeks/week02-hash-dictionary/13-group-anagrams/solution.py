from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        answer = defaultdict(list)
        for i in range(n):
            answer["".join(sorted(strs[i]))].append(strs[i])

        return list(answer.values())