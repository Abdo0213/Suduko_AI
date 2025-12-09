import sys
import os

# Add project directory to path
sys.path.append(os.getcwd())

from imparative1 import SudokuGame

def test_solver():
    print("Testing Iterative Solver...")
    
    # Test case 1: Easy puzzle
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    game = SudokuGame(puzzle)
    print("Initial Board:")
    game.print_board()
    
    print("\nSolving...")
    success = game.solve_sudoku()
    
    if success:
        print("\nSolved Successfully!")
        game.print_board()
        
        # Verify correctness
        if game.is_complete():
            print("Verification: Board is valid and complete.")
        else:
            print("Verification FAILED: Board is not complete.")
    else:
        print("\nFailed to solve.")

if __name__ == "__main__":
    test_solver()
