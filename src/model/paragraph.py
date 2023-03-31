from src.config import INFINITE


class Paragraph:

    def __init__(self, xparagraph):

        self.xparagraph = xparagraph
        self.level = INFINITE
        self.is_structure = self.level < INFINITE
