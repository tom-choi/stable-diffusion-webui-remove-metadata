import modules.scripts as scripts
import gradio as gr
import os
from PIL import Image
from PIL.ExifTags import TAGS
import tempfile

from modules import script_callbacks

def remove_metadata(file):
    """
    Removes the metadata from an image file and saves a new file with a prefix.
    
    Args:
        file (Gradio.File): The image file object.
    """
    # Create a temporary file to save the image
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
        file.save(temp_file.name)
        image = Image.open(temp_file.name)
        
        # Get the directory and filename
        directory, filename = os.path.split(temp_file.name)
        name, extension = os.path.splitext(filename)
        
        # Create the new filename with a prefix
        new_filename = f"no_metadata_{name}{extension}"
        new_path = os.path.join(directory, new_filename)
        
        # Remove the EXIF data and save the new file
        image.save(new_path, optimize=True, quality=100)

    print(f"Metadata removed from {temp_file.name}")
    print(f"New file saved as: {new_path}")
    
    return new_path

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            file_input = gr.File(
                label="Select an image"
            )
            btn = gr.Button(
                "Remove Metadata"
            ).style(
                full_width=False
            )
        with gr.Row():
            gallery = gr.Gallery(
                label="Image",
                show_label=False,
            )

        btn.click(
            remove_metadata,
            inputs = [file_input],
            outputs = [gallery],
        )

        return [(ui_component, "Remove Metadata", "extension_example_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)

# # Usage example
# remove_metadata("G:\github\\novelai\\novelai-webui-10-9update\outputs\extras-images\\00082.png")