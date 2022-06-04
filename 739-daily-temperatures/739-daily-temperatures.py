class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack)>0 and temp>stack[-1][0]:
                lower_temp = stack.pop()
                output[lower_temp[1]] = i - lower_temp[1]
            stack.append((temp,i))
        return output
            
        
        