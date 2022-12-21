class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+","-","*","/"}
        
        def compute_result(num1, num2, operator):
            if operator == "+":
                return num1+num2
            elif operator == "-":
                return num2-num1
            elif operator == "*":
                return num2*num1
            else:
                return int(num2/num1)
        
        for token in tokens:
            if token in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(compute_result(num1,num2,token))
            else:
                stack.append(int(token))
                
        return stack[0]
                
        