class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for s in set(board[i]):  # checking every row
                if board[i].count(s)>1 and s != ".":
                    return False
            column=set()
            for j in range(9):  # checking every column
                if board[j][i] in column and board[j][i] != ".":
                    return False
                else:
                    column.add(board[i][j])
        for i in range(0,9,3):  # checking every 3x3 sub-box
            for j in range(0,9,3):
                square=set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if board[row][col] in square and board[row][col] != ".":
                            return False
                        else:
                            square.add(board[row][col])
        return True
