"""
Rolls - Dice rolling for ActiveRPG
"""

__version__ = "0.1.0"


class InvalidNumberError(Exception):
    """Raised if the dice modifier exceeds the range."""
    pass


def roll_story(advantages=0, disadvantages=0):
    """ Rolls a number from 1 to 4. Adds advantage or disadvantages of 4 or less. 
    
    :param advantages: Optional. Adds advantages to roll.
    :type advantages: int
    :param disadvantages: Optional. Adds disadvantages to roll.
    :type disadvantages: int
    :raise rolls.InvalidNumberError: If advantages or disantages is > 4 or is negative.
    :return: A number from 1 to 4.
    :rtype: int
    """   
    if  (advantages > 4) or (advantages < 0) or (disadvantages > 4) or (disadvantages < 0):
        return InvalidNumberError
    return random.randint(1+advantages, 4-disadvantages)


