from static_and_class_methods_05.lab.hotel_rooms.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)
        self.guests += room.guests

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        number_free_rooms = [r.number for r in self.rooms if not r.is_taken]
        number_taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
                f"Free rooms: {', '.join(map(str, number_free_rooms))}\n" \
                f"Taken rooms: {', '.join(map(str, number_taken_rooms))}"

