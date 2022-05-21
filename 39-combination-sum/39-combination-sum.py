class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(current_sum,output,current,i):
            if current_sum == target:
                output.append(current[:])
            elif current_sum > target:
                return
            else:
                for j,num in enumerate(candidates[i:]):
                    current.append(num)
                    backtrack(current_sum+num,output,current,i+j)
                    current.pop()
            
        backtrack(0,output,[],0)
        return output