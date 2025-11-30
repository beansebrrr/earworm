from .list_item import ListItem
from ._scrollable_frame import ScrollableFrame

class ScrollList(ScrollableFrame):
    def connect_to_info_frame(self, frame):
        self.__info_frame = frame

    def populate(self, elements=[]):
        self.clear()
        for element in elements:
            ListItem(self.interior, element, info_frame=self.__info_frame).pack(anchor="nw", fill="x")
            
