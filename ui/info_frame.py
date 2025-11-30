import tkinter as tk
from PIL import Image, ImageTk

class InfoFrame(tk.Frame):
    def __init__(self, parent, api):
        super().__init__(parent)

        self.__api = api

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def fill_info(self, id):
        self.image = None
        self.tk_image = None
        self.clear()

        image_widget = tk.Label(self, text="No album art found", background="gray", height=360, width=360)

        image_data = self.__api.get_cover_art_data(id)
        if image_data is not None:
            self.image = Image.open(image_data)
            self.image.thumbnail((360, 360))
            self.tk_image = ImageTk.PhotoImage(self.image)
            image_widget.configure(image=self.tk_image)

        image_widget.pack()