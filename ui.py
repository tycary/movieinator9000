import tkinter as tk

class SearchApp:
    def __init__(self):
        self.root = tk.Tk()

        self.frame = tk.Frame(self.root)

        self.label = tk.Label(self.frame, text="Search:")
        self.entry = tk.Entry(self.frame)
        self.button = tk.Button(self.frame, text="Search", command=self.search)

        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT)
        self.button.pack(side=tk.RIGHT)

        self.frame.pack()

        self.root.mainloop()

    def search(self):
        query = self.entry.get()

        # Perform the search.
        # ...

        # Display the search results.
        # ...


if __name__ == "__main__":
    app = SearchApp()