import os
import json
import tkinter as tk

FILE_PATH = "save.json"

def save_state():
    """Gathers data and saves it to a JSON file."""
    app_data = {
        'score': valueLabel.cget("text")
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
                    valueLabel.config(text=content)
        except json.JSONDecodeError:
            print("Error reading saved state file.")
    else:
        print("No saved state file found.")

root = tk.Tk()

# Properties
root.title("Tela foda")
root.geometry("720x450")
# root.configure(bg="#1e1e1e")

# Variables
upgrade_click_count = 1
upgrade_click_cost = 100

# Score Labels
label1 = tk.Label(root, text="Dinheiros: ")
label1.grid(row=0, column=0, padx=5, pady=10)
valueLabel = tk.Label(root, text="0")
valueLabel.grid(row=0, column=1, pady=10)

# ====================
# === Handle Score ===
# ====================
def soma():
    current_value = int(valueLabel["text"])
    new_value = current_value + 1
    valueLabel.config(text=str(new_value))

sum_btn = tk.Button(root, text="Click!", command=soma)
sum_btn.grid(row=1, column=0, pady=5)

# Save Button
save_btn = tk.Button(root, text="Save and exit", command=save_state)
save_btn.place(relx=0.97, rely=0.03, anchor="ne")

load_state()
root.mainloop()