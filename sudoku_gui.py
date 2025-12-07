import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from typing import List, Optional
from declarative1 import solve_sudoku as solve_functional, Grid as FunctionalGrid
from imparative1 import SudokuGame
from puzzle_generator import get_random_puzzle

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku AI Solver - Functional vs Imperative")
        self.root.geometry("600x700")
        
        # Generate random puzzle
        self.initial_board = get_random_puzzle()
        
        self.current_board = [row[:] for row in self.initial_board]
        self.solving = False
        self.solve_speed = 50  # milliseconds between updates
        self.fast_mode = False  # Fast solving without visualization
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Sudoku AI Solver", 
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=10)
        
        # Paradigm selection
        paradigm_frame = tk.Frame(self.root)
        paradigm_frame.pack(pady=10)
        
        tk.Label(
            paradigm_frame, 
            text="Select Paradigm:", 
            font=("Arial", 12)
        ).pack(side=tk.LEFT, padx=10)
        
        self.paradigm_var = tk.StringVar(value="Functional")
        functional_radio = tk.Radiobutton(
            paradigm_frame,
            text="Functional (Pure Functions)",
            variable=self.paradigm_var,
            value="Functional",
            font=("Arial", 10)
        )
        functional_radio.pack(side=tk.LEFT, padx=5)
        
        imperative_radio = tk.Radiobutton(
            paradigm_frame,
            text="Imperative (Mutable State)",
            variable=self.paradigm_var,
            value="Imperative",
            font=("Arial", 10)
        )
        imperative_radio.pack(side=tk.LEFT, padx=5)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        self.solve_button = tk.Button(
            button_frame,
            text="Solve with AI",
            command=self.start_solving,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        )
        self.solve_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset_board,
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=5
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        self.new_puzzle_button = tk.Button(
            button_frame,
            text="New Puzzle",
            command=self.new_puzzle,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=5
        )
        self.new_puzzle_button.pack(side=tk.LEFT, padx=5)
        
        # Speed control
        speed_frame = tk.Frame(self.root)
        speed_frame.pack(pady=5)
        
        tk.Label(speed_frame, text="Speed:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.speed_var = tk.IntVar(value=50)
        speed_scale = tk.Scale(
            speed_frame,
            from_=1,
            to=200,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            length=200,
            command=self.update_speed
        )
        speed_scale.pack(side=tk.LEFT, padx=5)
        
        # Fast mode checkbox
        fast_mode_frame = tk.Frame(self.root)
        fast_mode_frame.pack(pady=5)
        
        self.fast_mode_var = tk.BooleanVar(value=False)
        fast_mode_check = tk.Checkbutton(
            fast_mode_frame,
            text="Fast Mode (Solve without visualization)",
            variable=self.fast_mode_var,
            font=("Arial", 10),
            command=self.toggle_fast_mode
        )
        fast_mode_check.pack()
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready to solve",
            font=("Arial", 10),
            fg="blue"
        )
        self.status_label.pack(pady=5)
        
        # Sudoku grid
        self.grid_frame = tk.Frame(self.root, bg="black", padx=2, pady=2)
        self.grid_frame.pack(pady=10)
        
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_frame = tk.Frame(
                    self.grid_frame,
                    bg="black",
                    width=50,
                    height=50
                )
                cell_frame.grid(row=i, column=j, padx=1, pady=1)
                
                # Add thicker borders for 3x3 boxes
                if i % 3 == 0:
                    cell_frame.grid(pady=(2, 1))
                if j % 3 == 0:
                    cell_frame.grid(padx=(2, 1))
                
                cell_label = tk.Label(
                    cell_frame,
                    text="",
                    font=("Arial", 16, "bold"),
                    width=3,
                    height=1,
                    bg="white",
                    relief=tk.RAISED
                )
                cell_label.pack(fill=tk.BOTH, expand=True)
                row.append(cell_label)
            self.cells.append(row)
    
    def update_speed(self, value):
        self.solve_speed = int(value)
    
    def toggle_fast_mode(self):
        """Toggle fast mode on/off"""
        self.fast_mode = self.fast_mode_var.get()
        if self.fast_mode:
            self.status_label.config(text="Fast Mode: ON (No visualization)", fg="orange")
        else:
            self.status_label.config(text="Fast Mode: OFF (With visualization)", fg="blue")
    
    def update_display(self, highlight_cell=None):
        """Update the GUI display with current board state"""
        for i in range(9):
            for j in range(9):
                value = self.current_board[i][j]
                cell = self.cells[i][j]
                
                if value == 0:
                    cell.config(text="", bg="white")
                else:
                    # Check if this was a given (initial value)
                    is_given = self.initial_board[i][j] != 0
                    if is_given:
                        cell.config(text=str(value), bg="#E0E0E0", fg="black")
                    else:
                        # Highlight if this is the cell being modified
                        if highlight_cell == (i, j):
                            cell.config(text=str(value), bg="#90EE90", fg="black")
                        else:
                            cell.config(text=str(value), bg="white", fg="blue")
        
        self.root.update()
    
    def reset_board(self):
        """Reset the board to initial state"""
        if self.solving:
            messagebox.showwarning("Warning", "Please wait for solving to complete")
            return
        
        self.current_board = [row[:] for row in self.initial_board]
        self.update_display()
        self.status_label.config(text="Board reset", fg="blue")
    
    def new_puzzle(self):
        """Generate a new random puzzle"""
        if self.solving:
            messagebox.showwarning("Warning", "Please wait for solving to complete")
            return
        
        self.status_label.config(text="Generating new puzzle...", fg="orange")
        self.root.update()
        
        # Generate new puzzle in a thread to avoid freezing GUI
        def generate():
            new_puzzle = get_random_puzzle()
            self.root.after(0, lambda: self.set_new_puzzle(new_puzzle))
        
        thread = threading.Thread(target=generate)
        thread.daemon = True
        thread.start()
    
    def set_new_puzzle(self, puzzle):
        """Set the new puzzle (called from main thread)"""
        self.initial_board = puzzle
        self.current_board = [row[:] for row in puzzle]
        self.update_display()
        self.status_label.config(text="New puzzle generated!", fg="green")
    
    def get_changed_cell(self, old_board, new_board):
        """Find which cell changed between two boards"""
        for i in range(9):
            for j in range(9):
                if old_board[i][j] != new_board[i][j]:
                    return (i, j)
        return None
    
    def solve_callback_functional(self, board):
        """Callback for functional solver - receives new immutable board"""
        if not self.solving:
            return
        
        # In fast mode, skip visualization
        if self.fast_mode:
            return
        
        changed_cell = self.get_changed_cell(self.current_board, board)
        self.current_board = [row[:] for row in board]
        self.update_display(changed_cell)
        time.sleep(self.solve_speed / 1000.0)
    
    def solve_callback_imperative(self, board):
        """Callback for imperative solver - receives mutable board reference"""
        if not self.solving:
            return
        
        # In fast mode, skip visualization
        if self.fast_mode:
            return
        
        changed_cell = self.get_changed_cell(self.current_board, board)
        self.current_board = [row[:] for row in board]
        self.update_display(changed_cell)
        time.sleep(self.solve_speed / 1000.0)
    
    def solve_functional_paradigm(self):
        """Solve using functional paradigm"""
        mode_text = " (Fast Mode)" if self.fast_mode else ""
        self.status_label.config(text=f"Solving with Functional Paradigm{mode_text}...", fg="green")
        board_copy = [row[:] for row in self.current_board]
        
        # Use callback only if not in fast mode
        callback = None if self.fast_mode else self.solve_callback_functional
        result = solve_functional(board_copy, callback)
        
        if result:
            self.current_board = result
            self.update_display()
            mode_text = " (Fast Mode)" if self.fast_mode else ""
            self.status_label.config(text=f"Solved! (Functional Paradigm{mode_text})", fg="green")
        else:
            self.status_label.config(text="No solution found", fg="red")
            messagebox.showerror("Error", "No solution exists for this puzzle")
    
    def solve_imperative_paradigm(self):
        """Solve using imperative paradigm"""
        mode_text = " (Fast Mode)" if self.fast_mode else ""
        self.status_label.config(text=f"Solving with Imperative Paradigm{mode_text}...", fg="green")
        board_copy = [row[:] for row in self.current_board]
        game = SudokuGame(board_copy)
        
        # Use callback only if not in fast mode
        callback = None if self.fast_mode else self.solve_callback_imperative
        success = game.solve_sudoku(callback)
        
        if success:
            self.current_board = game.board
            self.update_display()
            mode_text = " (Fast Mode)" if self.fast_mode else ""
            self.status_label.config(text=f"Solved! (Imperative Paradigm{mode_text})", fg="green")
        else:
            self.status_label.config(text="No solution found", fg="red")
            messagebox.showerror("Error", "No solution exists for this puzzle")
    
    def start_solving(self):
        """Start the solving process in a separate thread"""
        if self.solving:
            messagebox.showwarning("Warning", "Already solving!")
            return
        
        # Update fast mode from checkbox
        self.fast_mode = self.fast_mode_var.get()
        
        self.solving = True
        self.solve_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.new_puzzle_button.config(state=tk.DISABLED)
        
        # Run solving in a separate thread to keep GUI responsive
        paradigm = self.paradigm_var.get()
        thread = threading.Thread(
            target=self.solve_functional_paradigm if paradigm == "Functional" else self.solve_imperative_paradigm
        )
        thread.daemon = True
        thread.start()
        
        # Check when thread completes
        self.check_thread_completion(thread)
    
    def check_thread_completion(self, thread):
        """Check if solving thread has completed"""
        if thread.is_alive():
            self.root.after(100, lambda: self.check_thread_completion(thread))
        else:
            self.solving = False
            self.solve_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.new_puzzle_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()

