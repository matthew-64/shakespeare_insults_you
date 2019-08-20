from file_reader.csv_reader import InsultReader
from insult.insult_generator import Insultor

filepath = 'file_reader/insults.csv'

insultReader = InsultReader(filepath)
insult_lists = insultReader.get_insult_lists()

insultor = Insultor(insult_lists[0], insult_lists[1], insult_lists[2])

print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())