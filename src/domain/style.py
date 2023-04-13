from docx.enum.style import WD_STYLE_TYPE
class Style:

    def __init__(self, xstyle, doc_id, id_):

        self.id_ = int(str(doc_id)+str(id_))
        self.xstyle = xstyle
        #self.new_style = self.copy_from

    def copy_from(self, xref):  # need to be further developed

        if xref.type == WD_STYLE_TYPE.PARAGRAPH:
            self.xstyle.font.size = xref.font.size
            self.xstyle.font.color.rgb = xref.font.color.rgb
            self.xstyle.font.name = xref.font.name
            self.xstyle.font.all_caps = xref.font.all_caps
            # Read/write. Causes text in this font to appear in capital letters.
            self.xstyle.font.bold = xref.font.bold
            # Read/write. Causes text in this font to appear in bold.
            self.xstyle.font.complex_script= xref.font.complex_script
            # Read/write tri-state value. When True, causes the characters in
            # the run to be treated as complex script regardless of their Unicode values.
            # "complex script" refers to text written using a complex writing system such as Arabic, Hebrew, Tamil,
            # Persian, and others.These scripts require special typesetting and handling because they have different
            # writing directions, glyph connections, and letter shape variations. Word provides features that support
            # these complex scripts, allowing users to easily create, edit, and format this type of text.
            self.xstyle.font.cs_bold = xref.font.cs_bold
            # Read/write tri-state value. When True, causes the complex script characters
            # in the run to be displayed in bold typeface.
            self.xstyle.font.cs_italic = xref.font.cs_italic
            # Read/write tri-state value. When True, causes the complex script characters
            # in the run to be displayed in italic typeface
            self.xstyle.font.double_strike = xref.font.double_strike
            # Read/write tri-state value. When True, causes the text in the run to appear with double strikethrough.
            self.xstyle.font.emboss = xref.font.emboss
            # Read/write tri-state value. When True, causes the text in the run to appear
            # as if raised off the page in relief.
            self.xstyle.font.hidden = xref.font.hidden
            # Read/write tri-state value. When True, causes the text in the run to be hidden from display,
            # unless applications settings force hidden text to be shown.
            self.xstyle.font.highlight_color = xref.font.highlight_color
            # A member of WD_COLOR_INDEX indicating the color of highlighting applied,
            # or None if no highlighting is applied.
            self.xstyle.font.imprint = xref.font.imprint
            # Read/write tri-state value. When True,
            # causes the text in the run to appear as if pressed into the page.
            self.xstyle.font.italic = xref.font.italic
            self.xstyle.font.math = xref.font.math
            self.xstyle.font.no_proof = xref.font.no_proof
            # Read/write tri-state value. When True, specifies that the contents of this run
            # should not report any errors when the document is scanned for spelling and grammar.
            self.xstyle.font.outline = xref.font.outline
            # Read/write tri-state value. When True causes the characters in the run to appear as if they
            # have an outline, by drawing a one pixel wide border around the inside and
            # outside borders of each character glyph.
            self.xstyle.font.rtl = xref.font.rtl
            # Read/write tri-state value. When True causes the text in the
            # run to have right-to-left characteristics.
            self.xstyle.font.shadow = xref.font.shadow
            self.xstyle.font.small_caps = xref.font.small_caps
            self.xstyle.font.snap_to_grid = xref.font.snap_to_grid
            # Read/write tri-state value. When True causes the run to use the document grid characters per line
            # settings defined in the docGrid element when laying out the characters in this run.
            # Snap to grid" is a layout feature that helps users align text boxes, images, or other objects precisely
            # to a virtual gridline, ensuring consistent spacing and alignment of objects in a document. It improves the
            # visual appearance of a document and makes it easier to read and understand. This feature is particularly
            # useful for creating large documents such as reports, posters, and flyers, making them look more
            # professional, organized, and readable."""
            self.xstyle.font.spec_vanish = xref.font.spec_vanish
            # Read/write tri-state value. When True, specifies that the given run shall always behave as if it is
            # hidden, even when hidden text is being displayed in the current document. The property has a very narrow,
            # specialized use related to the table of contents.
            self.xstyle.font.strike = xref.font.strike
            # Read/write tri-state value. When True causes the text in the run to appear with a single horizontal line
            # through the center of the line.
            self.xstyle.font.subscript = xref.font.subscript
            # Boolean indicating whether the characters in this Font appear as subscript. None indicates the
            # subscript/subscript value is inherited from the style hierarchy.
            self.xstyle.font.superscript = xref.font.superscript
            self.xstyle.font.underline = xref.font.underline
            self.xstyle.font.web_hidden = xref.font.web_hidden
            # Using the "Web hidden" property allows us to create multiple versions of a document where some content
            # can be hidden, while other content can be displayed publicly. For example, in a resume, you can use the
            # "Web hidden" property to hide private information such as phone numbers and addresses. This information
            # will only be displayed when an employer chooses to view it.

            self.xstyle.base_style = xref.base_style
            # Style object this style inherits from or None if this style is not based on another style.
            # self.xstyle.builtin = xref.builtin
            self.xstyle.hidden = xref.hidden
            # True if display of this style in the style gallery and list of recommended styles is suppressed.
            # False otherwise. In order to be shown in the style gallery, this value must be False and quick_style
            # must be True.
            self.xstyle.locked = xref.locked
            # True if this style is locked. not appear in the styles panel or the style gallery and cannot be applied
            # to document content
            self.xstyle.name = xref.name
            self.xstyle.priority = xref.priority
            # The integer sort key governing display sequence of this style in the Word UI. None indicates no setting
            # is defined, causing Word to use the default value of 0. Style name is used as a secondary sort key to
            # resolve ordering of styles having the same priority value.
            #
            # In Microsoft Word, "priority" is typically used to describe the importance of markers and comments to
            # help authors and editors determine the urgency and priority of the feedback and changes being provided.
            # For example, a document may use priority markers such as "high," "medium," "low," etc.
            # to indicate issues that need to be addressed with a higher priority.


            self.xstyle.quick_style = xref.quick_style
            # True if this style should be displayed in the style gallery when hidden is False. Read/write Boolean.
            # for example, Quick Styles can be found in the "Styles" group on the "Home" tab.
            # self.xstyle.type = xref.type
            self.xstyle.unhide_when_used = xref.unhide_when_used
            # True if an application should make this style visible the next time it is applied to content.
            # False otherwise. Note that python-docx does not automatically unhide a style having True for this
            # attribute when it is applied to content.

            # "unhide_when_used" can refer to a feature in Microsoft Excel. It is a cell format option that allows the
            # cell to automatically show when it is being used and hide when it is not being used. This is useful when
            # dealing with complex worksheets as it helps users manage and organize data better. When the user needs to
            # edit or input data, the cell will automatically show, and once the user has completed the operation, the
            # cell will automatically hide to better present the data.

