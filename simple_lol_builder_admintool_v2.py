import tkinter as tk
from tkinter import ttk
import json


# initialize main window
root = tk.Tk()
root.title("Simple LoL Builder - Admin Tool V2")
root.geometry("600x400") # change window size if needed here

# load skill file and extract champions for champion_dropdown
with open("skills.json", "r") as f:
    skills_data = json.load(f)
    champion_names = sorted(list(skills_data.keys()))

# dropdown variables
champion_var = tk.StringVar()
lane_var = tk.StringVar()
role_var = tk.StringVar()

# champ label + dropdown
tk.Label(root, text="Champion:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
champion_dropdown = ttk.Combobox(root, textvariable=champion_var, values=champion_names)
champion_dropdown.grid(row=0, column=1, padx=10, pady=5)

# lane label + dropdown
tk.Label(root, text="Lane:").grid(row=1, column=1, sticky="w", padx=10, pady=5)
lane_dropdown = ttk.Combobox(root, textvariable=lane_var, values = ["Top", "Jungle", "Mid", "Bot", "Support"], state="readonly")
lane_dropdown.grid(row=1, column=1, padx=10, pady=5)

# role label + dropdown
tk.Label(root, text="role:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
role_dropdown = ttk.Combobox(root, textvariable=role_var, values=["Ad", "Ap", "Bruiser", "Tank", "Splitpush", "Assassin"], state="readonly")
role_dropdown.grid(row=2, column=1, padx=10, pady=5)