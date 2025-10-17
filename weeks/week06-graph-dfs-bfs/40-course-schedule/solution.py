from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        roots = set(range(numCourses))
        for a, b in prerequisites:
            graph[b].append(a)
            if a in roots:
                roots.remove(a)
        if not roots:
            return False

        visited, checked = set(), set()        
        def dfs(node):
            if node in visited:
                return False
            if node in checked:
                return True

            visited.add(node)
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            visited.remove(node), checked.add(node)
            return True

        for node in roots:
            if not dfs(node):
                return False
                
        return len(checked) == numCourses
