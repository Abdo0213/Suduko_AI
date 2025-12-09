# Sudoku AI Solver - Functional vs Imperative Paradigms

## Project Overview

This project implements a Sudoku puzzle solver using two different programming paradigms:
1. **Functional/Declarative Paradigm** (`declarative1.py`)
2. **Imperative Paradigm** (`imparative1.py`)

Both implementations solve the same Sudoku puzzles but use fundamentally different approaches to demonstrate the core differences between functional and imperative programming styles.

## Features

- ✅ AI-powered Sudoku solver using backtracking algorithm
- ✅ Random puzzle generation with varying difficulty levels
- ✅ Interactive GUI with real-time visualization
- ✅ Fast mode for instant solving
- ✅ Side-by-side comparison of programming paradigms

## Files Structure

```
Project/
├── declarative1.py      # Functional/Declarative implementation
├── imparative1.py       # Imperative implementation
├── puzzle_generator.py # Random puzzle generator
├── sudoku_gui.py       # GUI application
└── README.md           # This documentation
```

## Programming Paradigms Comparison

### Functional/Declarative Paradigm (`declarative1.py`)

#### Core Concepts Used:

1. **Pure Functions**
   - All functions are pure (no side effects)
   - Same input always produces same output
   - Functions don't modify external state
   - Example: `is_valid()`, `apply_move()`, `find_empty_cell()`

2. **Immutability**
   - Data structures are never modified in place
   - New data structures are created for each change
   - Example: `apply_move()` returns a new board instead of modifying the original

3. **Recursion**
   - Algorithm uses recursive backtracking
   - Each recursive call works with a new immutable state
   - Example: `solve_sudoku()` recursively calls itself with new board states

4. **Higher-Order Functions**
   - Functions that take other functions as parameters
   - Example: `solve_sudoku()` accepts an optional `callback` function

5. **Type Hints**
   - Explicit type annotations for better code clarity
   - Example: `def solve_sudoku(board: Grid, callback=None) -> Optional[Grid]`

6. **Functional Composition**
   - Functions are composed together
   - Data flows through transformations
   - Example: `apply_move()` → `solve_sudoku()` → returns new state

#### Key Characteristics:

- **No Mutable State**: Board state is never modified directly
- **Referential Transparency**: Functions can be replaced with their return values
- **Side-Effect Free**: Functions don't change global state
- **Declarative Style**: Focus on "what" rather than "how"

#### Example Code Pattern:
```python
# Functional approach: Create new state
new_board = apply_move(board, row, col, num)  # Returns new board
result = solve_sudoku(new_board, callback)    # Works with new board
```

---

### Imperative Paradigm (`imparative1.py`)

#### Core Concepts Used:

1. **Object-Oriented Programming**
   - Encapsulation: Board state is encapsulated in `SudokuGame` class
   - Methods operate on object's internal state
   - Example: `self.board` is modified directly

2. **Mutable State**
   - State is modified in place
   - Direct assignment to object attributes
   - Example: `self.board[row][col] = num`

3. **Imperative Control Flow**
   - Explicit step-by-step instructions
   - Direct manipulation of state
   - Example: Modify board, then check, then backtrack

4. **State Mutation**
   - Board is modified directly during solving
   - Backtracking by setting cells back to 0
   - Example: `self.board[row][col] = 0` for backtracking

5. **Procedural Methods**
   - Methods that perform actions (imperatives)
   - Methods change object state
   - Example: `solve_sudoku()` modifies `self.board`

6. **Recursion with State**
   - Recursive calls share the same mutable state
   - State changes persist across recursive calls
   - Backtracking restores previous state

#### Key Characteristics:

- **Mutable State**: Board is modified directly
- **Side Effects**: Methods change object state
- **Imperative Style**: Focus on "how" with explicit steps
- **Stateful Objects**: Objects maintain and modify state

#### Example Code Pattern:
```python
# Imperative approach: Modify existing state
self.board[row][col] = num        # Direct mutation
if self.solve_sudoku(callback):   # State persists
    return True
self.board[row][col] = 0          # Backtrack by mutating
```

---

## Algorithm: Backtracking

Both implementations use the **backtracking algorithm** to solve Sudoku:

1. Find an empty cell
2. Try placing numbers 1-9
3. Check if placement is valid
4. If valid, recursively solve the rest
5. If no solution found, backtrack and try next number

### Differences in Implementation:

| Aspect | Functional | Imperative |
|--------|-----------|------------|
| **State Management** | Creates new board for each move | Modifies existing board |
| **Backtracking** | Returns to previous recursive call with old state | Sets cell back to 0 |
| **Memory** | More memory (creates copies) | Less memory (modifies in place) |
| **Safety** | Thread-safe (immutable) | Not thread-safe (mutable) |
| **Testing** | Easier to test (pure functions) | Requires state setup |

---

## Programming Concepts Demonstrated

### 1. **Paradigm Differences**
   - **Functional**: Declarative, immutable, pure functions
   - **Imperative**: Procedural, mutable, stateful

### 2. **Data Structures**
   - 2D lists/arrays for 9×9 grid
   - Tuple for coordinates (immutable pairs)

### 3. **Control Structures**
   - Recursion for backtracking
   - Loops for iteration
   - Conditionals for validation

### 4. **Algorithm Design**
   - Backtracking algorithm
   - Constraint satisfaction
   - Search space exploration

### 5. **Software Engineering**
   - Code organization
   - Separation of concerns
   - Reusability

---

## How to Run

### Prerequisites
- Python 3.7 or higher
- tkinter (usually included with Python)

### Running the GUI Application

```bash
python sudoku_gui.py
```

### Running Individual Implementations

**Functional/Declarative:**
```bash
python declarative1.py
```

**Imperative:**
```bash
python imparative1.py
```

---

## GUI Features

### Controls:
- **Paradigm Selection**: Choose between Functional or Imperative
- **Solve with AI**: Start the AI solver
- **Reset**: Reset to initial puzzle state
- **New Puzzle**: Generate a new random puzzle
- **Speed Slider**: Control visualization speed (1-200ms)
- **Fast Mode**: Solve instantly without visualization

### Visual Indicators:
- **Gray cells**: Pre-filled numbers (givens)
- **Green cells**: Currently being filled (during solving)
- **Blue numbers**: Solved cells
- **White cells**: Empty cells

---

## Puzzle Generator

The `puzzle_generator.py` module generates random valid Sudoku puzzles:

- **Difficulty Levels**: Easy (40-45 clues), Medium (30-35 clues), Hard (20-25 clues)
- **Unique Solutions**: Ensures each puzzle has exactly one solution
- **Random Generation**: Different puzzle each time you run

### How It Works:
1. Generates a complete valid Sudoku solution
2. Randomly removes numbers while maintaining unique solution
3. Validates solution uniqueness using backtracking

---

## Code Examples

### Functional Approach - Applying a Move

```python
def apply_move(board: Grid, row: int, col: int, num: int) -> Optional[Grid]:
    """Returns NEW board, original unchanged"""
    if board[row][col] != 0:
        return None
    if not is_valid(board, row, col, num):
        return None
    
    # Create new board (immutable)
    new_board = [r[:] for r in board]  # Deep copy
    new_board[row][col] = num
    return new_board  # Return new state
```

### Imperative Approach - Applying a Move

```python
def solve_sudoku(self, callback=None):
    """Modifies self.board directly"""
    # ... find empty cell ...
    
    # Direct mutation
    self.board[row][col] = num
    
    # Recursive call (state persists)
    if self.solve_sudoku(callback):
        return True
    
    # Backtrack by mutating
    self.board[row][col] = 0
    return False
```

---

## Educational Value

This project demonstrates:

1. **Paradigm Comparison**: Side-by-side comparison of functional vs imperative
2. **Same Problem, Different Solutions**: How paradigms shape problem-solving
3. **Trade-offs**: Memory vs. safety, mutability vs. immutability
4. **Best Practices**: When to use each paradigm
5. **Algorithm Implementation**: Same algorithm, different styles

---

## Key Takeaways

### Functional Programming Benefits:
- ✅ Easier to reason about (no hidden state changes)
- ✅ Thread-safe (immutable data)
- ✅ Easier to test (pure functions)
- ✅ More predictable behavior

### Imperative Programming Benefits:
- ✅ More memory efficient (modifies in place)
- ✅ Potentially faster (no copying)
- ✅ More intuitive for some problems
- ✅ Direct state manipulation

---

## Future Enhancements

Possible improvements:
- [ ] Difficulty selection in GUI
- [ ] Solution step counter
- [ ] Performance comparison metrics
- [ ] Export/import puzzles
- [ ] Hint system
- [ ] Multiple solving algorithms

---

## Author Notes

This project was created to fulfill the requirements for demonstrating:
- Understanding of functional programming concepts
- Understanding of imperative programming concepts
- Ability to implement the same problem using different paradigms
- GUI development skills
- Algorithm implementation (backtracking)

---

## License

This project is for educational purposes.

---

## References

- Sudoku Rules: https://en.wikipedia.org/wiki/Sudoku
- Backtracking Algorithm: https://en.wikipedia.org/wiki/Backtracking
- Functional Programming: https://en.wikipedia.org/wiki/Functional_programming
- Imperative Programming: https://en.wikipedia.org/wiki/Imperative_programming

