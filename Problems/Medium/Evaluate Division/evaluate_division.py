class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for [a,b],val in zip(equations,values):
            graph[a].append((b,val))
            graph[b].append((a,1/val))
        
        def dfs(curr,target,seen,val):
            if curr not in graph or target not in graph:
                return -1
            if curr == target:
                return val
            seen.add(curr)
            for neighbour,weight in graph[curr]:
                if neighbour not in seen:
                    result = dfs(neighbour,target,seen,val*weight)
                    if result != -1:
                        return result
            return -1

        results = []
        for c,d in queries:
            results.append(dfs(c,d,set(),1))
        return results

