import docx


from src.model.container import Container


class Hdoc:

    def __init__(self, path):

        self.xdoc = docx.Document(path)
        self.container = Container(self.xdoc.paragraphs)  # need to extract the data necessary in order to create the objects below

        pass

    def save_as_docx(self):
        pass

    def to_docx(self):
        pass






