class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): return max(piles)
        l, r = 1, max(piles)
        
        def is_valid(speed):
            hours_left = h
            for pile in piles:
                hours_left -= pile // speed + (pile % speed > 0)
                if hours_left < 0: return False
            return True
        
        while l<r:
            m = (r+l) // 2
            
            v = is_valid(m)
            if v:
                r = m
            else:
                l = m + 1
            
        return r
        