class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            d = []
            for j in range(n):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d.append(board[i][j])

        for j in range(n):
            d = []
            for i in range(m):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d.append(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = []
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y] == '.':
                            pass
                        elif board[x][y]in d:
                            return False
                        else:
                            d.append(board[x][y])
        return True

s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
