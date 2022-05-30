class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2
        
        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        while dividend<=divisor:
            
            divisor_exp = divisor
            quotient_exp = -1
            while dividend <= divisor_exp + divisor_exp and divisor_exp >= HALF_MIN_INT:
                divisor_exp += divisor_exp
                quotient_exp += quotient_exp       
            
            quotient += quotient_exp
            dividend -= divisor_exp

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient