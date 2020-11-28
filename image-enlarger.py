from PIL import Image, ImageDraw
image = Image.open(r"E:\Files\file.png")

multiplier = int(input())

size = image.size
new_size = image.size[0] * multiplier, image.size[1] * multiplier
mode = image.mode
format = image.format

pixel_colors = list(image.getdata())
pixel_colors = [pixel_colors[i:i+size[0]] for i in range(0, len(pixel_colors), size[0])]

new_pixel_colors = []
for i in pixel_colors:
    for j in range(multiplier):
        [new_pixel_colors.append(val) for val in i for _ in range(multiplier)]

coordinates = []
for y in range(0,new_size[1]):
    for x in range(0,new_size[0]):
        coordinates.append((x,y))

img = Image.new("RGB", new_size, (255,255,255))
draw = ImageDraw.Draw(img)
for i in range(new_size[0]*new_size[1]):
    draw.point(coordinates[i], new_pixel_colors[i])
img.save(f"result.{lower(format)}", format)
