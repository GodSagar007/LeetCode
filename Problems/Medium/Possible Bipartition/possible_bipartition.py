class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0]*(n+1)
        for person in range(1,n+1):
            if color[person] != 0: # already grouped
                continue
            
            q = deque([person])
            color[person] = 1
            while q:
                person = q.popleft()
                for hater in graph[person]:
                    if color[hater] == color[person]:
                        return False
                    if color[hater] == 0:
                        color[hater] = -color[person]
                        q.append(hater)

        return True
        
