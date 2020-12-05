from PIL import Image, ImageDraw, ImageFont

height = 1520
width = 720
font_size = 110


def affirm_maker(text):
	img = Image.new('RGB', (width, height), color = 'black')


	fnt = ImageFont.truetype("E:/Work/Godot/Projects/Awesome-Python-Codes/Affirmations-Maker/fonts/Nerko_One/NerkoOne-Regular.ttf", font_size)
	d = ImageDraw.Draw(img)

	h_pos = height / 2 - font_size  * 1.5
	w_pos = width / 2 - (len(text) ** 2) - font_size  

	d.text((w_pos, h_pos), text, font=fnt, fill=(255, 255, 255))

	#img.show()
	img.save("wallpapers/" + text.lower() + '.png')

words = []
with open("words.txt") as f:
	words = f.readlines()

for word in words:
	affirm_maker(word.strip())
affirm_maker("Thank You")