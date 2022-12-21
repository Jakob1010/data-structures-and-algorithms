class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]   
        if len(nums) == 1:
            if nums[0] == target: return 0
            return -1
        
        # find turning point
        l, r = 0, len(nums)-1
        m = l + (r-l) // 2
        while nums[l]>nums[r]:
            m = l + (r-l) // 2
            if nums[m]>nums[m+1]:
                break
            
            if nums[m] > nums[l]:
                l = m
            elif nums[m] < nums[r]:
                r = m

           
        if target >= nums[0] and target <= nums[m]:
            l, r = 0, m
        elif target >= nums[m+1] and target <= nums[len(nums)-1]:
            l, r = m+1, len(nums)-1
        else:
            return -1
        
        while l<=r:
            m = l + (r-l) // 2
            
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        
        return -1
            