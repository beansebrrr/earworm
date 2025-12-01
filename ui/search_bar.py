import tkinter as tk

class SearchBar(tk.Frame):
    """Handles search functions and such"""
    def __init__(self, parent, api, scroll_list):
        super().__init__(parent)
        self.config(padx=16, pady=8)

        self.__api = api
        self.__list_element = scroll_list

        self.search_field = tk.Entry(self)
        self.search_button = tk.Button(self, text="Search", command=self.search)

        self.search_field.pack(expand=True, fill="x", side="left")
        tk.Frame(self, width=12).pack(side="left")
        self.search_button.pack(side="left")

        # Allows you to search by just clicking the `Enter` key
        self.search_field.bind('<Return>', self._search)

    def search(self):
        # Ignore if there's nothing to search
        if not self.search_field.get():
            return   
        search_results = self.__api.search_releases(self.search_field.get())
        self.__list_element.populate(search_results)

    def _search(self, e):
        if not self.search_field.get():
            return
        self.search_button.config(state="disabled")
        search_results = self.__api.search_releases(self.search_field.get())
        self.__list_element.populate(search_results)
        self.search_button.config(state="active")