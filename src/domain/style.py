from docx.enum.style import WD_STYLE_TYPE
class Style:

    def __init__(self, xstyle, doc_id, id_):

        self.id_ = int(str(doc_id)+str(id_))
        self.xstyle = xstyle

    def copy_from(self, xref):  # need to be further developed

        if xref.type == WD_STYLE_TYPE.PARAGRAPH:
            self.xstyle.font.size = xref.font.size
            self.xstyle.font.color.rgb = xref.font.color.rgb
            self.xstyle.font.name = xref.font.name
            
        pass
