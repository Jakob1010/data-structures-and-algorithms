class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        digit_to_letter = {
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        output = []
        
        def backtrack(k,l,temp):
            if len(temp) == len(digits):
                output.append(temp)
                
            for i in range(k,len(digits)):
                for j in range(0,len(digit_to_letter[digits[i]])):
                    temp = temp + digit_to_letter[digits[i]][j]
                    backtrack(i+1,j, temp)
                    temp = temp[0:len(temp)-1]
                    
        backtrack(0,0,"")            
        return output