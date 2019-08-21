class Insults:

    def __init__(self, start_list: list, middle_list: list, end_list: list):
        self._start_list = start_list
        self._middle_list = middle_list
        self._end_list = end_list

    @property
    def start_list(self) -> list:
        return self._start_list

    @property
    def middle_list(self) -> list:
        return self._middle_list

    @property
    def end_list(self) -> list:
        return self._end_list
