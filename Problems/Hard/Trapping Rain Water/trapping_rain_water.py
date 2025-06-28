class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 # Can also return null (Subject to preference)
        trapped_water = 0
        l,r = 0,len(height)-1
        lMax,rMax = height[l],height[r]

        while l<r:
            if lMax < rMax:
                trapped_water += lMax-height[l]
                l+=1
                lMax = max(lMax,height[l])
            else:
                trapped_water += rMax-height[r]
                r-=1
                rMax = max(rMax,height[r])
        
        return trapped_water
