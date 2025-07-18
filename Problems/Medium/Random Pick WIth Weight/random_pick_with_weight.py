class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        prefix = 0
        for weight in w:
            prefix+=weight
            self.weights.append(prefix)
        

    def pickIndex(self) -> int:
        idx = random.randint(1,self.weights[-1])
        left,right = 0,len(self.weights)
        while left<right:
            mid = (left+right)//2
            if self.weights[mid]<idx:
                left = mid+1
            else:
                right = mid
        
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
