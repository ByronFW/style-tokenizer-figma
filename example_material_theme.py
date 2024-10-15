"""An example TokenCollection that can be copy and pasted"""

from token_interface import *

MATERIAL = parse_material("material_theme_exports/material-theme-default.json")
LIGHT_THEME = MATERIAL["schemes"]["light"]
DEFAULT_FONT = "Roboto"


class M3Styles(TokenCollection):

    black = Color("#000000")
    white = Color("#FFFFFF")

    primary = Color(LIGHT_THEME["primary"])
    surfaceTint = Color(LIGHT_THEME["surfaceTint"])
    onPrimary = Color(LIGHT_THEME["onPrimary"])
    primaryContainer = Color(LIGHT_THEME["primaryContainer"])
    onPrimaryContainer = Color(LIGHT_THEME["onPrimaryContainer"])
    secondary = Color(LIGHT_THEME["secondary"])
    onSecondary = Color(LIGHT_THEME["onSecondary"])
    secondaryContainer = Color(LIGHT_THEME["secondaryContainer"])
    onSecondaryContainer = Color(LIGHT_THEME["onSecondaryContainer"])
    tertiary = Color(LIGHT_THEME["tertiary"])
    onTertiary = Color(LIGHT_THEME["onTertiary"])
    tertiaryContainer = Color(LIGHT_THEME["tertiaryContainer"])
    onTertiaryContainer = Color(LIGHT_THEME["onTertiaryContainer"])
    error = Color(LIGHT_THEME["error"])
    onError = Color(LIGHT_THEME["onError"])
    errorContainer = Color(LIGHT_THEME["errorContainer"])
    onErrorContainer = Color(LIGHT_THEME["onErrorContainer"])
    background = Color(LIGHT_THEME["background"])
    onBackground = Color(LIGHT_THEME["onBackground"])
    surface = Color(LIGHT_THEME["surface"])
    onSurface = Color(LIGHT_THEME["onSurface"])
    surfaceVariant = Color(LIGHT_THEME["surfaceVariant"])
    onSurfaceVariant = Color(LIGHT_THEME["onSurfaceVariant"])
    outline = Color(LIGHT_THEME["outline"])
    outlineVariant = Color(LIGHT_THEME["outlineVariant"])
    shadow = Color(LIGHT_THEME["shadow"])
    scrim = Color(LIGHT_THEME["scrim"])
    inverseSurface = Color(LIGHT_THEME["inverseSurface"])
    inverseOnSurface = Color(LIGHT_THEME["inverseOnSurface"])
    inversePrimary = Color(LIGHT_THEME["inversePrimary"])
    primaryFixed = Color(LIGHT_THEME["primaryFixed"])
    onPrimaryFixed = Color(LIGHT_THEME["onPrimaryFixed"])
    primaryFixedDim = Color(LIGHT_THEME["primaryFixedDim"])
    onPrimaryFixedVariant = Color(LIGHT_THEME["onPrimaryFixedVariant"])
    secondaryFixed = Color(LIGHT_THEME["secondaryFixed"])
    onSecondaryFixed = Color(LIGHT_THEME["onSecondaryFixed"])
    secondaryFixedDim = Color(LIGHT_THEME["secondaryFixedDim"])
    onSecondaryFixedVariant = Color(LIGHT_THEME["onSecondaryFixedVariant"])
    tertiaryFixed = Color(LIGHT_THEME["tertiaryFixed"])
    onTertiaryFixed = Color(LIGHT_THEME["onTertiaryFixed"])
    tertiaryFixedDim = Color(LIGHT_THEME["tertiaryFixedDim"])
    onTertiaryFixedVariant = Color(LIGHT_THEME["onTertiaryFixedVariant"])
    surfaceDim = Color(LIGHT_THEME["surfaceDim"])
    surfaceBright = Color(LIGHT_THEME["surfaceBright"])
    surfaceContainerLowest = Color(LIGHT_THEME["surfaceContainerLowest"])
    surfaceContainerLow = Color(LIGHT_THEME["surfaceContainerLow"])
    surfaceContainer = Color(LIGHT_THEME["surfaceContainer"])
    surfaceContainerHigh = Color(LIGHT_THEME["surfaceContainerHigh"])
    surfaceContainerHighest = Color(LIGHT_THEME["surfaceContainerHighest"])

    class Display:
        large = Typography(DEFAULT_FONT, "Regular", 57, 64, -0.25)
        medium = Typography(DEFAULT_FONT, "Regular", 45, 52)
        small = Typography(DEFAULT_FONT, "Regular", 36, 44)

    class Headline:
        large = Typography(DEFAULT_FONT, "Regular", 32, 40)
        medium = Typography(DEFAULT_FONT, "Regular", 28, 36)
        small = Typography(DEFAULT_FONT, "Regular", 24, 32)

    class Title:
        large = Typography(DEFAULT_FONT, "Regular", 22, 28)
        medium = Typography(DEFAULT_FONT, "Medium", 16, 24)
        small = Typography(DEFAULT_FONT, "Medium", 14, 20, 0.1)

    class Label:
        large = Typography(DEFAULT_FONT, "Medium", 14, 20, 0.1)
        medium_prominent = Typography(DEFAULT_FONT, "SemiBold", 12, 16, 0.5)
        medium = Typography(DEFAULT_FONT, "Medium", 12, 16, 0.5)
        small = Typography(DEFAULT_FONT, "Medium", 11, 16, 0.5)

    class Body:
        large = Typography(DEFAULT_FONT, "Regular", 16, 24, 0.5)
        medium = Typography(DEFAULT_FONT, "Regular", 14, 20, 0.25)
        small = Typography(DEFAULT_FONT, "Regular", 12, 16)

    # Elevations
    elevation_1 = CoreStyles.elevation_1
    elevation_2 = CoreStyles.elevation_2
    elevation_3 = CoreStyles.elevation_3
    elevation_4 = CoreStyles.elevation_4
    elevation_5 = CoreStyles.elevation_5


if __name__ == "__main__":
    M3Styles.export('style_tokens.json')
