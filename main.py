from api import MusicBrainzAPI
import tkinter as tk
from ui import ListItem, ScrollList

def main():
    api = MusicBrainzAPI()
    root = tk.Tk()
    root.geometry("1280x720")

    scroll_list = ScrollList(root)
    scroll_list.config(
        width=300
    )

    frame = tk.Frame(root, background="blue")

    releases = api.search_releases("Still Still Stellar")

    for release in releases:
        ListItem(scroll_list.interior, release).pack(anchor="nw", fill="x")

    scroll_list.pack(fill="y", side="left")
    frame.pack(expand=True, fill="both", side="left")

    root.mainloop()    


if __name__ == "__main__":
    main()
