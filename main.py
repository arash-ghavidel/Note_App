import tkinter as tk
from tkinter import messagebox, filedialog

#making the main window
root = tk.Tk()
root.title("Note App")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.resizable(False, False)

#making the top menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#making file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# lbl_title = tk.Label(root, text="Note App")
# lbl_title.grid(row=0, column=0, columnspan=2)
txt_area = tk.Text(root, wrap="word")
txt_area.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")

def save_note():
    content = txt_area.get("1.0", tk.END)
    if content.strip() == "":
        messagebox.showwarning("Warning", "Note is empty!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")] )
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def open_note():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", ".txt")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            txt_area.delete("1.0", tk.END)
            txt_area.insert(tk.END, content)

def new_note():
    if messagebox.askyesno("Confirm", "Clear current note?"):
        txt_area.delete("1.0", tk.END)


#making the File menu items
file_menu.add_command(label="New | Ctrl + n", command=new_note)
file_menu.add_command(label="Open | Ctrl + o", command=open_note)
file_menu.add_command(label="Save | Ctrl + s", command=save_note)
file_menu.add_separator()
file_menu.add_command(label="Exit | Ctrl + e", command=root.quit)

#making shortcut keys
root.bind("<Control-s>", lambda event: save_note())
root.bind("<Control-o>", lambda event: open_note())
root.bind("<Control-n>", lambda event: new_note())
root.bind("<Control-e>", lambda event: root.quit())



frame = tk.Frame(root, height=50)
frame.grid(row=4, column=0, columnspan=2, sticky="nsew")
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
btn_save = tk.Button(frame, text="Save", command=save_note)
btn_save.grid(row=0, column=0, sticky="nsew")
btn_open = tk.Button(frame, text="Open", command=open_note)
btn_open.grid(row=0, column=1, sticky="nsew")

root.mainloop()