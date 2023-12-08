import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets

class MovieSelectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Selection App")

        # Set the default window size to 1920x1080 pixels
        self.root.geometry("1920x1080")

        # Center the main window on the screen
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))

        # Manually set dark theme colors
        self.root.configure(bg="#36393f")  # Discord's dark theme background color

        # Use a themed style for a dark theme (similar to Discord)
        self.style = ttk.Style()
        self.style.theme_use("alt")  # Choose a dark theme (e.g., "alt")

        # Configure style for Listbox
        self.style.configure("TListbox", background="#2c2f33", fieldbackground="#2c2f33", foreground="#ffffff", selectbackground="#7289da", selectforeground="#ffffff")

        # Search Bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=40, bg="#2c2f33", fg="#ffffff", insertbackground="white")
        self.search_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Search Button (Mocked functionality)
        search_button = tk.Button(root, text="Search", command=self.mock_search, bg="#7289da", fg="#ffffff", width=15)
        search_button.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        # Left Listbox for Search Results
        self.results_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=20, bg="#2c2f33", fg="#ffffff", selectbackground="#7289da", selectforeground="#ffffff")
        self.results_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Right Listbox for Selected Movies
        self.selected_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=20, bg="#2c2f33", fg="#ffffff", selectbackground="#7289da", selectforeground="#ffffff")
        self.selected_listbox.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        # Arrows to Move Movies
        move_right_button = tk.Button(root, text=">", command=self.move_right, bg="#7289da", fg="#ffffff", width=5, height=2)
        move_right_button.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")
        
        move_left_button = tk.Button(root, text="<", command=self.move_left, bg="#7289da", fg="#ffffff", width=5, height=2)
        move_left_button.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

        # Generate Button
        generate_button = tk.Button(root, text="Generate List", command=self.generate_list, bg="#7289da", fg="#ffffff", width=15)
        generate_button.grid(row=3, column=1, pady=10, sticky="ew")

        # Configure row and column weights for scaling
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

    def mock_search(self):
        # Mocked Search Functionality
        search_query = self.search_var.get()
        # Replace this with actual movie search logic
        # For now, let's just add some mock results
        results = ["Movie 1 - Cast 1", "Movie 2 - Cast 2", "Movie 3 - Cast 3"]
        self.update_results_list(results)

    def update_results_list(self, results):
        # Clear previous results
        self.results_listbox.delete(0, tk.END)
        # Add new results to the listbox
        for result in results:
            self.results_listbox.insert(tk.END, result)

    def move_right(self):
        # Move selected item from left to right
        selected_index = self.results_listbox.curselection()
        if selected_index:
            selected_movie = self.results_listbox.get(selected_index)
            self.selected_listbox.insert(tk.END, selected_movie)
            self.results_listbox.delete(selected_index)

    def move_left(self):
        # Move selected item from right to left
        selected_index = self.selected_listbox.curselection()
        if selected_index:
            selected_movie = self.selected_listbox.get(selected_index)
            self.results_listbox.insert(tk.END, selected_movie)
            self.selected_listbox.delete(selected_index)

    def generate_list(self):
        # Get selected movies on the right side and compile them into a list
        selected_movies = list(self.selected_listbox.get(0, tk.END))
        print("Generated List:", selected_movies)
        # Add further processing or saving logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieSelectionApp(root)
    root.mainloop()