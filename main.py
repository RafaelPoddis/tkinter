import tkinter as tk

root = tk.Tk()

# Properties
root.title("Tela foda")
root.geometry("720x450")
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="0")
label.pack(pady=20)

def soma():
    current_value = int(label["text"])
    new_value = current_value + 1
    label.config(text=str(new_value))

sum_btn = tk.Button(root, text="Click!", command=soma)
sum_btn.pack(pady=5)

root.mainloop()