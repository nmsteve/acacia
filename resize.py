from PIL import Image

# Open the image file
input_file = 'imagesOut/17.jpg'
image = Image.open(input_file)

# Resize the image to 350x350 pixels
resized_image = image.resize((600, 400))

# Save the resized image
output_file = 'logo.jpg'
resized_image.save(output_file)