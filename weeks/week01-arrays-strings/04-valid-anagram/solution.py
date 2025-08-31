class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        box = {}
        for c in s:
            if not c in box:
                box[c] = 0
            box[c] += 1
        
        for c in t:
            if not c in box:
                return False
            
            box[c] -= 1
            if box[c] == 0:
                box.pop(c)
        
        return len(box) == 0