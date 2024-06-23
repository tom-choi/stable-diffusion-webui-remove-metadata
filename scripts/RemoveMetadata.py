import modules.scripts as scripts
import gradio as gr
import os
from PIL import Image
from PIL.ExifTags import TAGS

from modules import script_callbacks

def remove_metadata(file):
    """
    Removes the metadata from an image file and saves a new file with a prefix.
    
    Args:
        file (Gradio.File): The image file object.
    """
    # Open the image from the Gradio File object
    image = Image.open(file)
        
    # Get the directory and filename
    directory, filename = os.path.split(file.name)
    name, extension = os.path.splitext(filename)
        
    # Create the new filename with a prefix
    new_filename = f"no_metadata_{name}{extension}"
    new_path = os.path.join(directory, new_filename)
        
    # Remove the EXIF data and save the new file
    image.save(new_path, optimize=True, quality=100, exif=None)

    print(f"Metadata removed from {file.name}")
    print(f"New file saved as: {new_path}")
    
    return Image.open(new_path)

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            file_input = gr.File(
                label="Select an image"
            )
            gallery = gr.Gallery(
                label="Image",
                show_label=False,
            )
        with gr.Row():
            btn = gr.Button(
                "Remove Metadata"
            ).style(
                full_width=False
            )

        btn.click(
            remove_metadata,
            inputs = [file_input],
            outputs = [gallery],
        )

        return [(ui_component, "Remove Metadata", "extension_example_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)