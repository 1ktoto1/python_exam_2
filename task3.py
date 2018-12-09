
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByCompetition(Number, Competititon, Score = 0):

    if Competititon == []:
        return Score
    Score = sum(dataset[Number][Competititon[0]])

    return recursionByCompetition(Number, Competititon[1:], Score)



def recursionByNumber(Numbers = list(dataset.keys()), result_dict = dict()):

    if Numbers == []:
        return result_dict

    Number = Numbers[0]
    Competition = list(dataset[Number].keys())
    Score = recursionByCompetition(Number, Competition)
    result_dict[Number] = Score
    return recursionByNumber(Numbers[1:], result_dict)


print("Task 3")

result = recursionByNumber()
print(result)

print("\n\n")



