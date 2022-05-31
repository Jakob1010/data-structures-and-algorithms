class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        combinations = pow(2,k)
        for i in range(len(s)-k+1):
            if s[i:i+k] not in codes:
                codes.add(s[i:i+k])
                if len(codes) == combinations:
                    return True
                
        return False