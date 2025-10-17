from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        try:
            wordList.index(endWord)
        except:
            return 0

        box = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                box[word[:i:]+'*'+word[i+1::]].append(word)

        queue, visited = deque([(beginWord, 1)]), set([beginWord])
        while queue:
            word, depth = queue.popleft()
            if word == endWord:
                return depth
            
            for i in range(len(word)):
                for nxt in box[word[:i:]+'*'+word[i+1::]]:
                    if not nxt in visited:
                        queue.append((nxt, depth + 1))
                        visited.add(nxt)
        return 0