class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n1, n2 = len(matrix), len(matrix[0])
        le, ri = 0, n1 * n2 - 1
        
        while le<=ri:
            m = le + (ri-le) // 2
            r = m // (n2)
            c = m % (n2)
            
            if matrix[r][c] < target:
                le = r * (n2) + c + 1
            elif matrix[r][c] > target:
                ri = r * (n2) + c - 1
            else:
                return True
            
        return False