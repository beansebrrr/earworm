from api import MusicBrainzAPI
import tkinter as tk
from ui import InfoFrame, ScrollList, SearchBar

def main():
    api = MusicBrainzAPI()
    root = tk.Tk()
    root.geometry("1280x720")

    scroll_list = ScrollList(root)
    search_bar = SearchBar(root, api, scroll_list)
    info_frame = InfoFrame(root, api)

    scroll_list.connect_to_info_frame(info_frame)

    search_bar.pack(side="top", fill="x")
    scroll_list.pack(fill="y", side="left")
    info_frame.pack(expand=True, fill="both", side="left")

    root.mainloop()    


if __name__ == "__main__":
    main()
