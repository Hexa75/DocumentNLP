import docx


from src.model.container import Container
from src.model.paragraph import Paragraph


class Doc:

    def __init__(self, path):

        self.xdoc = docx.Document(path)
        paragraphs = [Paragraph(xp) for xp in self.xdoc.paragraphs]
        self.container = Container(paragraphs)  # need to extract the data necessary in order to create the objects below

        pass

    def save_as_docx(self):
        pass

    def to_docx(self):
        pass






