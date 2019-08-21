from file_reader.csv_reader import InsultReader
from insult.insult_generator import Insultor

filepath = 'file_reader/insults.csv'

insultReader = InsultReader(filepath)

insultor = Insultor(insultReader.get_insults())

print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())
print(insultor.generate_insult())