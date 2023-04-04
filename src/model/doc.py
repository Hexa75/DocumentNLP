import docx
from docx.enum.style import WD_STYLE_TYPE

from src.model.container import Container
from src.model.paragraph import Paragraph


class Doc:

    def __init__(self, path):

        self.xdoc = docx.Document(path)
        self.path = path
        paragraphs = [Paragraph(xp) for xp in self.xdoc.paragraphs]
        if paragraphs:
            self.container = Container(paragraphs)


    def set_style_from(self, doc):

        self_styles = [s for s in self.xdoc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]
        self_styles_names = [s.name for s in self_styles]

        doc_styles = [s for s in doc.xdoc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]
        doc_styles_names = [s.name for s in doc_styles]

        common_style_names = set(self_styles_names) & set(doc_styles_names)

        for name in common_style_names:
            font2 = doc.xdoc.styles[name].font
            font1 = self.xdoc.styles[name].font
            font1.size = font2.size
            font1.color.rgb = font2.color.rgb
            font1.name = font2.name







    def save_as_docx(self, path):
        self.xdoc.save(path)

    def to_docx(self):
        pass






