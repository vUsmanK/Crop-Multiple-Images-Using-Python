import os
import logging
from PIL import Image
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def crop_images_in_folder(folder_path, output_folder, margin_percentage):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Created output directory: {output_folder}")

    processed_count = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")) and "a" in filename:
            try:
                file_path = os.path.join(folder_path, filename)
                image = Image.open(file_path)
                width, height = image.size

                margin = int(width * margin_percentage / 100)

                # Left crop
                left_crop = image.crop((margin, 0, width // 2, height))
                left_filename = filename.replace("a", "b")
                left_crop.save(os.path.join(output_folder, left_filename))
                logging.info(f"Saved left crop: {left_filename}")

                # Right crop
                right_crop = image.crop((width // 2, 0, width - margin, height))
                right_filename = filename.replace("a", "c")
                right_crop.save(os.path.join(output_folder, right_filename))
                logging.info(f"Saved right crop: {right_filename}")

                processed_count += 1
            except Exception as e:
                logging.error(f"Error processing file {filename}: {e}")

    logging.info(f"Processing complete. Total images processed: {processed_count}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Crop multiple images in a folder.")
    parser.add_argument(
        "folder_path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Path to the folder containing images. Defaults to the current directory.",
    )
    parser.add_argument(
        "--output_folder", type=str, default="output", help="Path to the folder to save cropped images."
    )
    parser.add_argument(
        "--margin_percentage", type=float, default=7.0, help="Margin percentage for cropping (default: 7%)."
    )
    args = parser.parse_args()

    # Run the cropping function
    crop_images_in_folder(args.folder_path, args.output_folder, args.margin_percentage)
