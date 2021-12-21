from project.rooms.room import Room
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost

        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result += f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                family_name = room.family_name
                self.rooms.remove(room)
                result += f"{family_name} does not have enough budget and must leave the hotel.\n"

        return result.strip()

    def status(self):
        result = ""
        result += f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for idx, child in enumerate(room.children):
                    result += f"--- Child {idx + 1} monthly cost: {(child.cost*30):.2f}$\n"
            if hasattr(room, "appliances"):
                total = 0
                for a in room.appliances:
                    total += a.get_monthly_expense()
                result += f"--- Appliances monthly cost: {total:.2f}$\n"

        return result.strip()