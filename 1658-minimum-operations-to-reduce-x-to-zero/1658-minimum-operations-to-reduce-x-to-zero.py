class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        l = 0
        current = 0
        min_operations = -1
        
        for r in range(len(nums)):
            current += nums[r]
            while l<=r and total-current < x:
                current -= nums[l]
                l+=1
            if total - current == x:
                min_operations = max(min_operations, r-l+1)
                
        if min_operations == -1:
            return -1
        else:
            return len(nums) - min_operations
        