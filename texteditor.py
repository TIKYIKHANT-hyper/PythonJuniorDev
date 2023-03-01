import tkinter as tk
from tkinter import filedialog
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root)
text.pack()

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        code = file.read()
        highlighted_code = highlight(code, PythonLexer(), HtmlFormatter())
        text.insert('1.0', highlighted_code)

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text.get('1.0', 'end'))

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack()

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

root.mainloop()
