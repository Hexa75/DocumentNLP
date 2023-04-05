
class Styles:

    def __init__(self, xstyles):

        self.xstyles = xstyles
        self.styles = {xstyles.s.name: s for s in xstyles}

    def compare_styles(self, ref_styles):

        common_styles = [s for s in self.styles if s.name in ref_styles.keys()]
        outliers_styles = [s for s in self.styles if s.name not in ref_styles.keys()]

        return common_styles, outliers_styles

    def copy_styles_from(self, ref_styles):

        common_styles, _ = self.compare_styles(ref_styles)
        for s in common_styles:
            s.copy_from()






        def copy_style(style_source): # need to be further developed
            """
            font_tg = style_target.font
            font_src = style_source.font
            font_tg.size = font_src.size
            font_tg.color.rgb = font_src.color.rgb
            font_tg.name = font_src.name
            """
            pass
