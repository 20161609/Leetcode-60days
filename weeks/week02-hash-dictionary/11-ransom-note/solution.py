class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        box = {}
        for c in ransomNote:
            if not c in box:
                box[c] = 0
            box[c] += 1
        for c in magazine:
            if c in box:
                box[c] -= 1
                if box[c] == 0:
                    box.pop(c)
                    if len(box) == 0:
                        return True
        
        return False