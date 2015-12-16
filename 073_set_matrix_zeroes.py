class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_zero = False
        column_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

                    if i == 0:
                        row_zero = True
                    if j == 0:
                        column_zero = True

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if column_zero:
            for i in range(m):
                matrix[i][0] = 0
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
