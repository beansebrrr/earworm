import tkinter as tk

class SearchBar(tk.Frame):
    def __init__(self, parent, api, scroll_list):
        super().__init__(parent)
        self.config(padx=4, pady=12)

        self.__api = api
        self.__list_element = scroll_list

        self.search_field = tk.Entry(self)
        self.search_button = tk.Button(self, text="Search", command=self.search)

        self.search_field.pack(expand=True, fill="x", side="left")
        self.search_button.pack(side="left")
        self.search_field.bind('<Return>', self._search)

    def search(self):
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