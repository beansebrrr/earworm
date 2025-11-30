import tkinter as tk
import json
from PIL import Image, ImageTk
from ._scrollable_frame import ScrollableFrame


class InfoFrame(ScrollableFrame):
    def __init__(self, parent, api):
        super().__init__(parent)
        self.__api = api
        self.interior.columnconfigure(0, weight=1, minsize=256)
        self.interior.columnconfigure(1, weight=7)


    def fill_info(self, id):
        self.image = None
        self.tk_image = None
        self.clear()

        release_info = self.__api.lookup_release(id)
        release_summary = tk.Frame(self.interior, background="blue")

        print(json.dumps(release_info, indent=2))

        image_data = self.__api.get_cover_art_data(id)
        image_widget = AlbumCoverImage(self.interior, image_data)
        
        title_label = tk.Label(release_summary, text=release_info["title"], justify="left", anchor="nw")
        artists_label = tk.Label(release_summary, text=", ".join(release_info["artists"]), justify="left", anchor="nw")
        
        title_label.pack(fill="x")
        artists_label.pack(fill="x")

        image_widget.grid(column=0, row=0)
        release_summary.grid(column=1, row=0)
    

class AlbumCoverImage(tk.Label):
    def __init__(self, parent, image_data):
        super().__init__(parent)
        self.config(text="No album art found", background="gray", height=256, width=256)
        
        if image_data is not None:
            self.image = Image.open(image_data)
            self.image.thumbnail((256, 256))
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.config(image=self.tk_image)
        