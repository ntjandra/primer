"""
Primer - Python library for ActiveRPG.
"""


__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise primer.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """

    if (kind is 'cook'):
        return ["shells", "gorgonzola", "parsley"]
    if (kind is 'craft'):
        return ["ore", "brick", "sheep", "wheat", "wood"]
    if (kind is "consume"):
        return ["lesser", "greater", "major"]
    return InvalidKindError

