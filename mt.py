from tkinter import *
import tkinter.messagebox as msg

# Initialize the root window
root = Tk()
root.title("TIC-TAC-TOE")
root.configure(bg="#2C3E50")  # Set background color

# Initialize game variables
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
panels = [""] * 10
count = 0

# Function to check if a player has won
def win(panels, sign):
    return (
        (panels[1] == panels[2] == panels[3] == sign) or
        (panels[4] == panels[5] == panels[6] == sign) or
        (panels[7] == panels[8] == panels[9] == sign) or
        (panels[1] == panels[4] == panels[7] == sign) or
        (panels[2] == panels[5] == panels[8] == sign) or
        (panels[3] == panels[6] == panels[9] == sign) or
        (panels[1] == panels[5] == panels[9] == sign) or
        (panels[3] == panels[5] == panels[7] == sign)
    )

# Function to handle button clicks
def checker(digit):
    global count, digits, panels

    if digit in digits:
        digits.remove(digit)
        mark = "X" if count % 2 == 0 else "O"
        panels[digit] = mark
        
        buttons[digit].config(
            text=mark, state=DISABLED, font=("Times", 30, "bold"),
            disabledforeground="#EC7063" if mark == "X" else "#5DADE2"
        )
        
        # Check for win or draw
        if win(panels, mark):
            msg.showinfo("Result", f"Player {'1' if mark == 'X' else '2'} wins!")
            root.destroy()
        elif count == 8:  # Last move
            msg.showinfo("Result", "It's a Tie!")
            root.destroy()
        else:
            count += 1

# Create the UI for the game
Label(root, text="Player 1: X", font=("Times", 15), fg="white", bg="#2C3E50").grid(row=0, column=1)
Label(root, text="Player 2: O", font=("Times", 15), fg="white", bg="#2C3E50").grid(row=0, column=2)

# Create buttons and arrange them in a 3x3 grid
buttons = [None] * 10  # To store button references
for i in range(1, 10):
    buttons[i] = Button(
        root, text="", width=6, height=3, font=("Times", 20, "bold"),
        bg="#F8C471", fg="black", relief=RAISED, bd=5,
        activebackground="#D5DBDB",
        command=lambda digit=i: checker(digit)
    )
    buttons[i].grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3 + 1, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()