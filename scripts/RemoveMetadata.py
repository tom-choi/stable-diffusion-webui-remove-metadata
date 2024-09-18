import modules.scripts as scripts
import gradio as gr
import os
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS

from modules import shared, scripts
from modules import script_callbacks

def get_next_filename(directory, base_name, extension):
    """
    Finds the next available filename in the given directory.

    Args:
        directory (str): The directory to search for existing files.
        base_name (str): The base name for the file.
        extension (str): The file extension.

    Returns:
        str: The next available filename.
    """
    existing_files = os.listdir(directory)
    existing_numbers = []
    
    for file in existing_files:
        if file.startswith(base_name) and file.endswith(extension):
            num_part = file[len(base_name):-len(extension)]
            if num_part.isdigit():
                existing_numbers.append(int(num_part))
    
    next_number = 1
    while next_number in existing_numbers:
        next_number += 1
    
    return f"{base_name}{next_number:04d}{extension}"

def recreate_metadata(image_path):
    """
    Removes the metadata from an image file and saves a new file with an incremented number.
    
    Args:
        image_path (str): The path to the image file.
    """
    image = Image.open(image_path)
    
    # Get the directory and filename
    directory, filename = os.path.split(image_path)
    name, extension = os.path.splitext(filename)
    
    # Create the new filename with an incremented number
    output_directory = Path(scripts.basedir(), 'outputs', 'no-metadata-images')
    output_directory.mkdir(parents=True, exist_ok=True)
    
    base_name = "no_metadata_" + name
    new_filename = get_next_filename(output_directory, base_name, extension)
    new_path = output_directory / new_filename

    # Save the image without metadata
    image.save(new_path, optimize=True, quality=100)

    print(f"Metadata removed from {image_path}")
    print(f"New file saved as: {new_path}")
    
    return new_path


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(label="Input Image", type="filepath")
                btn = gr.Button("Recreate Image with Metadata Removed")
            with gr.Column():
                output_image = gr.Image(label="Please Ignore Here, place your image in left hand side, 這裡留空，請將您的圖片放在左側，將來會用來顯示結果", type="filepath")
        
            btn.click(recreate_metadata, inputs=input_image, outputs=input_image)

        # ui_component.launch()
        return [(ui_component, "Remove Metadata", "extension_example_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)