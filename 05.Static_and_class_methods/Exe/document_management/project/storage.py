from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return

        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return

        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return

        self.documents.append(document)

    @staticmethod
    def __get_object_by_id(objects, object_id):
        for object in objects:
            if object.id == object_id:
                return object

    def edit_category(self, category_id, new_name):
        category = self.__get_object_by_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        curr_topic = self.__get_object_by_id(self.topics, topic_id)
        curr_topic.topic = new_topic
        curr_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.__get_object_by_id(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__get_object_by_id(self.categories, category_id)
        if category not in self.categories:
            return

        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_object_by_id(self.topics, topic_id)
        if topic not in self.topics:
            return

        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        if document not in self.documents:
            return

        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        return document

    def __repr__(self):
        result = "\n".join([str(doc) for doc in self.documents])
        return result


