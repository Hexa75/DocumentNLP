from src.model.doc import Doc
from src.model.paragraph import Paragraph
from src.model.container import Container


def test_1_hdoc_create():

    path = '../../data/docu1.docx'

    doc = Doc(path)

    assert(len(doc.container.children) == 0)
    assert(len(doc.container.paragraphs) == 4)


def test_cctp_hdoc_create():

    path = '../../data/cctp.docx'

    doc = Doc(path)

    assert(len(doc.container.children) == 0)











