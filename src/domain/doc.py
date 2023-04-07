import docx
from docx.enum.style import WD_STYLE_TYPE

from src.domain.container import Container
from src.domain.paragraph import Paragraph
from src.domain.style import Style


class Doc:

    def __init__(self, path='', id_=None):

        self.xdoc = docx.Document(path)
        self.id_ = id(self)
        self.path = path
        paragraphs = [Paragraph(xp, self.id_, i) for (i, xp) in enumerate(self.xdoc.paragraphs)]
        self.container = Container(paragraphs, father=self)
        self.styles = [Style(xs, self.id_, i) for (i, xs) in enumerate(self.xdoc.styles)]

    def save_as_docx(self, path):
        self.xdoc.save(path)

    def apply_styles_from(self, ref_doc):

        ref_doc_styles_names = [s.xstyle.name for s in ref_doc.styles]
        common_styles = [s for s in self.styles if s.xstyle.name in ref_doc_styles_names]

        for s in common_styles:
            s.copy_from(ref_doc.xdoc.styles[s.xstyle.name])








