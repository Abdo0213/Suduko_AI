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
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


def is_valid(board: Grid, row: int, col: int, num: int) -> bool:
    if num in board[row]:
        return False

    if num in (board[i][col] for i in range(9)):
        return False

    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


def is_complete(board: Grid) -> bool:
    return all(0 not in row for row in board)


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
    new_board = [r[:] for r in board]  # Deep copy
    new_board[row][col] = num
    return new_board  # Return new state, not modified original


def find_empty_cell(board: Grid) -> Optional[Tuple[int, int]]:
    """Pure function to find the next empty cell (returns immutable tuple)"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


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
    
    # Try each number 1-9
    for num in range(1, 10):
        # Functional approach: Create new state, don't modify existing
        new_board = apply_move(board, row, col, num)
        if new_board is not None:
            if callback:
                callback(new_board)  # Higher-order function usage
            # Recursive call with NEW immutable state
            result = solve_sudoku(new_board, callback)
            if result is not None:
                return result  # Return new solved board
    
    # Backtracking in functional style: return None, previous call tries next number
    return None

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
    state = board  # Initial state

    print("Declarative Sudoku")
    print("Enter: row col number (1–9)")
    print("Example: 1 3 4")
    print("Type: 0 0 0 to exit")

    while True:
        print_board(state)

        if is_complete(state):
            print("\n You solved the Sudoku!")
            return

        try:
            row, col, num = map(int, input("\nYour move: ").split())
        except ValueError:
            print("Invalid input format")
            continue

        if (row, col, num) == (0, 0, 0):
            print("Game ended")
            return

        if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
            print("Values must be between 1 and 9")
            continue

        # Functional approach: Get new state, replace old one
        new_state = apply_move(state, row - 1, col - 1, num)

        if new_state is None:
            print("Invalid move!")
        else:
            print("Correct move!")
            state = new_state  # Replace state (functional style)



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
