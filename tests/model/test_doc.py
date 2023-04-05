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


def test_9_hdoc_create():
    path = '../../data/docu9.docx'  # with image title 2

    doc = Doc(path)
    assert len(doc.container.children) == 1
    assert doc.container.children[0].title


def test_10_hdoc_create():
    path = '../../data/docu10.docx'  # with footer and header

    doc = Doc(path)
    assert len(doc.container.children) == 1
    assert doc.container.children[0].title


def test_cccp_hdoc_create():
    path = '../../data/cctp.docx'
    doc = Doc(path)


def test_1_set_style_from():
    path19 = '../../data/docu19.docx'
    path20 = '../../data/docu20.docx'
    path22 = '../../data/docu22.docx'

    doc19 = Doc(path19)
    doc20 = Doc(path20)

    doc19.copy_styles_from(doc20)

    doc19.save_as_docx(path22)
    doc22 = Doc(path22)

    def get_style(doc: Doc, name):
        return doc.xdoc.styles[name]

    style19, style20, style22 = \
        get_style(doc19, 'Heading 1'), get_style(doc20, 'Heading 1'), get_style(doc22, 'Heading 1')

    assert style20.font.color.rgb == style22.font.color.rgb
    assert style19.font.size == style22.font.size
    assert style19.font.name == style22.font.name


def test_2_set_style_from():  # custom style
    path_input = '../../data/docu23.docx'
    path_style = '../../data/docu24.docx'
    path_output = '../../data/docu25.docx'

    doc_input = Doc(path_input)
    doc_style = Doc(path_style)

    doc_input.copy_styles_from(doc_style)

    doc_input.save_as_docx(path_output)
    doc_output = Doc(path_output)

    def get_style(doc: Doc, name):
        return doc.xdoc.styles[name]

    style_output, style_style = get_style(doc_output, 'Custom1'), get_style(doc_style, 'Custom1')

    assert style_output.font.color.rgb == style_style.font.color.rgb
    assert style_output.font.size == style_style.font.size
    assert style_output.font.name == style_style.font.name






