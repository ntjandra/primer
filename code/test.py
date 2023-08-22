from rolls import *
from primer import *

def test_story_rolls():
    # Basic rolls
    print(roll_story())
    print(roll_story(1, 1))
    print(roll_story(0, 1))

    # Invalid rolls
    print(roll_story(0, 4))
    print(roll_story(4, 1))
    print(roll_story(5, 0))
    print(roll_story(0, 5))
    print(roll_story(-1, 0))
    print(roll_story(0, -1))


test_story_rolls()