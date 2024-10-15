from token_interface import *

class CustomStyles(TokenCollection):
    black = CoreStyles.black
    white = CoreStyles.white
    primary = Color("#FF5722")
    secondary = Color("#795548")

    # Elevations
    drop_shadow_1 = DropShadow(add_alpha(black, 30), x = 0, y = 1, blur=3, spread=3) # black 30% opacity
    drop_shadow_2 = DropShadow(add_alpha(black, 15), x = 0, y = 1, blur=5, spread=5) # black 15% opacity
    elevation_1 = BoxShadow(drop_shadow_1, drop_shadow_1)

# Export the defined styles
CustomStyles.export('custom_styles.json')