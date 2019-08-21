from insult.insults import Insults


class InsultReader:

    def __init__(self, filepath):
        self._filepath = filepath

    def get_insults(self) -> Insults:
        list_start = []
        list_middle = []
        list_end = []
        with open(self._filepath, 'r') as f:
            for line in f:
                words = line.split(',')
                list_start.append(words[0])
                list_middle.append(words[1])
                list_end.append(words[2].strip())
        return Insults(list_start, list_middle, list_end)
