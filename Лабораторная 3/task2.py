# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sep=','):
    first_group = set(str1.split(sep))
    second_group = set(str2.split(sep))

    common_participants = list(first_group.intersection(second_group))
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
