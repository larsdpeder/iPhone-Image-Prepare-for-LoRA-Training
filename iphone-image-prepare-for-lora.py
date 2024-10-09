import os
from PIL import Image
import imghdr

def is_valid_image(file_path):
    return imghdr.what(file_path) is not None

def prepare_images_for_lora(input_folder, output_folder, rotate_90_clockwise=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.startswith('.'):
            continue

        input_path = os.path.join(input_folder, filename)
        
        if not os.path.isfile(input_path) or not is_valid_image(input_path):
            print(f"Skipping: {filename} (not a valid image file)")
            continue

        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                data = list(img.getdata())
                image_without_exif = Image.new(img.mode, img.size)
                image_without_exif.putdata(data)

                if rotate_90_clockwise:
                    image_without_exif = image_without_exif.rotate(-90, expand=True)

                image_without_exif.save(output_path)

            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

def main():
    print("iPhone Image Prepare for LoRA Training")
    input_folder = input("Enter the path to the input folder: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()
    rotate_option = input("Rotate images 90 degrees clockwise? (y/n): ").strip().lower()
    
    rotate_images = rotate_option == 'y'

    prepare_images_for_lora(input_folder, output_folder, rotate_90_clockwise=rotate_images)
    print("Processing complete!")

if __name__ == "__main__":
    main()
