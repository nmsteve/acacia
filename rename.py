from PIL import Image
import os

# Set the input and output directories
input_dir = 'imagesIn'
output_dir = 'imagesOut'

# Initialize a counter
counter = 1

# Loop through all the JPEG files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.jpg'):
        # Open the image file
        input_file = os.path.join(input_dir, file_name)
        image = Image.open(input_file)
        
        # Create a new file name using the counter
        new_file_name = f"{counter}.jpg"
        
        # Construct the file path for the output image
        output_file = os.path.join(output_dir, new_file_name)
        
        # Save the image with the new name
        image.save(output_file)
        
        # Increment the counter
        counter += 1
