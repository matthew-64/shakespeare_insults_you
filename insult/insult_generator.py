from insult.insults import Insults
import random


class Insultor:

    def __init__(self, insults: Insults):
        self._insults = insults

    def generate_insult(self) -> str:
        return 'Thou ' \
               + random.choice(self._insults.start_list) + ' ' \
               + random.choice(self._insults.middle_list) + ' ' \
               + random.choice(self._insults.end_list)
