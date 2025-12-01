import tkinter as tk

#

class ScrollableFrame(tk.Frame):
    """
    Scrollable frame
    Source: https://stackoverflow.com/a/16198198
    """
    def __init__(self, parent):
        super().__init__(parent)

        vscrollbar = tk.Scrollbar(self, orient="vertical")
        vscrollbar.pack(fill="y", side="right", expand=False)

        canvas = tk.Canvas(
            self, bd=0, highlightthickness=0,
            yscrollcommand=vscrollbar.set
        )
        canvas.pack(side="left", fill="both", expand=True)
        vscrollbar.config(command=canvas.yview)

        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        self.interior = interior = tk.Frame(canvas)
        self.interior.configure(width=300)
        interior_id = canvas.create_window(
            0, 0, window=interior,
            anchor="nw"
        )
 
        def _configure_interior(event):
            """Track changes to the canvas and frame width and sync them,
            also updating the scrollbar."""
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion=f"0 0 {" ".join([str(s) for s in size])}") # type: ignore
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        
    def clear(self):
        for widget in self.interior.winfo_children():
            widget.destroy()