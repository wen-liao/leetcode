class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        n = N//2
        for i in range(n):
            for j in range(N-1-2*i):
                matrix[i][i+j],matrix[i+j][N-1-i],matrix[N-1-i][N-1-j-i],matrix[N-1-j-i][i] = matrix[N-1-j-i][i],matrix[i][i+j],matrix[i+j][N-1-i],matrix[N-1-i][N-1-j-i]