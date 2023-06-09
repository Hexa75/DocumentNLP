from src.domain.doc import Doc
from src.domain.paragraph import Paragraph
from src.domain.container import Container


def test_1_container_get_text():
    path = '../../data/docu1.docx'  # Bonjour, je m’appelle Peng

    doc = Doc(path)

    assert doc.container.text == "Bonjour, je m’appelle Peng\n"


def test_2_container_get_text():
    path = '../../data/docu2.docx'  # Bonjour, je m’appelle Peng

    doc = Doc(path)

    assert doc.container.text == "Titre 1 : Bonjour, je m’appelle Peng\n"


def test_3_container_get_text():
    path = '../../data/docu13.docx'  # multiple containers

    doc = Doc(path)

    assert doc.container.children[0].text == "Titre 1 : Bonjour, je m’appelle Peng\nTitre 2 : Et j’aime le chocolat\n"


def test_4_container_get_text():
    path = '../../data/docu14.docx'  # multiple containers

    doc = Doc(path)

    assert doc.container.children[0].text == "Titre 1 : Bonjour, je m’appelle Peng\nTitre 2 : Et j’aime le chocolat\nTitre 3 : Et la mousse\nPas les fraises\n"
    assert doc.container.children[1].text == "Titre 1 : Et moi je m’appelle Jean-Charles\n"


def test_1_table_of_contents():
    path = '../../data/docu1.docx'  # Bonjour, je m’appelle Peng
    doc = Doc(path)
    assert doc.container.table_of_contents == []


def test_2_table_of_contents():
    path = '../../data/docu2.docx'  # Bonjour, je m’appelle Peng (title 1)

    doc = Doc(path)

    assert doc.container.table_of_contents == [{"1": "Bonjour, je m’appelle Peng"}]


def test_3_get_table_of_contents():
    path = '../../data/docu15.docx'  # Bonjour, je m’appelle Peng (title 1) + title3 + ... + title 1

    doc = Doc(path)

    assert doc.container.table_of_contents == [{"1": "Bonjour, je m’appelle Peng"}, {"3": "Et j’aime le chocolat"},
                                                 {"1": "Et moi je m’appelle Jean-Charles"}]


def test_1_move_container():
    path = '../../data/docu15.docx'  # Bonjour, je m’appelle Peng (title 1) + title3 + ... + title 1

    doc = Doc(path)


def test_1_rank():
    path = '../../data/docu15.docx'  # Bonjour, je m’appelle Peng (title 1) + title3 + ... + title 1

    doc = Doc(path)
    assert doc.container.rank == 0
    assert doc.container.children[0].rank == 1
    assert doc.container.children[0].children[0].rank == 2
    assert doc.container.children[0].children[0].level == 3

