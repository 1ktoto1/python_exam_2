from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getNumberAuto
from validators.lib import getCompetition
from validators.lib import getScore


from task1 import addUserProduct


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():
    #TODO
    Number = getNumberAuto()
    while not Number:
        print("It`s a not car number. Try again.")
        Number = getNumberAuto()

    Competition = getCompetition()
    while not Competition:
        print("It`s a not Competition. Try again.")
        Competition= getCompetition()

    Score = getScore()
    while not Score:
        print("It's a not Score. Try again.")
        Score = getScore()


    addUserProduct(Number , Competition , Score )



print("Task 1")
addUserProductValidator()
print(dataset)


print("\n\n")