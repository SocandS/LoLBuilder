import tkinter as tk
from tkinter import ttk
import json
#call the builds library
with open('builds.json', 'r') as f:
    champion_builds = json.load(f)


# Function to get build info
def get_build(champion, lane, role):
    try:
        return champion_builds[champion][lane][role]
    except KeyError:
        return {
            "items": ["N/A"],
            "skills": ["N/A"],
            "runes": ["N/A"],
            "summoner_spells": ["Not currently available, please check back."]
        }

# Callback when "Get Build" is clicked
def show_build():
    champ = champ_var.get().title()
    lane = lane_var.get().title()
    role = role_var.get().title()

    build = get_build(champ, lane, role)

    result_text.config(state="normal")  # Allow editing the text box
    result_text.delete("1.0", tk.END)    # Clear previous results

    result_text.insert(tk.END, f"{champ.title()} ({lane.title()} {role.title()}) Build:\n\n")

    result_text.insert(tk.END, "Summoner Spells:\n")
    for sums in build["summoner_spells"]:
        result_text.insert(tk.END, f"- {sums}\n")

    result_text.insert(tk.END, "\nRunes:\n")
    for rune in build["runes"]:
        result_text.insert(tk.END, f"- {rune}\n")

    result_text.insert(tk.END, "\nItems:\n")
    for item in build["items"]:
        result_text.insert(tk.END, f"- {item}\n")

    result_text.insert(tk.END, "\nSkills:\n")
    result_text.insert(tk.END, " > " + " → ".join(build["skills"]))

    result_text.config(state="disabled")  # Make text box read-only after displaying

# Callback to clear everything
def reset_fields():
    champ_var.set("Udyr")
    lane_var.set("Top")
    role_var.set("Tank")
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("League of Legends Build Planner")

# Dropdown Options
champion_options = ["Udyr", "Shaco", "Trundle"]
lane_options = ["Top", "Jungle", "Mid", "Bot", "Support"]
role_options = ["Tank", "AD", "AP", "Bruiser"]

# Variables
champ_var = tk.StringVar(value="Udyr")
lane_var = tk.StringVar(value="Top")
role_var = tk.StringVar(value="Tank")

# Labels + Dropdowns
tk.Label(root, text="Champion:").grid(row=0, column=0, sticky="w")
ttk.Combobox(root, textvariable=champ_var, values=champion_options, state="readonly").grid(row=0, column=1)

tk.Label(root, text="Lane:").grid(row=1, column=0, sticky="w")
ttk.Combobox(root, textvariable=lane_var, values=lane_options, state="readonly").grid(row=1, column=1)

tk.Label(root, text="Role:").grid(row=2, column=0, sticky="w")
ttk.Combobox(root, textvariable=role_var, values=role_options, state="readonly").grid(row=2, column=1)

# Buttons
tk.Button(root, text="Get Build", command=show_build).grid(row=3, column=0, pady=10)
tk.Button(root, text="Reset", command=reset_fields).grid(row=3, column=1, pady=10)

# Results Display
result_text = tk.Text(root, height=20, width=50, state="disabled")
result_text.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
