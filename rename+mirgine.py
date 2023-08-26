from PIL import Image, ImageOps
import os

#  rename then incrementally

# set the input and output directories
input_dir = '/imagesIn'
output_dir = '/imagesOut'

# initialize counter for file names
count = 1

# loop through all the JPEG files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.jpg'):
        # open the image file
        input_file = os.path.join(input_dir, file_name)
        image = Image.open(input_file)

        # add the margin to the image
        bordered_image = ImageOps.expand(image, border=margin_size, fill='white')

        # generate new file name
        new_file_name = f'image{count}.jpg'

        # save the new image to the output directory with the new file name
        output_file = os.path.join(output_dir, new_file_name)
        bordered_image.save(output_file)

        # delete the old image file
        os.remove(input_file)

        # increment the counter for file names
        count += 1
