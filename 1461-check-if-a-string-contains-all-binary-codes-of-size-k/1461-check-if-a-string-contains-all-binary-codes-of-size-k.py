class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        all_ones = need-1
        found = [False] * need
        hash_value = 0
        
        # old hash: 10
        # new hash: 01
        # shift old:100
        for i in range(len(s)):
            hash_value = ((hash_value << 1) & all_ones) | int(s[i])
            
            if i >= k-1 and found[hash_value] == False:
                found[hash_value] = True
                need -= 1
                if need == 0: return True
                
        return False
                