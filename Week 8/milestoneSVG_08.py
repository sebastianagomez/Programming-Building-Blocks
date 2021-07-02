from PIL import Image

image_beach = Image.open("cse110_images/beach.jpg")
image_penguin = Image.open("cse110_images/penguin.jpg")

print(image_beach.size)
print(image_beach.format)

(width, height) = image_beach.size

print(f"Width: {width}")
print(f"Height: {height}")

pixels_beach = image_beach.load()

pixels_image_penguin = image_penguin.load()

print(pixels_image_penguin[0, 0])

for y in range(0, height):
    for x in range (0, width):
        (r, g, b) = pixels_image_penguin[x, y]
        if (r <= 150) and (g >= 180 and g <= 250) and (b <=165):
            pixels_image_penguin[x,y] = pixels_beach[x,y]

image_penguin.show()

image_penguin.save("the_new_image.jpg")

