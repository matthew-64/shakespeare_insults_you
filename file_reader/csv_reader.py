from insult.insult_list import InsultList


class InsultReader:

    def __init__(self, filepath):
        self._filepath = filepath

    def get_insult_lists(self):
        list_start = []
        list_middle = []
        list_end = []
        with open(self._filepath, 'r') as f:
            for line in f:
                words = line.split(',')
                list_start.append(words[0])
                list_middle.append(words[1])
                list_end.append(words[2].strip())
        return [InsultList(list_start), InsultList(list_middle), InsultList(list_end)]
