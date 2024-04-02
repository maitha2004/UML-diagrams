class Exhibition:
    def __init__(self, duration, location, artworks):
        self.duration = duration
        self.location = location
        self.artworks = artworks

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)
