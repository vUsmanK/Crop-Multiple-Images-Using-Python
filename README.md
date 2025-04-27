# Crop Multiple Images Using Python

This Python program is designed to automate the process of cropping multiple images in a folder. It uses the Python Imaging Library (Pillow) to crop images based on specific criteria.

## Features

- Processes all `.jpg` images in a specified folder.
- Crops images into two parts:
  - The left part, excluding a margin on the left.
  - The right part, excluding a margin on the right.
- Renames the cropped images by replacing the letter "a" in the original filename with "b" (for the left crop) and "c" (for the right crop).

## How It Works

1. The program scans a folder for `.jpg` images containing the letter "a" in their filenames.
2. For each image:
   - It calculates a margin (7% of the image width).
   - Crops the image into two parts:
     - The left crop: From the margin to the middle of the image.
     - The right crop: From the middle of the image to the width minus the margin.
   - Saves the cropped images with new filenames.

## Usage

1. Install the required library:
   ```bash
   pip install pillow
   ```
2. Update the `folder_path` variable in the script to point to the folder containing your images.
3. Run the script:
   ```bash
   python "Crop Multiple Images Using Python.py"
   ```

## Example

If the folder contains an image named `examplea.jpg`, the program will generate:
- `exampleb.jpg` (left crop)
- `examplec.jpg` (right crop)

## Requirements

- Python 3.x
- Pillow library

## License

This project is licensed under the MIT License.
