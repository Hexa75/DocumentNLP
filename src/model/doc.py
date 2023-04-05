import docx
from docx.enum.style import WD_STYLE_TYPE

from src.model.container import Container
from src.model.paragraph import Paragraph
from src.model.styles import Styles


class Doc:

    def __init__(self, path):

        self.xdoc = docx.Document(path)
        self.path = path
        paragraphs = [Paragraph(xp) for xp in self.xdoc.paragraphs]
        self.container = Container(paragraphs)
        self.styles = {s.name: Styles(s) for s in self.xdoc.styles}


    def save_as_docx(self, path):
        self.xdoc.save(path)









