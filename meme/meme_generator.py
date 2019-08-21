from PIL import Image, ImageDraw, ImageFont
import textwrap

print('hello')
#load image
image = Image.open('./pictures/picture.jpg')
draw = ImageDraw.Draw(image)
image.show()
image_width, image_height = image.size

#Load font
#font = ImageFont.truetype(font='./fonts/impact/impact.ttf', size=int(image_height/10))

#wrap text
#top_text = 'top text'
#bottom_text = 'bottom text'

#char_width, char_height = font.getsize('A')
#print(char_height)