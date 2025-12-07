"""
Sudoku Puzzle Generator
Generates random valid Sudoku puzzles with unique solutions.
"""
import random
from typing import List, Tuple, Optional

Grid = List[List[int]]


def is_valid_placement(board: Grid, row: int, col: int, num: int) -> bool:
    """Check if placing a number at (row, col) is valid"""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def solve_for_generation(board: Grid) -> bool:
    """Solve board using backtracking (for puzzle generation)"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try numbers in random order for variety
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid_placement(board, i, j, num):
                        board[i][j] = num
                        if solve_for_generation(board):
                            return True
                        board[i][j] = 0
                return False
    return True


def generate_complete_sudoku() -> Grid:
    """Generate a complete valid Sudoku solution"""
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_for_generation(board)
    return board


def count_solutions(board: Grid, limit: int = 2) -> int:
    """Count number of solutions (stop at limit for efficiency)"""
    count = 0
    
    def solve_count(board_copy: Grid) -> None:
        nonlocal count
        if count >= limit:
            return
        
        for i in range(9):
            for j in range(9):
                if board_copy[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid_placement(board_copy, i, j, num):
                            board_copy[i][j] = num
                            solve_count(board_copy)
                            board_copy[i][j] = 0
                            if count >= limit:
                                return
                    return
        count += 1
    
    board_copy = [row[:] for row in board]
    solve_count(board_copy)
    return count


def generate_puzzle(difficulty: str = "medium") -> Grid:
    """
    Generate a random Sudoku puzzle with unique solution.
    
    Args:
        difficulty: "easy" (40-45 clues), "medium" (30-35 clues), "hard" (20-25 clues)
    
    Returns:
        A 9x9 grid with 0s representing empty cells
    """
    # Generate complete solution
    solution = generate_complete_sudoku()
    
    # Determine number of cells to remove based on difficulty
    difficulty_ranges = {
        "easy": (40, 45),
        "medium": (30, 35),
        "hard": (20, 25)
    }
    
    min_clues, max_clues = difficulty_ranges.get(difficulty, (30, 35))
    target_clues = random.randint(min_clues, max_clues)
    cells_to_remove = 81 - target_clues
    
    # Create list of all cell positions
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    
    puzzle = [row[:] for row in solution]
    removed = 0
    
    # Try removing cells while ensuring unique solution
    for row, col in positions:
        if removed >= cells_to_remove:
            break
        
        # Save the value
        original_value = puzzle[row][col]
        puzzle[row][col] = 0
        
        # Check if puzzle still has unique solution
        if count_solutions(puzzle, limit=2) == 1:
            removed += 1
        else:
            # Restore if multiple solutions
            puzzle[row][col] = original_value
    
    return puzzle


def get_random_puzzle() -> Grid:
    """Get a random puzzle with random difficulty"""
    difficulties = ["easy", "medium", "hard"]
    difficulty = random.choice(difficulties)
    return generate_puzzle(difficulty)

