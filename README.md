# iPhone Image Prepare for LoRA Training

This script prepares iPhone images for LoRA (Low-Rank Adaptation) training by addressing common issues with image orientation and metadata.

## Problem Statement

When training LoRA models with images from an iPhone, a common issue arises: the LoRA training process doesn't read the image metadata correctly, particularly the orientation information. This can result in training on images that appear rotated incorrectly. For example, a vertical image of a bottle might be processed as if it were lying on its side.

This script solves this problem by:
1. Stripping the metadata from the images, including orientation information.
2. Optionally rotating the images 90 degrees clockwise to ensure correct orientation.

By preprocessing your iPhone images with this script, you can ensure that your LoRA model trains on correctly oriented images, improving the quality and accuracy of your results.

## Features

- Strips metadata from images, resolving orientation issues
- Optional 90-degree clockwise rotation to correct image orientation
- Supports various image formats (JPG, PNG, etc.)
- Skips hidden files and non-image files
- User-friendly prompts for input and output folders

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
1. Input folder path (where your original iPhone images are stored)
2. Output folder path (where the processed images will be saved)
3. Whether to rotate images (y/n) - use this if your images need 90-degree rotation

The script will process all valid images in the input folder and save the corrected versions to the output folder.

## Best Practices for LoRA Training

- Always check a sample of your processed images before training to ensure correct orientation.
- If you notice images are still incorrectly oriented after processing, try running the script again with the rotation option set to the opposite of your previous choice.
- Consistent image orientation is crucial for effective LoRA training, especially for models that are sensitive to object orientation (e.g., models for recognizing or generating specific objects or scenes).


## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue if you have suggestions or encounter problems.
