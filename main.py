import tkinter as tk
import json
import os

FILE_PATH = "save.json"

def save_state():
    """Gathers data and saves it to a JSON file."""
    app_data = {
        'score': label.cget("text")
    }
    with open(FILE_PATH, 'w') as f:
        json.dump(app_data, f)
    root.destroy() # Close the window after saving

def load_state():
    """Loads state from JSON file and populates widgets."""
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as f:
                app_data = json.load(f)
                content = app_data.get('score', '')
                if content:
                    label.config(text=content)
        except json.JSONDecodeError:
            print("Error reading saved state file.")
    else:
        print("No saved state file found.")

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

save_btn = tk.Button(root, text="Save and exit", command=save_state)
save_btn.pack(pady=5)

load_state()
root.mainloop()