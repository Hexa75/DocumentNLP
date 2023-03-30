from src.model.content import Content


class Container:

    def __init__(self, level: int = 0):
        self.level = level
        self.xcontent = 2
        self.children = self.create_children()

    def create_children(self) -> []:
        """
        creates children containers or directly attached content
        and returns the list of containers and contents of level+1
        :return:
        [Content or Container]
        """
        pass

















    def summarize(self, max_word_length=100):
        pass

    def get_lang(self):
        """
        returns the main language of the document
        :return:
        """

    def get_structure(self, level=2):
        """
        returns the structure of the document
        :return:
        """

    def create_embeddings(self):
        """

        :return:
        """
