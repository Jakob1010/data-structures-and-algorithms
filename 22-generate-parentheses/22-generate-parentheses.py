class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        
        def backtrack(s,o,c):
            if len(s) == 2* n:
                output.append("".join(s))
                return
            else:
                    if o < n:
                        s.append("(")
                        backtrack(s,o+1,c)
                        s.pop()
                    if c < o:
                        s.append(")")   
                        backtrack(s,o,c+1)
                        s.pop()
                   
        backtrack([],0,0)
        return output