# How to Play the Individual Implementations

## Quick Start

### Functional/Declarative Implementation
```bash
python declarative1.py
```

### Imperative Implementation
```bash
python imparative1.py
```

---

## Menu Options

When you run either file, you'll see a menu with 3 options:

```
Choose an option:
1. Play manually (enter moves yourself)
2. Solve with AI (watch the solver work)
3. Solve with AI instantly (no visualization)
```

---

## Option 1: Manual Play

### How to Play:
1. The puzzle will be displayed in the terminal
2. Enter your moves in the format: `row col number`
3. Example: `2 3 5` means place number 5 at row 2, column 3

### Input Format:
- **Row**: 1-9 (top to bottom)
- **Column**: 1-9 (left to right)
- **Number**: 1-9 (the digit to place)

### Example Session:
```
Current Board:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

Your move: 1 3 4
Correct move!
```

### Rules:
- ✅ You can only place numbers in empty cells (shown as `.`)
- ✅ Numbers must be valid (no duplicates in row, column, or 3×3 box)
- ✅ Type `0 0 0` to exit the game
- ✅ Invalid moves will be rejected

### Tips:
- Start with cells that have fewer possibilities
- Look for numbers that can only go in one place
- Use the 3×3 boxes to narrow down options

---

## Option 2: AI Solve with Visualization

### What Happens:
- The AI solver will solve the puzzle step-by-step
- You'll see each move as it's made
- The board updates in real-time
- Shows the backtracking process

### Example Output:
```
Solving with AI (Functional Paradigm)...
Initial puzzle:
[Puzzle displayed]

Solving...

Current Board:
[Shows each step]
```

### Best For:
- Learning how the algorithm works
- Seeing the backtracking process
- Understanding the solving strategy

---

## Option 3: AI Solve Instantly

### What Happens:
- The AI solves the puzzle instantly
- Only shows the initial puzzle and final solution
- No step-by-step visualization

### Example Output:
```
Solving with AI (Functional Paradigm - Fast Mode)...
Initial puzzle:
[Puzzle displayed]

Solving...

SOLVED! Final solution:
[Complete solution displayed]
```

### Best For:
- Quick solutions
- Testing the solver
- When you just want the answer

---

## Understanding the Board Display

### Grid Layout:
```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

- **Numbers**: Pre-filled cells (givens)
- **`.` (dots)**: Empty cells you need to fill
- **`|`**: Separates 3×3 boxes horizontally
- **`---`**: Separates 3×3 boxes vertically

### Row and Column Numbers:
- **Rows**: 1-9 from top to bottom
- **Columns**: 1-9 from left to right

Example: Row 1, Column 1 is the top-left cell (contains `5` in the example above)

---

## Troubleshooting

### "Invalid input format"
- Make sure you enter exactly 3 numbers separated by spaces
- Example: `2 3 5` ✅ (not `2,3,5` or `2-3-5`)

### "Values must be between 1 and 9"
- Row, column, and number must all be between 1 and 9
- Use `0 0 0` to exit, not to place a number

### "Cell already filled"
- You can't place a number in a cell that already has one
- Only empty cells (shown as `.`) can be filled

### "Invalid move!"
- The number you're trying to place violates Sudoku rules
- Check for duplicates in the row, column, or 3×3 box

---

## Differences Between Implementations

### Functional (`declarative1.py`):
- Uses pure functions
- Creates new board states (immutable)
- Demonstrates functional programming concepts

### Imperative (`imparative1.py`):
- Uses object-oriented approach
- Modifies board directly (mutable state)
- Demonstrates imperative programming concepts

**Note**: Both solve puzzles the same way, but use different programming styles!

---

## Tips for Success

1. **Start Easy**: Look for cells with only one possible number
2. **Use Elimination**: Cross out numbers that can't go in a cell
3. **Check Boxes**: The 3×3 boxes are key constraints
4. **Be Patient**: Some puzzles take time to solve
5. **Practice**: Try different puzzles to improve

---

## Exiting the Game

- Type `0 0 0` when prompted for a move
- The game will exit and return to the command line

---

## Need Help?

- Check the `README.md` for detailed documentation
- Review `CONCEPTS.md` for programming concepts
- Run the GUI version (`python sudoku_gui.py`) for a visual interface

Happy solving! 🎯

