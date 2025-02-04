import tkinter as tk
from tkinter import ttk
import math
import random
import subprocess


# create post_file in same directory as this script
post_file = "post.nc"

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
title_entry.insert(0, "Program1")

# Add labels and entries for the left side controls
work_offset_label = ttk.Label(left_frame, text="Work Offset")
work_offset_label.pack(anchor=tk.W, pady=5)
work_offset_entry = ttk.Entry(left_frame)
work_offset_entry.pack(fill=tk.X, pady=5)
work_offset_entry.insert(0, "G54")

tool_label = ttk.Label(left_frame, text="Tool Diameter")
tool_label.pack(anchor=tk.W, pady=5)
tool_entry = ttk.Entry(left_frame)
tool_entry.pack(fill=tk.X, pady=5)
tool_entry.insert(0, "0.5")


spindle_rpm_label = ttk.Label(left_frame, text="Spindle RPM")
spindle_rpm_label.pack(anchor=tk.W, pady=5)
spindle_rpm_entry = ttk.Entry(left_frame)
spindle_rpm_entry.pack(fill=tk.X, pady=5)
spindle_rpm_entry.insert(0, "8000")


feedrate_label = ttk.Label(left_frame, text="Feedrate")
feedrate_label.pack(anchor=tk.W, pady=5)
feedrate_entry = ttk.Entry(left_frame)
feedrate_entry.pack(fill=tk.X, pady=5)
feedrate_entry.insert(0, "10")

z_feedrate_label = ttk.Label(left_frame, text="Z Feedrate")
z_feedrate_label.pack(anchor=tk.W, pady=5)
z_feedrate_entry = ttk.Entry(left_frame)
z_feedrate_entry.pack(fill=tk.X, pady=5)
z_feedrate_entry.insert(0, "5")

z_clear_label = ttk.Label(left_frame, text="Z Clear")
z_clear_label.pack(anchor=tk.W, pady=5)
z_clear_entry = ttk.Entry(left_frame)
z_clear_entry.pack(fill=tk.X, pady=5)
z_clear_entry.insert(0, "3")

# Create a tab control
tab_control = ttk.Notebook(root)
face_tab = ttk.Frame(tab_control)
profile_tab = ttk.Frame(tab_control)
pocket_tab = ttk.Frame(tab_control)
drill_tab = ttk.Frame(tab_control)
#thread_tab = ttk.Frame(tab_control)
#engrave_tab = ttk.Frame(tab_control)
#dxf_tab = ttk.Frame(tab_control)

tab_control.add(face_tab, text="Face")
tab_control.add(profile_tab, text="Profile")
tab_control.add(pocket_tab, text="Pocket")
tab_control.add(drill_tab, text="Drill")
#tab_control.add(thread_tab, text="Thread Mill")
#tab_control.add(engrave_tab, text="Engrave")
#tab_control.add(dxf_tab, text="DXF")
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
x_start_label.grid(row=0, column=0, padx=2, pady=10, sticky="w")
x_start_entry = ttk.Entry(face_tab, width=5)
x_start_entry.grid(row=1, column=0, padx=2, pady=10, sticky="ew")
x_start_entry.insert(0, "0.000")

x_end_label = ttk.Label(face_tab, text="X End")
x_end_label.grid(row=0, column=7, padx=2, pady=10, sticky="w")
x_end_entry = ttk.Entry(face_tab, width=5)
x_end_entry.grid(row=1, column=7, padx=2, pady=10, sticky="ew")
x_end_entry.insert(0, "4.000")

y_start_label = ttk.Label(face_tab, text="Y Start")
y_start_label.grid(row=9, column=11, padx=2, pady=10, sticky="w")
y_start_entry = ttk.Entry(face_tab, width=5)
y_start_entry.grid(row=9, column=12, padx=2, pady=10, sticky="ew")
y_start_entry.insert(0, "0")
y_start_entry.insert(0, "0.000")

y_end_label = ttk.Label(face_tab, text="Y End")
y_end_label.grid(row=11, column=11, padx=2, pady=10, sticky="w")
y_end_entry = ttk.Entry(face_tab, width=5)
y_end_entry.grid(row=11, column=12, padx=2, pady=10, sticky="ew")
y_end_entry.insert(0, "2.000")

stepover_label = ttk.Label(face_tab, text="Stepover")
stepover_label.grid(row=10, column=11, padx=2, pady=10, sticky="w")
stepover_entry = ttk.Entry(face_tab, width=5)
stepover_entry.grid(row=10, column=12, padx=2, pady=10, sticky="ew")
stepover_entry.insert(0, "0.250")

z_start_label = ttk.Label(face_tab, text="Z Start")
z_start_label.grid(row=11, column=0, padx=2, pady=10, sticky="w")
z_start_entry = ttk.Entry(face_tab, width=5)
z_start_entry.grid(row=11, column=1, padx=2, pady=10, sticky="ew")
z_start_entry.insert(0, "0.000")

depth_label = ttk.Label(face_tab, text="Depth of cut")
depth_label.grid(row=12, column=5, padx=2, pady=10, sticky="w")
depth_entry = ttk.Entry(face_tab, width=5)
depth_entry.grid(row=12, column=6, padx=2, pady=10, sticky="ew")
depth_entry.insert(0, "0.100")

z_end_label = ttk.Label(face_tab, text="Z End")
z_end_label.grid(row=13, column=0, padx=2, pady=10, sticky="w")
z_end_entry = ttk.Entry(face_tab, width=5)
z_end_entry.grid(row=13, column=1, padx=2, pady=10, sticky="ew")
z_end_entry.insert(0, "-0.100")


spiral_var = tk.BooleanVar()
rectangular_var = tk.BooleanVar()
rectangular_var.set(True)
global face_mode
face_mode = "rectangular"
image = tk.PhotoImage(file="source_images/face_rectangle.png")
canvas = tk.Canvas(face_tab, width=300, height=300)
canvas.create_image(0, 0, anchor=tk.NW, image=image)
canvas.image = image  # Keep a reference to avoid garbage collection
canvas.grid(row=10, column=1, columnspan=9, padx=2, pady=10, sticky="ew")

def on_spiral_check():
    global face_mode
    if spiral_var.get():
        face_mode = "spiral"
        rectangular_var.set(False)
        image = tk.PhotoImage(file="source_images/face_spiral.png")
        canvas = tk.Canvas(face_tab, width=300, height=300)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image  # Keep a reference to avoid garbage collection
        canvas.grid(row=10, column=1, columnspan=9, padx=2, pady=10, sticky="ew")

def on_rectangular_check():
    global face_mode
    if rectangular_var.get():
        face_mode = "rectangular"
        spiral_var.set(False)
        image = tk.PhotoImage(file="source_images/face_rectangle.png")
        canvas = tk.Canvas(face_tab, width=300, height=300)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        canvas.image = image  # Keep a reference to avoid garbage collection
        canvas.grid(row=10, column=1, columnspan=9, padx=2, pady=10, sticky="ew")

rectangular_check = ttk.Checkbutton(face_tab, text="Rectangular", variable=rectangular_var, command=on_rectangular_check)
rectangular_check.grid(row=0, column=10, padx=2, pady=10, sticky="w")
spiral_check = ttk.Checkbutton(face_tab, text="Spiral", variable=spiral_var, command=on_spiral_check)
spiral_check.grid(row=1, column=10, padx=2, pady=10, sticky="w")

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
depth_profile_label.grid(row=9, column=0, padx=2, pady=10)
depth_profile_entry = ttk.Entry(profile_tab)
depth_profile_entry.grid(row=9, column=1, padx=2, pady=10)

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
#z_clear_label = ttk.Label(pocket_tab, text="Z Clear")
#z_clear_label.grid(row=8, column=0, padx=2, pady=10)
#z_clear_entry = ttk.Entry(pocket_tab)
#z_clear_entry.grid(row=8, column=1, padx=2, pady=10)

# Add buttons below Z Clear
button_frame = ttk.Frame(left_frame)
button_frame.pack(fill=tk.X, pady=10)

# add routine to run when "Post" button is clicked
def post():
    print("Post button clicked")
    print("Title:", title_entry.get())
    print("Work Offset:", work_offset_entry.get())
    print("Tool Diameter:", tool_entry.get())
    print("Spindle RPM:", spindle_rpm_entry.get())
    print("Feedrate (X & Y):", feedrate_entry.get())
    print("Feedrate (Z):", z_feedrate_entry.get())
    print("Z Clear:", z_clear_entry.get())
    print("Coolant:", coolant_state)
    print("Air:", air_state)

    # Determine which tab is currently selected
    tab = tab_control.index(tab_control.select())
    print("Tab:", tab)

    # get name of each tab
    tab_name = tab_control.tab(tab, "text")
    print("Tab Name:", tab_name)

    if tab_name == "Face":
        print("X Start:", x_start_entry.get())
        print("X End:", x_end_entry.get())
        print("Y Start:", y_start_entry.get())
        print("Y End:", y_end_entry.get())
        print("Stepover:", stepover_entry.get())
        print("Z Start:", z_start_entry.get())
        print("Depth of cut:", depth_entry.get())
        print("Z End:", z_end_entry.get())
        print("Z Clear:", z_clear_entry.get())

        # get valyes from entries
        x_start = float(x_start_entry.get())
        x_end = float(x_end_entry.get())
        y_start = float(y_start_entry.get())
        y_end = float(y_end_entry.get())
        stepover = float(stepover_entry.get())
        z_start = float(z_start_entry.get())
        depth = float(depth_entry.get())
        z_end = float(z_end_entry.get())
        depth = float(depth_entry.get())
        tool_diameter = float(tool_entry.get())
        z_feedrate = float(z_feedrate_entry.get())
        z_clear = float(z_clear_entry.get())
        feedrate = float(feedrate_entry.get())

        # Determine the number of Z passes needed
        z_passes = int((z_start - z_end) / depth) + 1

        commands = ""

        if face_mode == "rectangular":
            print("Rectangular button selected!")

            

            # Move to z_start
            commands += f"G0 Z{z_start:.4f} (move to Z start)\n"

            # Move to x_start, y_start
            commands += f"G0 X{x_start:.4f} Y{y_start:.4f} (move to X/Y start)\n"

            
            # Start at the current Z and move in steps toward z_end
            current_z = z_start
            while current_z > z_end:
                current_z -= depth
                if current_z < z_end:
                    current_z = z_end  # Clamp to final Z depth

                commands += f"G1 Z{current_z:.4f} (move to next cutting depth)\n"  # Lower to cutting depth

                # Generate raster pattern with CW/CCW transitions
                y = y_start
                direction = 1  # 1 for forward, -1 for reverse
                while y <= y_end:
                    # Move along Y axis
                    commands += f"G1 Y{y:.4f} (linear move in Y)\n"

                    # Move along X axis
                    x_target = x_end if direction == 1 else x_start
                    commands += f"G1 X{x_target+(direction * tool_diameter):.4f} (linear move in X)\n"

                    # Increment Y for the next line
                    y += stepover

                    # Check if we're done with all raster lines
                    if y > y_end:
                        break

                    # Circular transition to next raster line
                    x_next = x_target  # Maintain X position
                    y_next = y  # Next Y position
                    radius = tool_diameter / 4   # Set radius for the circular move

                    if direction == 1:  # Forward direction, use CW (G2)
                        commands += f"G3 X{x_next+0.5:.4f} Y{y_next:.4f} I0 J{radius} (CW move)\n"
                    else:  # Reverse direction, use CCW (G3)
                        commands += f"G2 X{x_next-0.5:.4f} Y{y_next:.4f} I0 J{radius} (CCW move)\n"

                    direction *= -1  # Reverse direction for the next raster line

            # Retract tool to safe Z height
            commands += f"G0 Z{z_clear:.4f}\n"
            print("done writing rectangular mode..")

            # commands are:
            print(commands)


        elif face_mode == "spiral":
            print("Spiral button selected!")
            commands += "(Spiral facing pattern)\n"

            # Move to z_start
            commands += f"G0 Z{z_start:.4f} (move to Z start)\n"

            # Move to x_start, y_start
            commands += f"G0 X{x_start:.4f} Y{y_start:.4f} (move to X/Y start)\n"

            # Start at the current Z and move in steps toward z_end
            current_z = z_start
            while current_z > z_end:
                current_z -= depth
                if current_z < z_end:
                    current_z = z_end  # Clamp to final Z depth

                commands += f"G1 Z{current_z:.4f} (move to next cutting depth)\n"  # Lower to cutting depth

                # Initialize the spiral pattern: start at the initial diameter and reduce step by step
                current_x_start = x_start
                current_x_end = x_end
                current_y = y_start

                # Move back and forth in linear passes
                while current_x_end > current_x_start:
                    # Move from current_x_start to current_x_end along the X axis
                    commands += f"G1 X{current_x_end:.4f} Y{current_y:.4f} (move to X{current_x_end:.4f}, Y{current_y:.4f})\n"
                    
                    # Move vertically down after reaching x_end
                    current_y -= stepover

                    # If we reach the center, stop
                    if current_x_end - current_x_start <= tool_diameter:
                        break

                    # Move back to current_x_start along the X axis
                    commands += f"G1 X{current_x_start:.4f} Y{current_y:.4f}  (move to X{current_x_start:.4f}, Y{current_y:.4f})\n"
                    
                    # Move vertically up after reaching x_start
                    current_y += stepover

                    # Reduce the horizontal range (move closer to the center)
                    current_x_start += tool_diameter / 2
                    current_x_end -= tool_diameter / 2

            # Retract tool to safe Z height
            commands += f"G0 Z{z_clear:.4f} (retract to safe Z height)\n"
                
            # open post file and write some lines
            # force a new file to be created

    
        with open(post_file, "w") as file:
            # force 



            file.write("G90 G94 (absolute positioning, feed per min)\n")
            file.write("G17 (XY plane selection)\n")
            file.write("G20 (inch)\n")
            file.write("G28 G91 Z0 (return to home)\n")
            file.write("G90 (absolute positioning)\n")


            
            # if coolant is on, write M8 and add comment in g code 
            if coolant_state:
                file.write("M8 (Coolant On)\n")
            # if air is on, write M7
            if air_state == True:
                file.write("M7 (air on)\n")

            print("Writing to post file...")

            # set spindle speed and turn on spindle
            file.write(f"S{spindle_rpm_entry.get()} M3  (spindle RPM, enable spindle)\n")
            file.write(f"{work_offset_entry.get()} (work offset)\n")
            file.write("G0 X" + x_start_entry.get() + " Y" + y_start_entry.get() + " Z" + z_start_entry.get() + "\n")
            file.write("M6 T1\n")
            file.write("S" + spindle_rpm_entry.get() + "\n")
            file.write("F" + feedrate_entry.get() + "\n")
            file.write("G43 H1 Z1\n")
            file.write("G1 Z" + z_end_entry.get() + "\n")
            file.write("G0 Z" + z_clear_entry.get() + "\n")
            

            file.write(commands)

            file.write("M30\n")

            print("Done. File closed.")


    pass

post_button = ttk.Button(button_frame, text="Post", command=post)
post_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)



append_button = ttk.Button(button_frame, text="Append")
append_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

# create button that opens output file when clicked
def open_output():
    print("Open button clicked")

    # open file as Mac
    try:
        subprocess.call(["open", "-a", "TextEdit", post_file])
    except:

        try:
        # open file as Windows
            subprocess.call(["notepad.exe", post_file])

        # open file as Linux
        except:
            subprocess.call(["gedit", post_file])


open_button = ttk.Button(button_frame, text="Open", command=open_output)
open_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


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
