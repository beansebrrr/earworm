import tkinter as tk

class ListItem(tk.Frame):
    def __init__(self, parent, release):
        super().__init__(parent)
        self.config(
            padx=4, pady=8
        )

        self.release_title = tk.Label(
            self, text=release["title"],
            font=("TkDefaultFont", 12, "bold")
        ) 
        self.release_artists = tk.Label(self, text=", ".join(release["artists"]))
        self.release_date = tk.Label(self, text=release["release_date"])
        self.release_id = tk.Label(self, text=release["id"])
        self.view_button = tk.Button(self, text="View")

        self.release_title.pack(anchor="nw")
        self.release_artists.pack(anchor="nw")
        self.release_date.pack(anchor="nw")
        self.release_id.pack(anchor="nw")
        self.view_button.place(relx=1, rely=0, anchor="ne")