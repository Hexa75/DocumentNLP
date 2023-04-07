from src.domain.paragraph import Paragraph
from src.config import INFINITE


class Container:

    def __init__(self, paragraphs: [Paragraph], title: Paragraph = None, level: int = 0, rank: int = 0, father=None, id_=0):
        self.level = level
        self.title = title
        self.paragraphs = []
        self.children = []
        self.rank = rank
        self.father = father  # if not father, then the container is at the top of the hierarchy
        self.id_ = int(str(father.id_)+str(id_))
        if paragraphs:
            self.paragraphs, self.children = self.create_children(paragraphs, level, rank+1)

    @property
    def text(self):
        text = ""
        if self.title:
            text = "Titre " + str(self.level) + " : " + self.title.text + '\n'
        for p in self.paragraphs:
                text += p.text + '\n'
        for child in self.children:
                text += child.text
        return text

    @property
    def table_of_contents(self):
        toc = []
        if self.title:
            toc += [{str(self.level): self.title.text}]
        if self.children:
            for child in self.children:
                toc += child.table_of_contents
        return toc

    def move(self, position: int, new_father = None):
        current_father = self.father  # should be added in the domain
        current_father.children.remove(self)

        self.rank = new_father.rank + 1 if new_father else 0
        self.father = new_father
        if position < len(new_father.children):
            new_father.children.insert(position, self)
        else:
            new_father.children.append(self)

    def create_children(self, paragraphs, level, rank) -> ([], []):
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
        child_id = 0

        while paragraphs:
            p = paragraphs.pop(0)
            if not in_children and not p.is_structure:
                attached_paragraphs.append(p)
            else:
                in_children = True
                if p.is_structure and p.level <= level:  # if p is higher or equal in hierarchy
                    if container_paragraphs or container_title:
                        children.append(Container(container_paragraphs, container_title, level, rank, self, child_id))
                        child_id += 1
                    container_paragraphs = []
                    container_title = p
                    level = p.level

                else:  # p is strictly lower in hierarchy
                    container_paragraphs.append(p)

        if container_paragraphs or container_title:
            children.append(Container(container_paragraphs, container_title, level, rank, self, child_id))
            child_id += 1

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
