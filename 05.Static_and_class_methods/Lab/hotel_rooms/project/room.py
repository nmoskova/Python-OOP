class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        """
        if the room is not taken, and there is enough space,
        the guests take the room. Otherwise, the method should return "Room number {number} cannot be taken"
        """
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.capacity -= people
        self.guests += people

    def free_room(self):
        """
        if the room is taken, free it.
        Otherwise, return "Room number {number} is not taken"
        """
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.capacity += self.guests
        self.guests = 0

