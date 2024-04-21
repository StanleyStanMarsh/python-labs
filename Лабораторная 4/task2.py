# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as in_f:
        lines = [line for line in csv.reader(in_f)]

    list_of_dicts = []
    table_keys = lines[0]
    for line in lines[1:]:
        data = dict()
        for i in range(len(table_keys)):
            data[table_keys[i]] = line[i]
        list_of_dicts.append(data)

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as out_f:
        json.dump(list_of_dicts, out_f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
