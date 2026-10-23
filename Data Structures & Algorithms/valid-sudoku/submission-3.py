class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #each cell is contained in 3 types: row, column, box
        #organize board by row, then col, then box
        #take set of each category, check if len matches or not?
            #periods mess this up...
        #rows is js each index of board
        for i in range(len(board)):
            seen_row = []
            seen_col = []
            seen_box = []
            for j in range(len(board)):
                cell_row = board[i][j]
                if cell_row in seen_row:
                    return False
                if cell_row != ".":
                    seen_row.append(cell_row)
                cell_col = board[j][i]
                if cell_col in seen_col:
                    return False
                if cell_col != ".":
                    seen_col.append(cell_col)
                box_x = 3*(i//3) + j//3
                box_y = 3*(i%3) + j%3
                cell_box = board[box_x][box_y]
                if cell_box in seen_box:
                    return False
                if cell_box != ".":
                    seen_box.append(cell_box)
        return True