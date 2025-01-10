import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"),("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)
                root.title(f"Notepad - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                content = text_area.get("1.0", tk.END)
                file.write(content)
                root.title(f"Notepad - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

# Function to update a file
def update_file():
    if root.title().startswith("Notepad - "):
        file_path = root.title().replace("Notepad - ", "")
        try:
            with open(file_path, "w") as file:
                content = text_area.get("1.0", tk.END)
                file.write(content)
                messagebox.showinfo("Success", "File updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update file: {e}")
    else:
        messagebox.showwarning("Warning", "No file to update. Save the file first.")

root = tk.Tk()
root.title("Notepad")

text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Update", command=update_file)
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
