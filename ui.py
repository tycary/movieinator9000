import tkinter as tk
from tkinter import ttk

def update_results(*args):
    search_query = entry.get().lower()
    filtered_results = [result for result in all_results if search_query in result.lower()]
    listbox.delete(0, tk.END)  # Clear previous results
    for result in filtered_results:
        listbox.insert(tk.END, result)

def on_resize(event):
    # Calculate the new font size based on the window size
    new_font_size = max(8, min(20, int((event.width + event.height) / 40)))

    # Update fonts for entry, search_button, and listbox
    entry_font = ("Helvetica", new_font_size)
    search_button_font = ("Helvetica", new_font_size)
    listbox_font = ("Helvetica", new_font_size)
    # Update the button font using the style option
    search_button_style = ttk.Style()

    entry.configure(font=entry_font)
    listbox.configure(font=listbox_font)
    search_button_style.configure("TButton", font=search_button_font)

# Sample list of results
all_results = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Strawberry"]

# Create the main window
root = tk.Tk()
root.title("Search App")

# Set dark theme colors
dark_bg_color = "#36393F"  # Discord dark theme background color
entry_bg_color = "#40444B"  # Entry background color
button_bg_color = "#7289DA"  # Discord purple button color
button_hover_color = "#677BC4"  # Discord purple button color on hover
button_fg_color = "#FFFFFF"  # Button text color
listbox_bg_color = "#2C2F33"  # Listbox background color
listbox_fg_color = "#FFFFFF"  # Listbox text color

root.configure(bg=dark_bg_color)

# Set weights for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Create and place the search bar with dark theme
entry_style = ttk.Style()
entry_style.configure("TEntry", fieldbackground=entry_bg_color, foreground="white")
entry = ttk.Entry(root, font=("Helvetica", 12))
entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
entry.bind("<KeyRelease>", update_results)  # Bind the function to key release event

# Create and place the search button with a placeholder icon
button_style = ttk.Style()
button_style.configure("TButton", background=button_bg_color, foreground=button_fg_color)
button_style.map("TButton", background=[("active", button_hover_color)])
search_icon = tk.PhotoImage(width=1, height=1)  # Create a 1x1 transparent image
search_button = ttk.Button(root, image=search_icon, command=update_results, text="Search", compound="left")
search_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Create and place the listbox for search results with dark theme
listbox = tk.Listbox(root, width=30, height=10, font=("Helvetica", 12), selectbackground=button_hover_color)  # Initial font size
listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
listbox.configure(bg=listbox_bg_color, fg=listbox_fg_color, selectbackground=button_hover_color)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root, command=listbox.yview)
scrollbar.grid(row=1, column=2, sticky='nsew')
listbox['yscrollcommand'] = scrollbar.set

# Bind the on_resize function to window resize event
root.bind("<Configure>", on_resize)

# Populate the initial list of results
for result in all_results:
    listbox.insert(tk.END, result)

# Run the Tkinter event loop
root.mainloop()
