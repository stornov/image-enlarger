from PIL import Image, ImageDraw
image = Image.open("file.png")

multiplier = int(input())

# Collect data from a given image
size = image.size  # We get tuple (width, height)
new_size = image.size[0] * multiplier, image.size[1] * multiplier
mode = image.mode
format = image.format

# Get pixel colors list of for a given image...
pixel_colors = list(image.getdata())
# ... and divide it into "height" equal parts
pixel_colors = [pixel_colors[i:i+size[0]] for i in range(0, len(pixel_colors), size[0])]

# Create a pixel colors list for a new image
new_pixel_colors = []
for i in pixel_colors:
    for j in range(multiplier):
        [new_pixel_colors.append(val) for val in i for _ in range(multiplier)]

# Create a coordinate list for a new image
coordinates = []
for y in range(0,new_size[1]):
    for x in range(0,new_size[0]):
        coordinates.append((x,y))

# Create new image and save it
img = Image.new("RGB", new_size, (255,255,255))
draw = ImageDraw.Draw(img)
for i in range(new_size[0]*new_size[1]):
    draw.point(coordinates[i], new_pixel_colors[i])
img.save(f"result.{lower(format)}", format)
