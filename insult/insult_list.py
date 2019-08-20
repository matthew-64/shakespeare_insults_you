import random


class InsultList:

    _list: object

    def __init__(self, my_list: list):
        self._list = my_list

    def get_random_value(self) -> list:
        return random.choice(self._list)
