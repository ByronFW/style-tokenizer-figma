from token_interface import *

DEFAULT_FONT = "ROBOTO"


class Tokens(TokenCollection):
    black = CoreStyles.black
    white = Color("#FFFFFF")

    shadow_1 = DropShadow(add_alpha(black, 30), 0, 1, 2, 0)
    shadow_2 = DropShadow(add_alpha(black, 15), 0, 1, 3, 1)

    class Display:
        large = Typography(DEFAULT_FONT, "Regular", 57, 64, -0.25)
        medium = Typography(DEFAULT_FONT, "Regular", 45, 52)
        small = Typography(DEFAULT_FONT, "Regular", 36, 44)

    class Headline:
        large = Typography(DEFAULT_FONT, "Regular", 32, 40)
        medium = Typography(DEFAULT_FONT, "Regular", 28, 36)
        small = Typography(DEFAULT_FONT, "Regular", 24, 32)

    elevation_1 = CoreStyles.elevation_1
    elevation_2 = CoreStyles.elevation_2
    elevation_3 = CoreStyles.elevation_3
    elevation_4 = CoreStyles.elevation_4
    elevation_5 = CoreStyles.elevation_5

Tokens.export('style_tokens.json')