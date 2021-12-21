class Validator:
    @staticmethod
    def search_for_object_and_returns_it_if_found(list_of_objects, object):
        for obj in list_of_objects:
            if obj == object:
                return obj
        return None

    @staticmethod
    def search_object_by_type(list_of_objects, type):
        for object in list_of_objects:
            if object.__class__.__name__ == type:
                return object

        return None

    @staticmethod
    def search_object_by_name(objects_list, name):
        for object in objects_list:
            if object.name == name:
                return object

        return None

    @staticmethod
    def raise_value_error_if_empty_string(value, error_message):
        if value == "":
            raise ValueError(error_message)

    @staticmethod
    def raise_value_error_if_value_equal_or_below_zero(value, error_message):
        if value <= 0:
            raise ValueError(error_message)

