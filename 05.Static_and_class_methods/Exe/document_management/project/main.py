from static_and_class_methods_05.exe.document_management.project.category import Category
from static_and_class_methods_05.exe.document_management.project.document import Document
from static_and_class_methods_05.exe.document_management.project.storage import Storage
from static_and_class_methods_05.exe.document_management.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")
d2 = Document(2, 2, 2, "secrets")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
storage.add_document(d2)
print(storage)
storage.delete_document(2)
print(storage)
print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
