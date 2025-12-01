import tkinter as tk

class ListItem(tk.Frame):
    def __init__(self, parent, release, info_frame):
        super().__init__(parent)
        self.config(padx=16, pady=12)

        self.release_title = tk.Label(self, text=release["title"],
                                      font=("TkDefaultFont", 12, "bold"),
                                      wraplength=264,
                                      justify="left") 
        self.release_artists = tk.Label(self, wraplength=264, justify="left", text=", ".join(release["artists"]))
        self.release_date = tk.Label(self, text=release["release_date"])
        self.release_id = tk.Label(self, text=release["id"], font=("tkDefaultFont", 8))
        self.view_button = tk.Button(self, text="View", font=("tkDefaultFont", 10), command=self.view_info)

        self.__info_frame = info_frame
        self.__id = release["id"]

        self.release_title.pack(anchor="nw")
        self.release_artists.pack(anchor="nw")
        self.release_date.pack(anchor="nw")
        self.release_id.pack(anchor="sw")
        self.view_button.pack(anchor="sw")

    def view_info(self):
        self.__info_frame.fill_info(self.__id)
