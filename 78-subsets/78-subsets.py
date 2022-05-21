class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        i = 0
        
        def backtrack(i,current):
            output.append(current[:])
            
            for j,num in enumerate(nums[i:]):
                current.append(num)
                backtrack(i+j+1,current)
                current.pop()
            
        backtrack(0,[])
        return output