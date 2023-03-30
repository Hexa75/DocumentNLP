from src.model.hdoc import Hdoc


def test_1_hdoc_create():

    path = '../../data/docu1.docx'

    hdoc = Hdoc(path)

    assert(hdoc.container.children == None)