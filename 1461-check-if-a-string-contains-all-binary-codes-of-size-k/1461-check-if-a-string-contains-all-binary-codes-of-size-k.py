class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found_combinations = set()
        combinations_cnt = 0
        all_ones = (1<<k)-1
        
        current = 0
        
        for i in range(0,len(s)):
            current = ((current << 1) & all_ones) | int(s[i])                      
            if i>=k-1 and current not in found_combinations:
                found_combinations.add(current)
                combinations_cnt += 1
            if combinations_cnt == all_ones+1:
                return True        
            
        return False