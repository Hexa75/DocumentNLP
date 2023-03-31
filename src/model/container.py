from src.model.paragraph import Paragraph
from src.config import INFINITE


class Container:

    def __init__(self, paragraphs, level: int = 0):
        assert paragraphs
        self.level = level
        self.title = paragraphs[0]
        self.paragraphs, self.children = self.create_children(paragraphs[1:])

    def create_children(self, paragraphs) -> ([], []):
        """
        creates children containers or directly attached content
        and returns the list of containers and contents of level+1
        :return:
        [Content or Container]
        """
        attached_paragraphs = []
        container_paragraphs = []
        children = []
        in_children = False
        level = 0

        while paragraphs:
            p = paragraphs.pop(0)
            if not p.is_structure and not in_children:
                attached_paragraphs.append(p)
            else:
                in_children = True
                while level < p.level or level == INFINITE:
                    container_paragraphs.append(p)
                children.append(Container(container_paragraphs))
                container_paragraphs = [p]
                level = p.level

        if container_paragraphs:
            children.append(Container(container_paragraphs, level))

        return attached_paragraphs, children

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
