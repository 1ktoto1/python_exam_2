
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getNumberAuto():

    user_input = input()

    if (re.match(r"/\w{2}\d{4}/gm", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getCompetition(dataset):

    user_input = input()
    if (re.match(r"/\w+\s{1}\w/gm", user_input) ):
        return user_input
    else:
        return False



"""
    Написати валідатор ....
    Правило валідації
"""


def getScore():

    user_input = input()
    if (re.match(r"/\d+\.\d+", user_input)):
        return user_input
    else:
        return False
