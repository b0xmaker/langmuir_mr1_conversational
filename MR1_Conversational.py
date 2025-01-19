import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("MR1 Conversational")
root.geometry("1500x800")

# Create a frame for the left side controls
left_frame = ttk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=2, pady=10)

# Add labels and entries for the left side controls
title_label = ttk.Label(left_frame, text="Title:")
title_label.pack(anchor=tk.W, pady=5)
title_entry = ttk.Entry(left_frame)
title_entry.pack(fill=tk.X, pady=5)

# Add labels and entries for the left side controls
work_offset_label = ttk.Label(left_frame, text="Work Offset")
work_offset_label.pack(anchor=tk.W, pady=5)
work_offset_entry = ttk.Entry(left_frame)
work_offset_entry.pack(fill=tk.X, pady=5)

tool_label = ttk.Label(left_frame, text="Tool")
tool_label.pack(anchor=tk.W, pady=5)
tool_entry = ttk.Entry(left_frame)
tool_entry.pack(fill=tk.X, pady=5)

spindle_rpm_label = ttk.Label(left_frame, text="Spindle RPM")
spindle_rpm_label.pack(anchor=tk.W, pady=5)
spindle_rpm_entry = ttk.Entry(left_frame)
spindle_rpm_entry.pack(fill=tk.X, pady=5)

feedrate_label = ttk.Label(left_frame, text="Feedrate")
feedrate_label.pack(anchor=tk.W, pady=5)
feedrate_entry = ttk.Entry(left_frame)
feedrate_entry.pack(fill=tk.X, pady=5)

z_feedrate_label = ttk.Label(left_frame, text="Z Feedrate")
z_feedrate_label.pack(anchor=tk.W, pady=5)
z_feedrate_entry = ttk.Entry(left_frame)
z_feedrate_entry.pack(fill=tk.X, pady=5)

z_clear_label = ttk.Label(left_frame, text="Z Clear")
z_clear_label.pack(anchor=tk.W, pady=5)
z_clear_entry = ttk.Entry(left_frame)
z_clear_entry.pack(fill=tk.X, pady=5)

# Create a tab control
tab_control = ttk.Notebook(root)
face_tab = ttk.Frame(tab_control)
profile_tab = ttk.Frame(tab_control)
pocket_tab = ttk.Frame(tab_control)
drill_tab = ttk.Frame(tab_control)
thread_tab = ttk.Frame(tab_control)
engrave_tab = ttk.Frame(tab_control)
dxf_tab = ttk.Frame(tab_control)

tab_control.add(face_tab, text="Face")
tab_control.add(profile_tab, text="Profile")
tab_control.add(pocket_tab, text="Pocket")
tab_control.add(drill_tab, text="Drill")
tab_control.add(thread_tab, text="Thread Mill")
tab_control.add(engrave_tab, text="Engrave")
tab_control.add(dxf_tab, text="DXF")
tab_control.pack(expand=1, fill="both")

# Configure the grid
face_tab.columnconfigure(0, weight=1)
face_tab.columnconfigure(1, weight=1)
face_tab.columnconfigure(2, weight=1)
face_tab.columnconfigure(3, weight=1)
face_tab.columnconfigure(4, weight=1)
face_tab.columnconfigure(5, weight=1)
face_tab.columnconfigure(6, weight=1)
face_tab.columnconfigure(7, weight=1)
face_tab.columnconfigure(8, weight=1)
face_tab.columnconfigure(9, weight=1)
face_tab.columnconfigure(10, weight=1)

# Add input fields for Face tab
x_start_label = ttk.Label(face_tab, text="X Start")
x_start_label.grid(row=1, column=0, padx=2, pady=10, sticky="w")
x_start_entry = ttk.Entry(face_tab, width=5)
x_start_entry.grid(row=1, column=1, padx=2, pady=10, sticky="ew")

x_end_label = ttk.Label(face_tab, text="X End")
x_end_label.grid(row=1, column=4, padx=2, pady=10, sticky="w")
x_end_entry = ttk.Entry(face_tab, width=5)
x_end_entry.grid(row=1, column=5, padx=2, pady=10, sticky="ew")

y_start_label = ttk.Label(face_tab, text="Y Start")
y_start_label.grid(row=1, column=7, padx=2, pady=10, sticky="w")
y_start_entry = ttk.Entry(face_tab, width=5)
y_start_entry.grid(row=1, column=8, padx=2, pady=10, sticky="ew")

y_end_label = ttk.Label(face_tab, text="Y End")
y_end_label.grid(row=7, column=7, padx=2, pady=10, sticky="w")
y_end_entry = ttk.Entry(face_tab, width=5)
y_end_entry.grid(row=7, column=8, padx=2, pady=10, sticky="ew")

stepover_label = ttk.Label(face_tab, text="Stepover")
stepover_label.grid(row=8, column=11, padx=2, pady=10, sticky="w")
stepover_entry = ttk.Entry(face_tab, width=5)
stepover_entry.grid(row=8, column=12, padx=2, pady=10, sticky="ew")

z_start_label = ttk.Label(face_tab, text="Z Start")
z_start_label.grid(row=11, column=0, padx=2, pady=10, sticky="w")
z_start_entry = ttk.Entry(face_tab, width=5)
z_start_entry.grid(row=11, column=1, padx=2, pady=10, sticky="ew")

depth_label = ttk.Label(face_tab, text="Depth of cut")
depth_label.grid(row=13, column=0, padx=2, pady=10, sticky="w")
depth_entry = ttk.Entry(face_tab, width=5)
depth_entry.grid(row=13, column=1, padx=2, pady=10, sticky="ew")

z_end_label = ttk.Label(face_tab, text="Z End")
z_end_label.grid(row=11, column=5, padx=2, pady=10, sticky="w")
z_end_entry = ttk.Entry(face_tab, width=5)
z_end_entry.grid(row=11, column=6, padx=2, pady=10, sticky="ew")


spiral_var = tk.BooleanVar()
rectangular_var = tk.BooleanVar()
rectangular_var.set(True)


def on_spiral_check():
    if spiral_var.get():
        rectangular_var.set(False)
        image = tk.PhotoImage(file="source_images/face_spiral.png")
        canvas = tk.Canvas(face_tab, width=300, height=300)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image  # Keep a reference to avoid garbage collection
        canvas.grid(row=8, column=1, columnspan=9, padx=2, pady=10, sticky="ew")

def on_rectangular_check():
    if rectangular_var.get():
        spiral_var.set(False)
        image = tk.PhotoImage(file="source_images/face_rectangle.png")
        canvas = tk.Canvas(face_tab, width=300, height=300)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image  # Keep a reference to avoid garbage collection
        canvas.grid(row=8, column=1, columnspan=9, padx=2, pady=10, sticky="ew")

spiral_check = ttk.Checkbutton(face_tab, text="Spiral", variable=spiral_var, command=on_spiral_check)
spiral_check.grid(row=9, column=0, padx=2, pady=10, sticky="w")
rectangular_check = ttk.Checkbutton(face_tab, text="Rectangular", variable=rectangular_var, command=on_rectangular_check)
rectangular_check.grid(row=9, column=1, padx=2, pady=10, sticky="w")

# Add input fields for Profile tab:
# X Profile Start, X Profile End, Y Profile Start, Y Profile End, Z Profile Start, Z Profile End, Stepover, Depth of Cut
x_profile_start_label = ttk.Label(profile_tab, text="X Profile Start")
x_profile_start_label.grid(row=1, column=0, padx=2, pady=10)
x_profile_start_entry = ttk.Entry(profile_tab)
x_profile_start_entry.grid(row=1, column=1, padx=2, pady=10)

y_profile_start_label = ttk.Label(profile_tab, text="Y Profile Start")
y_profile_start_label.grid(row=2, column=0, padx=2, pady=10)
y_profile_start_entry = ttk.Entry(profile_tab)
y_profile_start_entry.grid(row=2, column=1, padx=2, pady=10)

x_profile_end_label = ttk.Label(profile_tab, text="X Profile End")
x_profile_end_label.grid(row=3, column=0, padx=2, pady=10)
x_profile_end_entry = ttk.Entry(profile_tab)
x_profile_end_entry.grid(row=3, column=1, padx=2, pady=10)

y_profile_end_label = ttk.Label(profile_tab, text="Y Profile End")
y_profile_end_label.grid(row=4, column=0, padx=2, pady=10)
y_profile_end_entry = ttk.Entry(profile_tab)
y_profile_end_entry.grid(row=4, column=1, padx=2, pady=10)

z_profile_start_label = ttk.Label(profile_tab, text="Z Profile Start")
z_profile_start_label.grid(row=5, column=0, padx=2, pady=10)
z_profile_start_entry = ttk.Entry(profile_tab)
z_profile_start_entry.grid(row=5, column=1, padx=2, pady=10)

z_profile_end_label = ttk.Label(profile_tab, text="Z Profile End")
z_profile_end_label.grid(row=6, column=0, padx=2, pady=10)
z_profile_end_entry = ttk.Entry(profile_tab)
z_profile_end_entry.grid(row=6, column=1, padx=2, pady=10)

stepover_profile_label = ttk.Label(profile_tab, text="Stepover")
stepover_profile_label.grid(row=7, column=3, padx=2, pady=10)
stepover_profile_entry = ttk.Entry(profile_tab)
stepover_profile_entry.grid(row=7, column=4, padx=2, pady=10)

depth_profile_label = ttk.Label(profile_tab, text="Depth of cut")
depth_profile_label.grid(row=8, column=0, padx=2, pady=10)
depth_profile_entry = ttk.Entry(profile_tab)
depth_profile_entry.grid(row=8, column=1, padx=2, pady=10)

# Add input fields for Pocket tab:
# X Width, Radius, Stepover, Y Height, Depth of Cut, Z Start, Z End, Z Clear

x_width_label = ttk.Label(pocket_tab, text="X Width")
x_width_label.grid(row=1, column=0, padx=2, pady=10)
x_width_entry = ttk.Entry(pocket_tab)
x_width_entry.grid(row=1, column=1, padx=2, pady=10)
radius_label = ttk.Label(pocket_tab, text="Radius")
radius_label.grid(row=2, column=0, padx=2, pady=10)
radius_entry = ttk.Entry(pocket_tab)
radius_entry.grid(row=2, column=1, padx=2, pady=10)
stepover_pocket_label = ttk.Label(pocket_tab, text="Stepover")
stepover_pocket_label.grid(row=3, column=0, padx=2, pady=10)
stepover_pocket_entry = ttk.Entry(pocket_tab)
stepover_pocket_entry.grid(row=3, column=1, padx=2, pady=10)
y_height_label = ttk.Label(pocket_tab, text="Y Height")
y_height_label.grid(row=4, column=0, padx=2, pady=10)
y_height_entry = ttk.Entry(pocket_tab)
y_height_entry.grid(row=4, column=1, padx=2, pady=10)
depth_pocket_label = ttk.Label(pocket_tab, text="Depth of cut")
depth_pocket_label.grid(row=5, column=0, padx=2, pady=10)
depth_pocket_entry = ttk.Entry(pocket_tab)
depth_pocket_entry.grid(row=5, column=1, padx=2, pady=10)
z_start_pocket_label = ttk.Label(pocket_tab, text="Z Start")
z_start_pocket_label.grid(row=6, column=0, padx=2, pady=10)
z_start_pocket_entry = ttk.Entry(pocket_tab)
z_start_pocket_entry.grid(row=6, column=1, padx=2, pady=10)
z_end_pocket_label = ttk.Label(pocket_tab, text="Z End")
z_end_pocket_label.grid(row=7, column=0, padx=2, pady=10)
z_end_pocket_entry = ttk.Entry(pocket_tab)
z_end_pocket_entry.grid(row=7, column=1, padx=2, pady=10)
z_clear_label = ttk.Label(pocket_tab, text="Z Clear")
z_clear_label.grid(row=8, column=0, padx=2, pady=10)
z_clear_entry = ttk.Entry(pocket_tab)
z_clear_entry.grid(row=8, column=1, padx=2, pady=10)

# Add buttons below Z Clear
button_frame = ttk.Frame(left_frame)
button_frame.pack(fill=tk.X, pady=10)

post_button = ttk.Button(button_frame, text="Post")
post_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

append_button = ttk.Button(button_frame, text="Append")
append_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

coolant_state = True
air_state = True

def toggle_coolant():
    global coolant_state
    if coolant_state:
        coolant_button.config(text="Coolant ON")
    else:
        coolant_button.config(text="Coolant OFF")
    coolant_state = not coolant_state

coolant_button = ttk.Button(button_frame, text="Coolant OFF", command=toggle_coolant)
coolant_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


def toggle_air():
    global air_state
    if air_state:
        air_button.config(text="Air ON")
    else:
        air_button.config(text="Air OFF")
    air_state = not air_state

air_button = ttk.Button(button_frame, text="Air OFF", command=toggle_air)
air_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


# Add input fields for Drill tab:
# Create a table for input values
# First column of table is 1, 2, 3, ... n
# Second column of table is labeled "X"
# Third column of table is labeled "Y"

# Add a button for each of: Raise, Lower, Insert Row, Delete, Clear All

# Create a table for Drill tab
drill_table = ttk.Treeview(drill_tab, columns=("X", "Y"), show="headings")
# Insert row numbers
drill_table.heading("#1", text="#")
drill_table.column("#1", width=50)

drill_table.heading("X", text="X")
drill_table.heading("Y", text="Y")
drill_table.grid(row=1, column=0, columnspan=2, padx=2, pady=10)

# Add buttons for Raise, Lower, Insert Row, Delete, Clear All
def insert_row():
    drill_table.insert("", "end", values=(drill_table.index("end") + 1, "", ""))

def delete_row():
    selected_item = drill_table.selection()
    if selected_item:
        drill_table.delete(selected_item)

def clear_all():
    for item in drill_table.get_children():
        drill_table.delete(item)

def raise_row():
    selected_item = drill_table.selection()
    if selected_item:
        index = drill_table.index(selected_item)
        if index > 0:
            drill_table.move(selected_item, "", index - 1)

def lower_row():
    selected_item = drill_table.selection()
    if selected_item:
        index = drill_table.index(selected_item)
        if index < len(drill_table.get_children()) - 1:
            drill_table.move(selected_item, "", index + 1)

insert_button = ttk.Button(drill_tab, text="Insert Row", command=insert_row)
insert_button.grid(row=2, column=0, padx=2, pady=10)
delete_button = ttk.Button(drill_tab, text="Delete", command=delete_row)
delete_button.grid(row=2, column=1, padx=2, pady=10)
clear_button = ttk.Button(drill_tab, text="Clear All", command=clear_all)
clear_button.grid(row=3, column=0, padx=2, pady=10)
raise_button = ttk.Button(drill_tab, text="Raise", command=raise_row)
raise_button.grid(row=3, column=1, padx=2, pady=10)
lower_button = ttk.Button(drill_tab, text="Lower", command=lower_row)
lower_button.grid(row=4, column=0, padx=2, pady=10)



# Run the main loop
root.mainloop()
