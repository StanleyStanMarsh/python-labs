# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)
    res = 0
    for dict_ in data:
        res += dict_['score'] * dict_['weight']
    return round(res, 3)


print(task())
