class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dict = defaultdict(list)
        for i, pre in prerequisites:
            dict[pre].append(i)
    
        visited = set()
        stack = set()
    
        def dfs(course):
            if course in stack:
                return False
            if course in visited:
                return True
    
            stack.add(course)
            visited.add(course)
    
            for neighbor in dict[course]:
                if not dfs(neighbor):
                    return False
    
            stack.remove(course)
            return True
    
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
    
        return True