from PIL import Image, ImageDraw, ImageFont

text_margin = 0.1


class MemeGenerator:

    def __init__(self, completed_meme_path: str, font_filepath: str):
        self._completed_meme_path = completed_meme_path
        self._font_filepath = font_filepath

    def __calculate_font_size(self, insult: str, image: Image) -> int:
        font_size = 1
        font = ImageFont.truetype(self._font_filepath, font_size)
        while font.getsize(insult)[0] < (1 - text_margin) * image.size[0]:  # put text margin here
            font_size += 1
            font = ImageFont.truetype(self._font_filepath, font_size)
        return font_size

    def generate_meme(self, base_image_filepath: str, insult: str) -> None:
        image = Image.open(base_image_filepath)
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        font = ImageFont.truetype(self._font_filepath, self.__calculate_font_size(insult, image))
        text_pos_x = 5
        text_pos_y = int(image_height * 0.75)
        draw.text(xy=(text_pos_x, text_pos_y), text=insult, fill=(225, 69, 0), font=font)
        image.save(self._completed_meme_path)