from src.config import INFINITE


class Paragraph:

    def __init__(self, xparagraph):

        self.xparagraph = xparagraph
        name = self.xparagraph.style.name
        self.level = int(name.split(' ')[-1]) if 'Heading' in name else INFINITE
        self.is_structure = self.level < INFINITE
