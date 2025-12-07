"""
Imperative Sudoku Solver

This implementation demonstrates imperative programming concepts:
- Object-Oriented Programming (encapsulation)
- Mutable state (direct modification)
- Imperative control flow (step-by-step instructions)
- State mutation (changing existing data)
- Recursion with shared mutable state

Key Principle: Methods modify object state directly through commands.
"""

class SudokuGame:
    """
    Imperative OOP approach: Encapsulates state and behavior.
    State (self.board) is MUTABLE and modified directly.
    """
    def __init__(self, board):
        self.board = board  # Mutable state stored in object

    def print_board(self):
        print("\nCurrent Board:")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                val = self.board[i][j]
                print(val if val != 0 else ".", end=" ")
            print()

    def is_valid(self, row, col, num):
        # Check row
        for j in range(9):
            if self.board[row][j] == num:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check 3x3 box
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def is_complete(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def find_empty_cell(self):
        """Find the next empty cell (mutable state access)"""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve_sudoku(self, callback=None):
        """
        Imperative AI solver using backtracking with mutable state.
        
        IMPERATIVE CONCEPTS DEMONSTRATED:
        1. State mutation: Modifies self.board directly
        2. Imperative control: Explicit step-by-step commands
        3. Shared state: Recursive calls share same mutable state
        4. Side effects: Method changes object state
        
        Modifies self.board directly (mutable state).
        callback: Optional function(board) called on each step for visualization
        """
        if self.is_complete():
            if callback:
                callback(self.board)
            return True
        
        empty = self.find_empty_cell()
        if empty is None:
            if callback:
                callback(self.board)
            return self.is_complete()
        
        row, col = empty
        
        # Try each number 1-9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                # IMPERATIVE: Direct state mutation
                self.board[row][col] = num  # Modify existing state
                if callback:
                    callback(self.board)
                
                # Recursive call - state persists (shared mutable state)
                if self.solve_sudoku(callback):
                    return True
                
                # IMPERATIVE: Backtrack by mutating state back
                self.board[row][col] = 0  # Direct mutation for backtracking
                if callback:
                    callback(self.board)
        
        return False

    def play(self):
        print("Welcome to Sudoku!")
        print("Enter row col number (1-9)")
        print("Example: 2 3 5  → means row 2, col 3 = 5")
        print("Type '0 0 0' to exit")

        while True:
            self.print_board()

            if self.is_complete():
                print("\nCongratulations! You solved the Sudoku correctly!")
                break

            try:
                row, col, num = map(int, input("\nYour move: ").split())
            except ValueError:
                print("Invalid input format!")
                continue

            if row == 0 and col == 0 and num == 0:
                print("Game exited.")
                break

            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("Numbers must be between 1 and 9!")
                continue

            row -= 1
            col -= 1

            if self.board[row][col] != 0:
                print("Cell already filled!")
                continue

            if self.is_valid(row, col, num):
                self.board[row][col] = num
                print("Correct move!")
            else:
                print("Invalid move! Try again.")


# --------------------
# Start game
# --------------------
if __name__ == "__main__":
    try:
        from puzzle_generator import get_random_puzzle
        print("Generating random puzzle...")
        puzzle = get_random_puzzle()
    except ImportError:
        # Fallback to default puzzle if generator not available
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

    print("\n" + "="*50)
    print("IMPERATIVE SUDOKU SOLVER")
    print("="*50)
    print("\nChoose an option:")
    print("1. Play manually (enter moves yourself)")
    print("2. Solve with AI (watch the solver work)")
    print("3. Solve with AI instantly (no visualization)")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    game = SudokuGame(puzzle)
    
    if choice == "1":
        game.play()
    elif choice == "2":
        print("\nSolving with AI (Imperative Paradigm)...")
        print("Initial puzzle:")
        game.print_board()
        print("\nSolving...\n")
        
        def show_progress(board):
            # Create temporary game to print
            temp_game = SudokuGame(board)
            temp_game.print_board()
            print()
            import time
            time.sleep(0.1)  # Small delay for visualization
        
        success = game.solve_sudoku(show_progress)
        if success:
            print("="*50)
            print("SOLVED! Final solution:")
            print("="*50)
            game.print_board()
        else:
            print("No solution found!")
    elif choice == "3":
        print("\nSolving with AI (Imperative Paradigm - Fast Mode)...")
        print("Initial puzzle:")
        game.print_board()
        print("\nSolving...\n")
        
        success = game.solve_sudoku(None)  # No callback = fast
        if success:
            print("="*50)
            print("SOLVED! Final solution:")
            print("="*50)
            game.print_board()
        else:
            print("No solution found!")
    else:
        print("Invalid choice. Starting manual play...")
        game.play()
