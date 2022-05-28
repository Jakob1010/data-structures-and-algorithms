class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = 0
        
        for i,num in enumerate(nums):
            missing_num += i
            missing_num -= num
            
        return missing_num+len(nums)