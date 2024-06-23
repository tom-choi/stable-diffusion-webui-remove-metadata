# import modules.scripts as scripts
import gradio as gr
import os
from PIL import Image
from PIL.ExifTags import TAGS

# from modules import script_callbacks

def recreate_metadata(image_path):
    """
    Removes the metadata from an image file and saves a new file with a prefix.
    
    Args:
        image_path (str): The path to the image file.
    """
    print(image_path)
    image = Image.open(image_path)
    
    # Get the directory and filename
    directory, filename = os.path.split(image_path)
    name, extension = os.path.splitext(filename)
    
    # Create the new filename with a prefix
    new_filename = f"no_metadata_{name}{extension}"
    new_path = os.path.join(directory, new_filename)
    
    # Remove the EXIF data and save the new file
    print(new_path)
    image.save(new_path, optimize=True, quality=100)

    print(f"Metadata removed from {image_path}")
    print(f"New file saved as: {new_path}")
    
    return new_path

with gr.Blocks(analytics_enabled=False) as ui_component:
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Input Image", type="filepath")
            btn = gr.Button("Recreate Image with Metadata Removed")
        with gr.Column():
            output_image = gr.Gallery(label="Output Image", type="filepath")
    btn.click(recreate_metadata, inputs=input_image, outputs=output_image)

    ui_component.launch()
    # return [(ui_component, "Remove Metadata", "extension_example_tab")]

# def on_ui_tabs():
#     with gr.Blocks(analytics_enabled=False) as ui_component:
#         with gr.Row():
#             with gr.Column():
#                 input_image = gr.Image(label="Input Image", type="pil")
#                 btn = gr.Button("Recreate Image with Metadata Removed")
#             with gr.Column():
#                 output_image = gr.Gallery(label="Output Image")
#         btn.click(recreate_metadata, inputs=input_image, outputs=output_image)

#         # ui_component.launch()
#         return [(ui_component, "Remove Metadata", "extension_example_tab")]

# script_callbacks.on_ui_tabs(on_ui_tabs)