from src.config import INFINITE


class Paragraph:

    def __init__(self, xparagraph, doc_id: int, id_: int):

        self.xparagraph = xparagraph
        self.id_ = int(str(doc_id)+str(id_))
        name = self.xparagraph.style.name
        self.level = int(name.split(' ')[-1]) if 'Heading' in name else INFINITE
        self.is_structure = self.level < INFINITE
        self.text = self.xparagraph.text
