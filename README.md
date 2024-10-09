# iPhone Image Prepare for LoRA Training

This script prepares iPhone images for LoRA (Low-Rank Adaptation) training by stripping metadata and optionally rotating images.

## Features

- Strips metadata from images
- Optional 90-degree clockwise rotation
- Supports various image formats (JPG, PNG, etc.)
- Skips hidden files and non-image files

## Requirements

- Python 3.6+
- Pillow library

## Installation

1. Clone this repository or download the script.
2. Install the required library:

```
pip install -r requirements.txt
```

## Usage

Run the script:

```
python iphone_image_prepare_for_lora.py
```

Follow the prompts to enter:
1. Input folder path
2. Output folder path
3. Whether to rotate images (y/n)

The script will process all valid images in the input folder and save them to the output folder.

## Notes

- Ensure you have sufficient disk space in the output location.
- The script preserves original filenames.
- Invalid or non-image files are skipped with a notification.

## License

This project is open source and available under the [MIT License](LICENSE).
