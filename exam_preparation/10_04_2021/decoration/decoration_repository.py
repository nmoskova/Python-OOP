from project.common.validator import Validator


class DecorationRepository:
    def __init__(self):
        self.decorations = []  # will contain all decorations (objects)

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        found_object = Validator.search_for_object_and_returns_it_if_found(self.decorations, decoration)
        if not found_object:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type):
        decoration = Validator.search_object_by_type(self.decorations, decoration_type)
        if not decoration:
            return "None"
        return decoration
