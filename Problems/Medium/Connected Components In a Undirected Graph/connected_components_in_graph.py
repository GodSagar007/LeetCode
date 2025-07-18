class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = 0

        seen = set()
        def dfs(a):
            seen.add(a)
            for b in graph[a]:
                if b not in seen:
                    dfs(b)
        
        for i in range(n):
            if i not in seen:
                components+=1
                dfs(i)
        
        return components
