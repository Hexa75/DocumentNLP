import docx
from docx.enum.style import WD_STYLE_TYPE

from src.model.container import Container
from src.model.paragraph import Paragraph
from src.model.style import Style


class Doc:

    def __init__(self, path):

        self.xdoc = docx.Document(path)
        self.path = path
        paragraphs = [Paragraph(xp) for xp in self.xdoc.paragraphs]
        self.container = Container(paragraphs)
        self.styles = dict(s.name, s for s in self.xdoc.styles])

    def compare_styles(self, doc):
        self_styles_names = [s.name for s in self.styles]
        doc_styles_names = [s.name for s in doc.styles]

        common_style_names = list(set(self_styles_names) & set(doc_styles_names))

        common_styles = [s for s in self.styles if s.name in common_style_names]
        outliers_styles = [s for s in self.styles if s.name not in common_style_names]

        return common_styles, outliers_styles

    def copy_styles_from(self, doc):

        common_styles = self.compare_styles(doc)
        for s in common_styles:
            s.copy_from()

        self_styles_names = [s.name for s in self.xdoc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]
        doc_styles_names = [s.name for s in doc.xdoc.styles if s.type == WD_STYLE_TYPE.PARAGRAPH]

        common_style_names = set(self_styles_names) & set(doc_styles_names)



        for name in common_style_names:
            copy_style(self.xdoc.styles[name], doc.xdoc.styles[name])


    def save_as_docx(self, path):
        self.xdoc.save(path)

    def to_docx(self):
        pass






