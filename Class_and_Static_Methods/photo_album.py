_PAGE_PHOTOS: int = 4
_SUCCESS: str = "photo added successfully on page"
_FAILED: str = "No more free slots"
_DISHES: str = f'{11 * "-"}\n'


class PhotoAlbum:
    PAGE_PHOTOS = _PAGE_PHOTOS
    SUCCESS = _SUCCESS
    FAILED = _FAILED
    DASHES = _DISHES

    def __init__(self, pages: int):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]
        self.pindex: int = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        photos: int = int(photos_count) // cls.PAGE_PHOTOS
        return cls(photos)

    def is_space(self) -> bool:
        return self.pindex < self.pages and \
               len(self.photos[self.pindex]) < self.PAGE_PHOTOS

    def page_new(self) -> int:
        if len(self.photos[self.pindex]) == self.PAGE_PHOTOS:
            self.pindex += 1
        return self.pindex

    def add_photo(self, label: str):
        if not self.is_space():
            return self.FAILED
        self.photos[self.pindex].append(str(label))
        p_added = f"{label} photo added successfully on page {self.pindex + 1} slot {len(self.photos[self.pindex])}"
        self.page_new()
        return p_added

    def display(self):
        displ = self.DASHES
        for _ in self.photos:
            if _:
                displ += ''.join("[] " for p in range(len(_))).strip()
                print(displ)
            displ += f"\n{self.DASHES}"
        return displ


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
