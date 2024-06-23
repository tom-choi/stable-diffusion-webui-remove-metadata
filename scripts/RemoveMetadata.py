import modules.scripts as scripts
import gradio as gr
import os
from PIL import Image
from PIL.ExifTags import TAGS

from modules import script_callbacks

def recreate_metadata(input_image):
    """
    This function takes an input image, removes its metadata, and saves a new image with the metadata removed.
    
    Parameters:
    input_image (PIL.Image.Image): The input image to be processed.
    
    Returns:
    PIL.Image.Image: The new image with the metadata removed.
    """
    # Load the input image
    img = Image.open(input_image)
    
    # Remove the metadata
    img_no_metadata = Image.new(img.mode, img.size)
    img_no_metadata.putdata(list(img.getdata()))
    
    # Save the new image with the metadata removed
    new_filename = os.path.splitext(os.path.basename(input_image))[0] + "_no_metadata.png"
    img_no_metadata.save(new_filename)
    
    return img_no_metadata

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            with gr.Column():
                input_image = gr.Image(label="Input Image")
                btn = gr.Button("Recreate Image with Metadata Removed")
            with gr.Column():
                output_image = gr.Image(label="Output Image")

        return [(ui_component, "Remove Metadata", "extension_example_tab")]
    # Create the Gradio UI
    # with gr.Blocks() as demo:
    #     with gr.Row():
    #         with gr.Column():
    #             input_image = gr.Image(label="Input Image")
    #             btn = gr.Button("Recreate Image with Metadata Removed")
    #         with gr.Column():
    #             output_image = gr.Image(label="Output Image")
        
    #     btn.click(recreate_metadata, inputs=input_image, outputs=output_image)

script_callbacks.on_ui_tabs(on_ui_tabs)