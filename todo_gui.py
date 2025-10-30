import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=40, height=10)
        self.listbox.pack(side=tk.LEFT, padx=(0,10))

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=(0,10))

        self.add_btn = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_btn.pack(side=tk.LEFT, padx=(20,5), pady=(0,10))

        self.del_btn = tk.Button(root, text="Delete Selected", width=15, command=self.delete_task)
        self.del_btn.pack(side=tk.LEFT, padx=5, pady=(0,10))

        self.clear_btn = tk.Button(root, text="Clear All", width=15, command=self.clear_tasks)
        self.clear_btn.pack(side=tk.LEFT, padx=5, pady=(0,10))

    def add_task(self):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected[0])
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()