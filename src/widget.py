import tkinter as tk

def label(root: tk, text_label: str, bg_color: str, f_family: str, f_size: int):
    element = tk.Label(root,
                       text=text_label,
                       bg=bg_color,
                       font=(f_family, f_size)
                       )
    return element

def entry(root: tk, bg_color: str, f_family: str, f_size: int, h_thick: int, h_bg: str, h_color: str):
    element = tk.Entry(root,
                       bg=bg_color,
                       font=(f_family, f_size),
                       highlightthickness=h_thick,
                       highlightbackground=h_bg,
                       highlightcolor=h_color
                       )
    return element

def button(root: tk, text_label: str, func, fg_color: str, bg_color: str, f_family: str, f_size: int, type: str, a_fg : str, a_bg: str):
    element = tk.Button(root,
                        text=text_label,
                        command=func,
                        fg=fg_color, 
                        bg=bg_color, 
                        font=(f_family, f_size),
                        bd=1,
                        padx=5,
                        relief=type,
                        activeforeground=a_fg, 
                        activebackground=a_bg
                        )
    return element