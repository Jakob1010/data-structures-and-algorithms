class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * (n+1)
        right_max = [0] * (n+1)
        trap_cnt = 0
        
        for i in range(n):
            left_max[i+1] = max(height[i],left_max[i])
            right_max[n-1-i] = max(height[n-1-i],right_max[n-i])
            
        for i in range(1,n):
            current_h = height[i]
            l, r = left_max[i], right_max[i]
            if current_h <= l and current_h <= r:
                trap_cnt += min(l,r) - current_h
                
        return trap_cnt
            
        