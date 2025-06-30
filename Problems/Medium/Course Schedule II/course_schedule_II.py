class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        schedule = []
        while q:
            course = q.popleft()
            schedule.append(course)

            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        return schedule if len(schedule) == numCourses else []
        
