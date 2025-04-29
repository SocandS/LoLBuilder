import json
import tkinter as tk
from tkinter import ttk

#load items
try:
    with open("items.json", "r") as f:
        items_data = json.load(f)
        item_names = list(items_data.keys())
except FileNotFoundError:
    item_names = []

def save_build():
    # gather inputs
    champ = champion_entry.get().title()
    lane = lane_var.get().title()
    role = role_var.get().title()
    items = [items_listbox.get(i) for i in items_listbox.curselection()]
    runes = [rune.strip() for rune in runes_entry.get().split(",")]
    skills = [skill.strip() for skill in skills_entry.get().split(",")]
    summoners = [summoner.strip() for summoner in summoner_entry.get().split(",")]

    # create build dictionary
    new_build = {
        "items": items,
        "runes": runes,
        "skills": skills,
        "summoner_spells": summoners
    }
    
    #create build directory
    try:
        with open("champion_builds.json", "r") as f:
            builds = json.load(f)
    except FileNotFoundError:
        builds = {}
    
    #insert/update builds
    if champ not in builds:
        builds[champ] = {}
    if lane not in builds[champ]:
        builds[champ][lane] = {}
    builds[champ][lane][role] = new_build


    #read existing file - if it exists
    with open("champion_builds.json", "w") as f:
        json.dump(builds, f, indent=4)

    #clear the fields after saving
    champion_entry.delete(0, tk.END)
    lane_var.set("")
    role_var.set("")
    items_listbox.select_clear(0, tk.END)
    runes_entry.delete(0, tk.END)
    skills_entry.delete(0, tk.END)
    summoner_entry.delete(0, tk.END)


# main window
root = tk.Tk()
root.title("Simple LOL Builder Admin Tool")

# champ input
tk.Label(root, text="Champion:").grid(row=0, column=0, sticky="w")
champion_entry = tk.Entry(root)
champion_entry.grid(row=0, column=1)

# lane dropdown
tk.Label(root, text="Lane:").grid(row=1, column=0, sticky="w")
lane_var = tk.StringVar()
lane_dropdown = ttk.Combobox(root, textvariable=lane_var, values=["Top", "Jungle", "Mid", "Bot", "Support"], state="readonly")
lane_dropdown.grid(row=1, column=1)

# role dropdown
tk.Label(root, text="Role:").grid(row=2, column=0, sticky="w")
role_var = tk.StringVar()
role_dropdown = ttk.Combobox(root, textvariable=role_var, values=["Ad", "Ap", "Bruiser", "Assassin", "Split Push", "Tank", "Enchantress"], state="readonly")
role_dropdown.grid(row=2, column=1)

# item input
tk.Label(root, text="Items (Hold CTRL to select multiple):").grid(row=3, column=0, sticky="w")
items_listbox = tk.Listbox(root, selectmode="multiple", height=10, exportselection=0)
for item in item_names:
    items_listbox.insert(tk.END, item)
items_listbox.grid(row=3, column=1)

# Rune Input
tk.Label(root, text="Runes (Comma Separated):").grid(row=4, column=0, sticky="w")
runes_entry = tk.Entry(root)
runes_entry.grid(row=4, column=1)

# skills input
tk.Label(root, text="Skills (Comma Separated):").grid(row=5, column=0, sticky="w")
skills_entry = tk.Entry(root)
skills_entry.grid(row=5, column=1)

# summoner spell input
tk.Label(root, text="Summoner Spells (Comma Separated):").grid(row=6, column=0, sticky="w")
summoner_entry = tk.Entry(root)
summoner_entry.grid(row=6, column=1)

# save button - function written later
save_button = tk.Button(root, text="Save Build", command=save_build)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

# start GUI event loop
root.mainloop()
