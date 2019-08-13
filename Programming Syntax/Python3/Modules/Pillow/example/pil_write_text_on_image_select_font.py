from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (100, 30), color = (73, 109, 137))

fnt = ImageFont.truetype('ARIAL.TTF', 15) #Note: using .ttf fonts requires using .truetype()
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')
