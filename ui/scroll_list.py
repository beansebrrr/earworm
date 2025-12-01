from .list_item import ListItem
from ._scrollable_frame import ScrollableFrame

class ScrollList(ScrollableFrame):
    """Just a scrollable frame with some functionalities to fill with list items"""
    def __init__(self, parent, info_frame):
        super().__init__(parent)
        self.__info_frame = info_frame

    def populate(self, elements=[]):
        self.clear()
        # Cycles through a `list` of albums to then create list_item widgets out of
        for element in elements:
            ListItem(self.interior, element, 
                     info_frame=self.__info_frame
                     ).pack(anchor="nw", fill="x")
            
