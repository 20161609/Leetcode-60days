class Solution:
    def firstUniqChar(self, s: str) -> int:
        box = {}
        abandon = set()
        for i, c in enumerate(s):
            if c in abandon:
                continue
            if not c in box:
                box[c] = i
            else:
                abandon.add(s[box.pop(c)])

        if len(box) == 0:
            return -1
        else:
            return min(box.values())