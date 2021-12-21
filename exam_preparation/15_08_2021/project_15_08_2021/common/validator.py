class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, error_message):
        if string.strip() == "":
            raise ValueError(error_message)

    @staticmethod
    def raise_if_value_equal_or_less_than_zero(value, error_message):
        if value <= 0:
            raise ValueError(error_message)

    @staticmethod
    def raise_if_table_number_not_valid(value, min_number, max_number, error_message):
        if value not in range(min_number, max_number + 1):
            raise ValueError(error_message)

    @staticmethod
    def validate_if_exist_by_name(list_of_objects, name, error_message):
        for object in list_of_objects:
            if object.name == name:
                raise Exception(error_message)

    @staticmethod
    def validate_table_number(tables_repository, table_number, error_message):
        for table in tables_repository:
            if table.table_number == table_number:
                raise Exception(error_message)

    @staticmethod
    def search_for_table_by_table_number(tables_repository, table_number):
        for table in tables_repository:
            if table.table_number == table_number:
                return table

        return None

    @staticmethod
    def search_for_object_by_name(objects_list, object_name):
        for object in objects_list:
            if object.name == object_name:
                return object


