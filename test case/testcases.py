class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

class Exhibition:
    def __init__(self, duration, location, artworks):
        self.duration = duration
        self.location = location
        self.artworks = artworks

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, artwork):
        self.artworks.remove(artwork)

class SpecialEvent:
    def __init__(self, event_type, duration, location, ticket_price):
        self.event_type = event_type
        self.duration = duration
        self.location = location
        self.ticket_price = ticket_price

class Ticket:
    def __init__(self, ticket_type, ticket_price, exhibition):
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price
        self.exhibition = exhibition

class Visitor:
    def __init__(self, ticket_id, name, age, national_id, ticket_type):
        self.ticket_id = ticket_id
        self.name = name
        self.age = age
        self.national_id = national_id
        self.ticket_type = ticket_type

# Test Case: Addition of new art to the museum
def test_add_artwork():
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "One of the most famous paintings in the world", "Permanent Gallery")
    print("Artwork added successfully:", artwork.title)

# Test Case: Opening of a new exhibition or event at the museum
def test_open_exhibition():
    artworks = [Artwork("The Starry Night", "Vincent van Gogh", "1889", "Iconic painting depicting night sky", "Exhibition Hall")]
    exhibition = Exhibition("2024-05-01", "Exhibition Hall", artworks)
    print("New exhibition opened:", exhibition.location)

# Test Case: Purchase of tickets by an individual or tour group for an event
def test_purchase_tickets():
    exhibition = Exhibition("2024-05-01", "Exhibition Hall", [])
    ticket = Ticket("Adult", 63.0, exhibition)
    print("Ticket purchased for:", ticket.exhibition.location)

# Test Case: Display of payment receipts for purchasing tickets
# Test Case: Display of payment receipts for purchasing tickets
def test_display_receipt():
    visitor = Visitor("12345", "Maitha Mohammed", 30, "1234567890", "Adult")
    exhibition = Exhibition("2024-05-01", "Exhibition Hall", [])
    ticket = Ticket("Adult", 63.0, exhibition)
    print("Payment Receipt:")
    print("Ticket ID:", visitor.ticket_id)
    print("Visitor Name:", visitor.name)
    print("Ticket Price:", ticket.ticket_price)


# Run test cases
if __name__ == "__main__":
    print("--- Testing Addition of New Artwork ---")
    test_add_artwork()
    print("\n--- Testing Opening of New Exhibition ---")
    test_open_exhibition()
    print("\n--- Testing Purchase of Tickets ---")
    test_purchase_tickets()
    print("\n--- Testing Display of Payment Receipt ---")
    test_display_receipt()
