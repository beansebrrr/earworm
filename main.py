from api import MusicBrainzAPI
import tkinter as tk
from ui import InfoFrame, ScrollList, SearchBar

def main():
    api = MusicBrainzAPI()
    root = tk.Tk()
    root.geometry("1280x720")
    root.columnconfigure(0, minsize=320)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)

    scroll_list = ScrollList(root)
    search_bar = SearchBar(root, api, scroll_list)
    info_frame = InfoFrame(root, api)

    scroll_list.connect_to_info_frame(info_frame)

    search_bar.grid(column=0, row=0, columnspan=2, sticky="nsew")
    scroll_list.grid(column=0, row=1, sticky="nsew")
    info_frame.grid(column=1, row=1, sticky="nsew")

    root.mainloop()    


if __name__ == "__main__":
    main()
