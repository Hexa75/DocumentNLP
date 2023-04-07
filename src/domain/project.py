from src.domain.doc import Doc


class Project:

    def __init__(self, name: str, docs: [Doc]):

        self.docs = docs
        self.name = name
