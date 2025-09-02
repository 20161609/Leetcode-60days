class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box = dict()
        front, answer = 0, 0
        for rear, c in enumerate(s):
            if not c in box:
                box[c] = rear
            else: # Duplicated
                for i in range(front, box[c]):
                    box.pop(s[i])
                front = box.pop(c) + 1
                box[c] = rear
            answer = max(answer, len(box))

        return answer