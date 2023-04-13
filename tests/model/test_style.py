from src.domain.doc import Doc
from src.domain.paragraph import Paragraph
from src.domain.container import Container
from src.domain.style import Style
def test_1_style():
    path_input = '../../data/docu23.docx'
    path_style = '../../data/docu24.docx'

    doc_input = Doc(path_input)
    doc_style= Doc(path_style)

    doc_input.apply_styles_from(doc_style)

    doc_input.styles.xstyle.font.size == doc_style.styles.xstyle.font.size
