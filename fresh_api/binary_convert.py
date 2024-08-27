# Python script to convert binary to image
import base64

with open("core_utilisateur-image.bin", "rb") as binary_file:
    binary_data = binary_file.read()

with open("output_image.png", "wb") as image_file:
    image_file.write(binary_data)

print("Image created successfully as output_image.png")
