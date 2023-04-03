from src.model.paragraph import Paragraph
from src.config import INFINITE


class Container:

    def __init__(self, paragraphs: [Paragraph], title: Paragraph = None, level: int = 0):
        self.level = level
        self.title = title
        self.paragraphs = None
        self.children = None
        if paragraphs:
            self.paragraphs, self.children = self.create_children(paragraphs, level)
        self.text = self.get_text()
        self.table_of_contents = self.get_table_of_contents()

    def get_text(self):
        text = ""
        if self.title:
            text = "Titre " + str(self.level) + " : " + self.title.text + '\n'
        if self.paragraphs:
            for p in self.paragraphs:
                text += p.text + '\n'
        if self.children:
            for child in self.children:
                text += child.text
        return text


    def get_table_of_contents(self):
        toc = []
        if self.title:
            toc += [{str(self.level): self.title.text}]
        if self.children:
            for child in self.children:
                toc += child.table_of_contents
        return toc


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
