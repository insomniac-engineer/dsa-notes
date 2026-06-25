class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = []
        colSet = []
        r = 0
        c = 0

        while c < 9:
            while r < 9:
                if board[r][c] != '.':
                    if board[r][c] in colSet:
                        return False
                    else:
                        colSet.append(board[r][c])
                r += 1
            c += 1
            r = 0
            colSet.clear()
            
        for i in board:
            for j in i:
                if j != "." and j in rowSet:
                    return False
                else:
                    rowSet.append(j)
            rowSet.clear()
            
        box_r = 0
        box_c = 0
        while box_r < 9:
            while box_c < 9:
                boxSet = []
                
                r = 0
                while r < 3:
                    c = 0
                    while c < 3:
                        element = board[box_r + r][box_c + c]
                        if element != '.':
                            if element in boxSet:
                                return False
                            else:
                                boxSet.append(element)
                        c += 1
                    r += 1
                
                box_c += 3
            box_c = 0
            box_r += 3 

        return True

# def main():
#     test_board = [
#         ["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#         [".","9","8",".",".",".",".",".","3"],
#         ["5",".",".",".","6",".",".",".","4"],
#         [".",".",".","8",".","3",".",".","5"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".",".",".",".",".",".","2",".","."],
#         [".",".",".","4","1","9",".",".","8"],
#         [".",".",".",".","8",".",".","7","9"]
#     ]
    
#     solution = Solution()
#     result = solution.isValidSudoku(test_board)
#     print(f"Result: {result}")

# if __name__ == "__main__":
#     main()