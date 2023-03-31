from src.model.paragraph import Paragraph
from src.config import INFINITE


class Container:

    def __init__(self, paragraphs: [Paragraph], title: Paragraph = None, level: int = 0):
        self.level = level
        self.title = title
        if paragraphs:
            self.paragraphs, self.children = self.create_children(paragraphs, level)



    def create_children(self, paragraphs, level) -> ([], []):
        """
        creates children containers or directly attached content
        and returns the list of containers and contents of level+1
        :return:
        [Content or Container]
        """
        attached_paragraphs = []
        container_paragraphs = []
        container_title = None
        children = []
        in_children = False
        level = INFINITE

        while paragraphs:
            p = paragraphs.pop(0)
            if not in_children and not p.is_structure:
                attached_paragraphs.append(p)
            else:
                in_children = True
                if p.is_structure and p.level <= level:  # if p is higher or equal in hierarchy
                    if container_paragraphs or container_title:
                        children.append(Container(container_paragraphs, container_title, level))
                    container_paragraphs = []
                    container_title = p
                    level = p.level

                else:  # p is stricly lower in hierarchy
                    container_paragraphs.append(p)

        if container_paragraphs or container_title:
            children.append(Container(container_paragraphs, container_title, level))

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
