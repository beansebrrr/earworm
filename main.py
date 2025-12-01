from api import MusicBrainzAPI
import tkinter as tk
from ui import InfoFrame, ScrollList, SearchBar

def main():
    api = MusicBrainzAPI()

    # Boilerplate
    root = tk.Tk()
    root.title("Earworm: An album viewer")
    root.geometry("1280x720")
    root.columnconfigure(0, minsize=320)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    # Main components. Check the `ui` folder to view the special-looking ones
    header = tk.Label(root, text="🎵 Earworm 🎵", font=("tkDefaultFont", 14, "bold"), anchor="center")
    info_frame = InfoFrame(root, api)
    scroll_list = ScrollList(root, info_frame)
    search_bar = SearchBar(root, api, scroll_list)

    # Placement
    header.grid(column=0, row=0, columnspan=2, sticky="nsew")
    search_bar.grid(column=0, row=1, columnspan=2, sticky="nsew")
    scroll_list.grid(column=0, row=2, sticky="nsew")
    info_frame.grid(column=1, row=2, sticky="nsew")

    root.mainloop()


if __name__ == "__main__":
    main()
