import os
from PIL import Image

def crop_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") and "a" in filename:
            file_path = os.path.join(folder_path, filename)
            image = Image.open(file_path)
            width, height = image.size

            margin = int(width * 0.07)  

            left_crop = image.crop((margin, 0, width // 2, height))
            left_filename = filename.replace("a", "b")
            left_crop.save(os.path.join(folder_path, left_filename))

            right_crop = image.crop((width // 2, 0, width - margin, height))
            right_filename = filename.replace("a", "c")
            right_crop.save(os.path.join(folder_path, right_filename))

# Set path to the folder containing images
folder_path = r"C:\Users\DANISH LAPTOP\Desktop\Crop Multiple Images Using Python"
crop_images_in_folder(folder_path)
