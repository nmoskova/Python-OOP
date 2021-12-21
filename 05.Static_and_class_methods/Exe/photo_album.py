from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.create_album()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE)
        return cls(pages)

    def create_album(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    def add_photo(self, label):
        for row_i in range(len(self.photos)):
            if row_i == PhotoAlbum.MAX_PHOTOS_PER_PAGE - 1:
                continue
            if len(self.photos[row_i]) == PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                continue
            self.photos[row_i].append(label)
            return f"{label} photo added successfully on page {row_i + 1} slot {len(self.photos[row_i])}"

        return "No more free slots"

    def display(self):
        result = ("-" * 11) + "\n"
        for row in self.photos:
            result += ' '.join(["[]" for _ in row])
            result += "\n" + "-" * 11 + "\n"
        return result


album = PhotoAlbum(4)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.photos)
print(album.display())
