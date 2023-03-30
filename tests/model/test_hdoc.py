from src.model.hdoc import Hdoc
from src.model.content import Content


def test_1_hdoc_create():

    path = '../../data/docu1.docx'

    hdoc = Hdoc(path)

    assert(len(hdoc.container.children) == 1)


