from .helper import locate_file, milliseconds_to_time
from PIL import Image, ImageTk
from ._scrollable_frame import ScrollableFrame
import tkinter as tk


class InfoFrame(ScrollableFrame):
    def __init__(self, parent, api):
        super().__init__(parent)
        self.__api = api
        self.interior.columnconfigure(0, minsize=256)
        self.interior.columnconfigure(1, weight=1)
        self.interior.configure(padx=8, pady=8)


    def fill_info(self, id):
        self.image = None
        self.tk_image = None
        self.clear()

        release_info = self.__api.lookup_release(id)
        release_summary = tk.Frame(self.interior, padx=12)

        duration = sum([track["length"] 
                        if track["length"] != None else 0
                        for track in release_info["tracks"]])
        duration = milliseconds_to_time(duration)

        # Cover image retrieval
        image_data = self.__api.get_cover_art_data(id)
        image_widget = AlbumCoverImage(self.interior, image_data)
        
        # Top-level information
        title_label = tk.Label(release_summary,
                               justify="left", anchor="nw",
                               text=release_info["title"],
                               font=("tkDefaultFont", 18, "bold"),
                               wraplength=500)
        artists_label = tk.Label(release_summary,
                                 justify="left", anchor="nw",
                                 text=", ".join(release_info["artists"]),
                                 font=("tkDefaultFont", 14),
                                 wraplength=500)
        track_count_label = tk.Label(release_summary,
                                     justify="left", anchor="nw",
                                     text=f"{len(release_info["tracks"])} tracks")
        duration_label = tk.Label(release_summary,
                                  justify="left", anchor="nw",
                                  text=duration)
        track_list = TrackList(self.interior, release_info["tracks"])

        # Placement of a release's basic info
        title_label.pack(fill="x")
        artists_label.pack(fill="x")
        tk.Frame(release_summary, height=16).pack()
        track_count_label.pack(fill="x")
        duration_label.pack(fill="x")

        # Placement of main components
        image_widget.grid(column=0, row=0, sticky="nsew")
        release_summary.grid(column=1, row=0, sticky="nsew")
        tk.Frame(self.interior, height=24).grid(column=0, row=1, sticky="nsew")
        track_list.grid(column=0, row=2, columnspan=2, sticky="nsew")


class AlbumCoverImage(tk.Label):
    """Cover image displayed when you view a release"""

    def __init__(self, parent, image_data):
        super().__init__(parent)
        self.config(background="slateblue", height=256, width=256)

        # Fallback cover image
        if image_data is None:
            image_data = locate_file("images/image_not_found.png")

        # Parse image data into a Tk image
        self.image = Image.open(image_data)
        self.image.thumbnail((256, 256))
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.config(image=self.tk_image)


class TrackList(tk.Frame):
    """Generates a table of tracks, displaying their title and duration"""
    def __init__(self, parent, tracks):
        # Alternating two row colors
        ROW_COLORS = ["lightcyan1","slategray2"]
        __alt = True

        # Boilerplate and config
        super().__init__(parent)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=300)
        self.config(pady=2, padx=2, background="midnightblue")
        
        # Table headers
        tk.Label(self, text="#",
                 font=("tkDefaultFont", 12, "bold"),
                 pady=8,
                 background="slateblue2",
                 foreground="ghostwhite"
                 ).grid(column=0, row=0, sticky="nsew")
        tk.Label(self, text="Title",
                 font=("tkDefaultFont", 12, "bold"),
                 anchor="nw", justify="left",
                 pady=8,
                 background="slateblue2",
                 foreground="ghostwhite"
                 ).grid(column=1, row=0, sticky="nsew")
        tk.Label(self, text="Duration",
                 font=("tkDefaultFont", 12, "bold"),
                 anchor="nw", justify="left",
                 pady=8,
                 background="slateblue2",
                 foreground="ghostwhite"
                 ).grid(column=2, row=0, sticky="nsew")
        
        tk.Frame(self, height=2, background="indigo").grid(sticky="nsew")

        # Generate each individual row
        for i, track in enumerate(tracks):
            __selected_color = ROW_COLORS[0 if __alt else 1]
            tk.Label(self, text=str(i+1),
                     anchor="nw", justify="left",
                     font=("tkDefaultFont", 11),
                     background=__selected_color,
                     padx=24
                     ).grid(column=0, row=i+1, sticky="nsew")
            tk.Label(self, text=track["title"],
                     anchor="nw", justify="left",
                     wraplength=600,
                     font=("tkDefaultFont", 11),
                     background=__selected_color,
                     ).grid(column=1, row=i+1, sticky="nsew")
            tk.Label(self, text=milliseconds_to_time(track["length"]),
                     anchor="nw", justify="left",
                     font=("tkDefaultFont", 11),
                     background=__selected_color,
                     ).grid(column=2, row=i+1, sticky="nsew")
            __alt = not __alt

