class Search:
    @staticmethod
    def search_for_object_by_name(objects_repo, name):
        for object in objects_repo:
            if object.name == name:
                return object

        return None