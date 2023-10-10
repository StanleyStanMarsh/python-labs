users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

visiting = {"Общее количество": 0, "Уникальные посещения": 0}

visiting["Общее количество"] = len(users)

unique = set(users)
visiting["Уникальные посещения"] = len(unique)

print(visiting)
