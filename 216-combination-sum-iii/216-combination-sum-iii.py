class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        current = []
        combinations = []
        
        
        def backtrack(current_sum,i,current,combinations):
            if len(current) == k and current_sum == n:
                combinations.append(current[:])
            elif len(current) < k and current_sum < n:
                for j in range(i,10):
                    current_sum += j
                    current.append(j)
                    backtrack(current_sum,j+1,current,combinations)
                    current_sum -= j
                    current.pop()
                
            
        backtrack(0,1,current,combinations)
        return combinations