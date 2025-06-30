class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp,username,website))

        userVisitPattern = defaultdict(list)
        for _,user,site in data:
            userVisitPattern[user].append(site)
        
        patternCount = Counter()
        for user,sites in userVisitPattern.items():
            n = len(sites)
            seen = set()

            for i in range(n-2):
                for j in range(i+1,n-1):
                    for k in range(j+1,n):
                        pattern = (sites[i],sites[j],sites[k])
                        if pattern not in seen:
                            seen.add(pattern)
                            patternCount[pattern] += 1

        if not patternCount:
            return []

        maxVisitedPattern = max(sorted(patternCount),key = lambda p: patternCount[p])
        return maxVisitedPattern
