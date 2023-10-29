import sys
from PIL import Image

width = 1920
height = 1080

# Create a new image to store the final result
result_image = Image.new("RGB", (width, height), "white")

image_a_cacher = Image.open("image_a_cacher.jpg")
image_conteneur = Image.open("image_conteneur.jpeg")

for i in range(width):
    for j in range(height):
        pixel_ac = image_a_cacher.getpixel((i, j))
        pixel_c = image_conteneur.getpixel((i, j))

        # Supprimer les bits de poids faible du conteneur (utiliser un & logique)
        pixel_c = (pixel_c[0] & 0b11111100, pixel_c[1] & 0b11111100, pixel_c[2] & 0b11111100)

        # Décaler les bits de poids fort en bits de poids faible du secret (utiliser un décalage à droite : >>)
        pixel_ac = (pixel_ac[0] >> 5, pixel_ac[1] >> 5, pixel_ac[2] >> 5)

        pixel_c = (pixel_c[0] | pixel_ac[0], pixel_c[1] | pixel_ac[1], pixel_c[2] | pixel_ac[2])

        # Update the result image with the modified pixel
        result_image.putpixel((i, j), pixel_c)

# Save the resulting image as a BMP
result_image.save("image_finale.bmp", "BMP")
