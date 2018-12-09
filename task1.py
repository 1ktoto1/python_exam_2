from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(auto, competition, score):
    if auto not in dataset :
        dataset = dataset.update(auto , competition)
    elif auto in dataset:
        for key in dataset:
            if key == auto:
                for i in dataset[key]:
                    if dataset[key][i].values() == score:
                        dataset.popitem(i)
                        dataset[key] = dataset.update(competition, score)
                    elif i == competition:
                        dataset = dataset[key].update(competition, score)



print("Task 1")

#Додати нового користувача та нову покупку
addUserProduct(?,?,?)

#Додати існуючому користувачу нову покупку нового продукту
addUserProduct(?,?,?)

#Додати існуючому користувачу нову покупку існуючого продукту
addUserProduct(?,?,?)

print(dataset)


print("\n\n")