import tkinter as tk
from tkinter import PhotoImage
from bb import *

def start_game():
    root.withdraw()  # Hide the intro window
    bb.start_main_window()  # Start the main window

def quit_game():
    root.quit()  # Exit the application

# Create the intro window
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("400x300")
root.resizable(False, False)  # Disable window resizing

# Set the background image
bg_image = PhotoImage(file="src/assets/dice2.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create the Start button
start_button = tk.Button(root, text="Start", font=("Arial", 16), bg="green", fg="white", command=start_game)
start_button.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.15)

# Create the Quit button
quit_button = tk.Button(root, text="Quit", font=("Arial", 16), bg="red", fg="white", command=quit_game)
quit_button.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.15)

# Start the intro window loop
root.mainloop()