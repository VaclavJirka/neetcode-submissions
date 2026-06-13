class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for i in range(9):
            if not i in rows:
                rows[i] = set()
            for j in range(9):
                if not j in cols:
                    cols[j] = set()
                if not (i,j) in squares:
                    squares[(i,j)] = set()
                number = board[i][j]
                if number == ".":
                    continue
                if number in rows[i] or number in cols[j] or number in squares[(i//3,j//3)]:
                    return False
                rows[i].add(number)
                cols[j].add(number)
                squares[(i//3,j//3)].add(number)
        return True