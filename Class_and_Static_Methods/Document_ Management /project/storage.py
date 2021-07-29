from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for el in self.categories:
            if el.name == category.name:
                return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for el in self.topics:
            if el.id == topic.id:
                return
        self.topics.append(topic)

    def add_document(self, document: Document):
        for el in self.documents:
            if el.id == document.id:
                return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for el in self.categories:
            if el.id == category_id:
                el.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        obj_topic: Topic = [x for x in self.topics if x.id == topic_id][0]

        for el in self.topics:
            if el.id == topic_id:
                obj_topic.topic = new_topic
                obj_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        obj_doc: Document = [x for x in self.documents if x.id == document_id][0]

        for el in self.documents:
            if el.id == document_id:
                obj_doc.file_name = new_file_name

    def delete_category(self, category_id):
        for el in self.categories:
            if el.id == category_id:
                self.categories.remove(el)

    def delete_topic(self, topic_id):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)

    def delete_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return el

    def __repr__(self):
        result = '\n'.join(str(x) for x in self.documents)
        return result
