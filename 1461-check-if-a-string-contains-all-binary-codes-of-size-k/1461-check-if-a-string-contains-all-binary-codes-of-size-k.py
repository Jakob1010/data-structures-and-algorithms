class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        needed = 1 << k
        all_ones = needed - 1
        combinations = set()
        current = 0

        
        for i in range(0,len(s)):
            current = ((current << 1) & all_ones) | int(s[i])
            if i>=k-1 and current not in combinations:
                combinations.add(current)
                needed-=1
                if needed == 0: return True
                
        return False
                
        