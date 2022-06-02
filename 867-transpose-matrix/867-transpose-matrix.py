class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        transposed = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(n):
            for j in range(m):
                transposed[j][i] = matrix[i][j]
                
        return transposed
                