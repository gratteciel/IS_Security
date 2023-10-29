import sys
from PIL import Image

width = 1920
height = 1080

image_a_cacher = Image.open("image_finale.bmp")

result_image = Image.new("RGB", (width, height), "white")

for i in range(width):
    for j in range(height):
        pixel_ac = image_a_cacher.getpixel((i, j))

        #Décaler les bits de poids faible en bits de poids fort (utiliser un décalage à gauche <<)
        pixel_ac = (pixel_ac[0] << 5, pixel_ac[1] << 5, pixel_ac[2] << 5)

        # Ecrêter chaque composante de couleur sur 8 bits (utiliser un & logique)
        pixel_ac = (pixel_ac[0] & 0b11111111, pixel_ac[1] & 0b11111111, pixel_ac[2] & 0b11111111)

        # Update the result image with the modified pixel
        result_image.putpixel((i, j), pixel_ac)

# Save the resulting image as a BMP
result_image.save("result_image.bmp", "BMP")

#close image
image_a_cacher.close()
