# import gradio as gr
# import os
# from pathlib import Path
# from PIL import Image
# from PIL.ExifTags import TAGS

# def recreate_metadata(image_path):
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
#     Path(directory, 'outputs', 'no-metadata-images').mkdir(parents=True, exist_ok=True)
#     new_path = os.path.join(directory, 'outputs', 'no-metadata-images', new_filename)
#     tmp_path = os.path.join(directory, new_filename)

#     # Create a temp file to save the image without metadata
#     g = image.save(tmp_path, optimize=True, quality=100)
    
#     # Remove the EXIF data and save the new file
#     image.save(new_path, optimize=True, quality=100)

#     print(f"Metadata removed from {image_path}")
#     print(f"New file saved as: {new_path}")
    
#     return new_path

# with gr.Blocks(analytics_enabled=False) as ui_component:
#     with gr.Row():
#         with gr.Column():
#             input_image = gr.Image(label="Input Image", type="filepath")
#             btn = gr.Button("Recreate Image with Metadata Removed")
#         with gr.Column():
#             output_image = gr.Image(label="Please Ignore Here, place your image in left hand side, 這裡留空，請將您的圖片放在左側，將來會用來顯示結果", type="filepath")
    
#         btn.click(recreate_metadata, inputs=input_image, outputs=input_image)

# ui_component.launch()