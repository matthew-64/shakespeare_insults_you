

class Insultor:

    def __init__(self, start_list: list, middle_list: list, end_list: list):
        self._start_list = start_list
        self._middle_list = middle_list
        self._end_list = end_list

    def generate_insult(self):
        return 'Thou ' \
               + self._start_list.get_random_value() + ' ' \
               + self._middle_list.get_random_value() + ' ' \
               + self._end_list.get_random_value()
