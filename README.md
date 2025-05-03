# Crop Images Using Python

This Python program automates the process of cropping multiple images in a folder. It uses the Python Imaging Library (Pillow) to crop images based on specific criteria and provides several customizable options.

## Features

- Processes images in multiple formats: `.jpg`, `.jpeg`, `.png`.
- Crops images into two parts:
  - The left part, excluding a margin on the left.
  - The right part, excluding a margin on the right.
- Allows customization of the margin percentage for cropping.
- Saves cropped images in a specified output folder.
- Skips processing if cropped files already exist.
- Provides detailed logging for processed files and errors.
- Command-line arguments for flexibility:
  - Specify the input folder path (defaults to the current directory if not provided).
  - Specify the output folder path.
  - Set the margin percentage for cropping.

## How It Works

1. The program scans a folder for images containing the letter "a" in their filenames.
2. For each image:
   - It calculates a margin based on the specified percentage.
   - Crops the image into two parts:
     - The left crop: From the margin to the middle of the image.
     - The right crop: From the middle of the image to the width minus the margin.
   - Saves the cropped images with new filenames:
     - Replaces "a" with "b" for the left crop.
     - Replaces "a" with "c" for the right crop.

## Usage

1. Install the required library:
   ```bash
   pip install pillow
   ```

2. Run the script with the following command:
   ```bash
   python crop_images.py [folder_path] --output_folder <output_folder> --margin_percentage <margin_percentage>
   ```

   - `[folder_path]`: (Optional) Path to the folder containing images. Defaults to the current directory if not provided.
   - `--output_folder`: (Optional) Path to save cropped images. Default is `output`.
   - `--margin_percentage`: (Optional) Margin percentage for cropping. Default is `7`.

3. Examples:
   - Run the script in the current directory:
     ```bash
     python crop_images.py
     ```
   - Specify a custom folder path:
     ```bash
     python crop_images.py "C:\Users\DANISH LAPTOP\Desktop\Crop Multiple Images Using Python"
     ```
   - Specify a custom output folder:
     ```bash
     python crop_images.py --output_folder "C:\Users\DANISH LAPTOP\Desktop\Cropped Images"
     ```
   - Change the margin percentage:
     ```bash
     python crop_images.py --margin_percentage 10
     ```

## Example Output

If the folder contains an image named `examplea.jpg`, the program will generate:
- `exampleb.jpg` (left crop)
- `examplec.jpg` (right crop)

## Requirements

- Python 3.x
- Pillow library

## Logging

The program logs all actions, including:
- Files processed successfully.
- Errors encountered during processing.

Logs are displayed in the terminal for easy debugging.

## License

This project is licensed under the MIT License.