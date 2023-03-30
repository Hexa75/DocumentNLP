from src.model.content import Content


class Container:

    def __init__(self, paragraphs, level: int = 0):
        self.level = level
        self.paragraphs = paragraphs
        self.children = self.create_children(paragraphs)

    def create_children(self, paragraphs) -> []:
        """
        creates children containers or directly attached content
        and returns the list of containers and contents of level+1
        :return:
        [Content or Container]
        """
        text = ""
        in_children = False
        for p in paragraphs:
            if (p.style.name == "normal") and not in_children:
                text += p.text if p.text != "" else "\n"
            else:
                in_children = True

        children = [Content(text)]

        return children























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
