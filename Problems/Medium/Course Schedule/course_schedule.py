class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        schedule = []
        while q:
            course = q.popleft()
            schedule.append(course)
            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        return len(schedule) == numCourses
            
