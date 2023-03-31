from src.model.doc import Doc
from src.model.paragraph import Paragraph
from src.model.container import Container



def test_1_hdoc_create():

    path = '../../data/docu1.docx'  # "je m'appelle Peng"

    doc = Doc(path)

    assert len(doc.container.children) == 0
    assert len(doc.container.paragraphs) == 1
    assert not doc.container.title
    assert doc.container.level == 0



def test_2_hdoc_create():

    path = '../../data/docu2.docx'  # # je m'appelle Peng (titre 1)

    doc = Doc(path)

    assert len(doc.container.children) == 1
    assert len(doc.container.paragraphs) == 0
    assert doc.container.children[0].title
    assert doc.container.children[0].level == 1

def test_3_hdoc_create():

    path = '../../data/docu3.docx'  # # je m'appelle Peng (titre 2)

    doc = Doc(path)

    assert len(doc.container.children) == 1
    assert len(doc.container.paragraphs) == 0
    assert doc.container.children[0].title
    assert doc.container.children[0].level == 2

def test_4_hdoc_create():
    path = '../../data/docu4.docx'  # # je m'appelle Peng (titre 2),  et là ça marche?

    doc = Doc(path)

    assert len(doc.container.children) == 1
    assert len(doc.container.paragraphs) == 0
    assert doc.container.children[0].title
    assert doc.container.children[0].level == 2
    assert doc.container.children[0].paragraphs

def test_cccp_hdoc_create():
    path = '../../data/cctp.docx'
    doc = Doc(path)





