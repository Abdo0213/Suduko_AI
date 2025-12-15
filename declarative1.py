"""
Functional/Declarative Sudoku Solver

This implementation demonstrates functional programming concepts:
- Pure functions (no side effects)
- Immutability (no state mutation)
- Recursion with immutable state
- Higher-order functions (callback parameter)
- Type hints for clarity

Key Principle: Functions transform input to output without modifying external state.
"""
from typing import List, Tuple, Optional

# Type alias for better code clarity
Grid = List[List[int]]

# ============================================
# PURE FUNCTIONS - No side effects
# ============================================
def print_board(board: Grid) -> None:
    print("\nCurrent Board:")
    
    def print_cells(i: int, j: int) -> None:
        if j == 9:
            print()
            return
        
        if j % 3 == 0 and j != 0:
            print("|", end=" ")
        
        print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print_cells(i, j + 1)

    def print_rows(i: int) -> None:
        if i == 9:
            return
            
        if i % 3 == 0 and i != 0:
            print("-" * 21)
            
        print_cells(i, 0)
        print_rows(i + 1)

    print_rows(0)


def is_valid(board: Grid, row: int, col: int, num: int) -> bool:
    if num in board[row]:
        return False

    def check_col(i: int) -> bool:
        if i == 9:
            return True
        if board[i][col] == num:
            return False
        return check_col(i + 1)
    
    if not check_col(0):
        return False

    box_row = row // 3 * 3
    box_col = col // 3 * 3
    
    def check_box(i: int, j: int) -> bool:
        if i == box_row + 3:
            return True
        if j == box_col + 3:
            return check_box(i + 1, box_col)
        
        if board[i][j] == num:
            return False
        return check_box(i, j + 1)

    return check_box(box_row, box_col)


def is_complete(board: Grid) -> bool:
    def check_rows(i: int) -> bool:
        if i == 9:
            return True
        if 0 in board[i]:
            return False
        return check_rows(i + 1)
    return check_rows(0)


def apply_move(board: Grid, row: int, col: int, num: int) -> Optional[Grid]:
    """
    Pure function: Returns a NEW board, original is unchanged.
    This demonstrates IMMUTABILITY - we never modify the input.
    
    Functional Principle: Transform input → output, don't mutate.
    """
    if board[row][col] != 0:
        return None

    if not is_valid(board, row, col, num):
        return None

    # Create new board (immutability) - original board unchanged
    # Create new board (immutability) - original board unchanged
    def build_new_row(r_idx: int, c_idx: int) -> List[int]:
        if c_idx == 9:
            return []
        if r_idx == row and c_idx == col:
            return [num] + build_new_row(r_idx, c_idx + 1)
        return [board[r_idx][c_idx]] + build_new_row(r_idx, c_idx + 1)

    def build_board(r_idx: int) -> Grid:
        if r_idx == 9:
             return []
        # Construct new row recursively
        new_row = build_new_row(r_idx, 0)
        return [new_row] + build_board(r_idx + 1)

    return build_board(0)


def find_empty_cell(board: Grid) -> Optional[Tuple[int, int]]:
    """Pure function to find the next empty cell (returns immutable tuple)"""
    def search(i: int, j: int) -> Optional[Tuple[int, int]]:
        if i == 9:
            return None
        if j == 9:
            return search(i + 1, 0)
        
        if board[i][j] == 0:
            return (i, j)
        return search(i, j + 1)
    return search(0, 0)


def solve_sudoku(board: Grid, callback=None) -> Optional[Grid]:
    """
    Pure functional AI solver using backtracking.
    
    FUNCTIONAL CONCEPTS DEMONSTRATED:
    1. Pure function: No side effects, only returns new state
    2. Recursion: Calls itself with new immutable state
    3. Higher-order function: Accepts callback function as parameter
    4. Immutability: Never modifies input board, returns new board
    
    Returns a new solved board or None if unsolvable.
    callback: Optional function(board) called on each step for visualization
    """
    if is_complete(board):
        if callback:
            callback(board)
        return board
    
    empty = find_empty_cell(board)
    if empty is None:
        if callback:
            callback(board)
        return board if is_complete(board) else None
    
    row, col = empty
    
    def try_num(num: int) -> Optional[Grid]:
        if num == 10:
            return None

        # Functional approach: Create new state, don't modify existing
        new_board = apply_move(board, row, col, num)
        if new_board is not None:
            if callback:
                callback(new_board)  # Higher-order function usage
            # Recursive call with NEW immutable state
            result = solve_sudoku(new_board, callback)
            if result is not None:
                return result  # Return new solved board
        
        return try_num(num + 1)
    
    return try_num(1)

# ============================================
# GAME LOOP - Functional State Replacement
# ============================================
# In functional programming, we REPLACE the whole state
# rather than modifying it. Each iteration gets a new state.

def play(board: Grid) -> None:
    """
    Game loop demonstrating functional state management.
    State is replaced, not modified (immutability principle).
    """
    print("Declarative Sudoku")
    print("Enter: row col number (1–9)")
    print("Example: 1 3 4")
    print("Type: 0 0 0 to exit")

    def game_loop(state: Grid) -> None:
        print_board(state)

        if is_complete(state):
            print("\n You solved the Sudoku!")
            return

        try:
            inp = input("\nYour move: ").split()
            row, col, num = map(int, inp)
        except ValueError:
            print("Invalid input format")
            return game_loop(state)

        if (row, col, num) == (0, 0, 0):
            print("Game ended")
            return

        if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
            print("Values must be between 1 and 9")
            return game_loop(state)

        # Functional approach: Get new state, replace old one
        new_state = apply_move(state, row - 1, col - 1, num)

        if new_state is None:
            print("Invalid move!")
            return game_loop(state)
        else:
            print("Correct move!")
            # Replace state (functional style) - recursive call with new state
            return game_loop(new_state)

    game_loop(board)



#Start Game
if __name__ == "__main__":
    try:
        from puzzle_generator import get_random_puzzle
        print("Generating random puzzle...")
        initial_board = get_random_puzzle()
    except ImportError:
        # Fallback to default puzzle if generator not available
        initial_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    print("\n" + "="*50)
    print("FUNCTIONAL/DECLARATIVE SUDOKU SOLVER")
    print("="*50)
    print("\nChoose an option:")
    print("1. Play manually (enter moves yourself)")
    print("2. Solve with AI (watch the solver work)")
    print("3. Solve with AI instantly (no visualization)")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        play(initial_board)
    elif choice == "2":
        print("\nSolving with AI (Functional Paradigm)...")
        print("Initial puzzle:")
        print_board(initial_board)
        print("\nSolving...\n")
        
        def show_progress(board):
            print_board(board)
            print()
            import time
            time.sleep(0.1)  # Small delay for visualization
        
        result = solve_sudoku(initial_board, show_progress)
        if result:
            print("="*50)
            print("SOLVED! Final solution:")
            print("="*50)
            print_board(result)
        else:
            print("No solution found!")
    elif choice == "3":
        print("\nSolving with AI (Functional Paradigm - Fast Mode)...")
        print("Initial puzzle:")
        print_board(initial_board)
        print("\nSolving...\n")
        
        result = solve_sudoku(initial_board, None)  # No callback = fast
        if result:
            print("="*50)
            print("SOLVED! Final solution:")
            print("="*50)
            print_board(result)
        else:
            print("No solution found!")
    else:
        print("Invalid choice. Starting manual play...")
        play(initial_board)
