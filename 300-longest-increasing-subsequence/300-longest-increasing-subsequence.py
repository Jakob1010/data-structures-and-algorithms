class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            if len(sub)==0 or num > sub[-1]:
                sub.append(num)
            else:
                j = 0
                while num > sub[j]:
                    j+=1
                sub[j] = num

        return len(sub)