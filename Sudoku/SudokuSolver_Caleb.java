
public class SudokuSolver_Caleb implements SudokuSolver {
	public int[][] solve_dfs(int i, int j, int[][] cells) {
        if (i == 9) { // Base case - solution has been found 
            return cells; 
        }

        int i2;
        int j2;

        //Check if at the last column
        if (j == 8) { // Go to next row and start at first column
            i2 = i + 1;
            j2 = 0;
        }
        else { // Stay in same row and go to next column
            i2 = i;
            j2 = j +1;
        }

        if (cells[i][j] != 0) { // Recursive call to fill in cells
            return solve_dfs(i2, j2, cells);
        }

        // Iterate through the board
        for (int num = 1; num <= 9; num++) {
            if (check_move(i, j, num, cells)) { // If the move is valid
                cells[i][j] = num; // Temporarily assign the number to the current cell 
                int[][] nextCell = solve_dfs(i2, j2, cells); // Find next valid cell recursively
                if (nextCell != null) { // Check if valid nextCell has been found
                    return nextCell;
                }
                cells[i][j] = 0; // Didn't find valid nextCell, backtrack
            }
        }
        return null; // No solution found
    }

	 public boolean check_move(int i, int j, int val, int[][] cells){
        for (int num = 0; num < 9; num++) { // Loop through cells in same column and row
            if (cells[i][num] == val || cells[num][j] == val) { // Check if number is in row or column
                return false; // Number is in row or column, invalid move
            }
        }

        int subGridRow = (i / 3) * 3; // Determine which 3x3 box in the row
        int subGridCol = (j / 3) * 3; // Determine which 3x3 box in the column

        for (int row = 0; row < 3; row++) { // For the rows in the 3x3 subgrid
            for (int col = 0; col < 3; col++) { //For the columns in the 3x3 subgrid
                if (cells[subGridRow + row][subGridCol + col] == val) { // Check if value is in 3x3 subgrid
                    return false; // Return false if it is
                }
            }
        }
        return true;
    }
}
