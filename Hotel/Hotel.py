class Room:
    def __init__(self, name, is_double, is_occupied = False):
        self.name = name
        self.is_double = is_double
        self.is_occupied = is_occupied

    def book(self):
        if self.is_occupied:
            print(f"{self.name} konte nicht gebucht werden.")
            return False
        self.is_occupied = True
        print(f"{self.name} wurde gebucht.")
        return True

    def cancel(self):
        if self.is_occupied:
            print(f"{self.name} wurde stoniert.")
            self.is_occupied = False
            return True
        print(f"{self.name} konnte nicht stoniert werden.")
        return False
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def book_room(self, name):
        for room in self.rooms:
            if room.name == name:
                return room.book()
        return False

    def book_next_free(self):
        for room in self.rooms:
            if room.is_occupied == False:
                room.book()
                return True
        return False

    def cancel_room(self,name):
        for room in self.rooms:
            if room.name == name:
                return room.cancel()
        return False

if __name__ == "__main__":
    rooms = [Room('Raum Peter', True, True),
             Room('Raum Sebi', False),
             Room('Raum Schwaiger', True, True)]
    hotel = Hotel('Hotel Super Cool', rooms)

    hotel.cancel_room('Raum Peter')
    hotel.book_room('Raum Peter')
    hotel.cancel_room('Raum Schwaiger')
    hotel.book_next_free()





