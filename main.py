from file_reader.csv_reader import InsultReader
from insult.insult_generator import Insultor
from meme.meme_generator import MemeGenerator
import random
import os

insults_filepath = './file_reader/insults.csv'
font_filepath = './meme/fonts/impact/impact.ttf'
base_image_dir = './meme/pictures/base_images/'
completed_meme_filepath = './meme/pictures/completed_meme/meme.jpg'

base_image_list = os.listdir(base_image_dir)

insultReader = InsultReader(insults_filepath)
insultor = Insultor(insultReader.get_insults())
meme_generator = MemeGenerator(completed_meme_filepath, font_filepath)

meme_generator.generate_meme(
    base_image_dir + random.choice(os.listdir(base_image_dir)),
    insultor.generate_insult())
