import modules.scripts as scripts
import gradio as gr
import os
from PIL import Image
from PIL.ExifTags import TAGS

from modules import script_callbacks

def remove_metadata(image_path):
    """
    Removes the metadata from an image file and saves a new file with a prefix.
    
    Args:
        image_path (str): The path to the image file.
    """
    image = Image.open(image_path)
    
    # Get the directory and filename
    directory, filename = os.path.split(image_path)
    name, extension = os.path.splitext(filename)
    
    # Create the new filename with a prefix
    new_filename = f"no_metadata_{name}{extension}"
    new_path = os.path.join(directory, new_filename)
    
    # Remove the EXIF data and save the new file
    image.save(new_path, optimize=True, quality=100)

    print(f"Metadata removed from {image_path}")
    print(f"New file saved as: {new_path}")
    
    return new_path

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            checkbox = gr.Checkbox(
                True,
                label="Show image"
            )
            btn = gr.Button(
                "Remove Metadata"
            ).style(
                full_width=False
            )
        with gr.Row():
            file_input = gr.File(
                label="Select an image"
            )
            gallery = gr.Gallery(
                label="Dummy Image",
                show_label=False,
            )

        btn.click(
            remove_metadata,
            inputs = [file_input],
            outputs = [gallery],
        )

        return [(ui_component, "Extension Example", "extension_example_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)


# from PIL import Image
# from PIL.ExifTags import TAGS
# import os

# def remove_metadata(image_path):
#     """
#     Removes the metadata from an image file and saves a new file with a prefix.
    
#     Args:
#         image_path (str): The path to the image file.
#     """
#     image = Image.open(image_path)
    
#     # Get the directory and filename
#     directory, filename = os.path.split(image_path)
#     name, extension = os.path.splitext(filename)
    
#     # Create the new filename with a prefix
#     new_filename = f"no_metadata_{name}{extension}"
#     new_path = os.path.join(directory, new_filename)
    
#     # Remove the EXIF data and save the new file
#     image.save(new_path, optimize=True, quality=100)

#     print(f"Metadata removed from {image_path}")
#     print(f"New file saved as: {new_path}")

# # Usage example
# remove_metadata("G:\github\\novelai\\novelai-webui-10-9update\outputs\extras-images\\00082.png")