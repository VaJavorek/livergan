from skimage import io
from tifffile import imwrite
from pathlib import Path

# Function to convert PNG to TIFF with specified pixel size in mm
def convert_png_to_tiff_skimage(png_path, tiff_path, pixel_size_mm):
    # Load the .png image using skimage
    image_array = io.imread(png_path)
    
    # Convert pixel size from mm to meters for use with tifffile
    pixel_size_m = pixel_size_mm / 1000
    
    # Define the metadata for the TIFF file
    # In this metadata, 'XResolution' and 'YResolution' are the number of pixels per meter
    metadata = {
        'resolution': (1/pixel_size_m, 1/pixel_size_m),
        'metadata': {'unit': 'METRE'}
    }

    # Save the image as a .tif file with the specified metadata
    imwrite(tiff_path, image_array, **metadata)

    print(f"Image saved as {tiff_path} with a pixel size of {pixel_size_mm} mm.")

# Path to the uploaded .png file
input_png_path = str(Path('./PIG-002_J-18-0092_HE__-1_split_176.png').resolve())
output_tiff_path = str(Path('skimage.tif').resolve())

# Pixel size in mm as per the requirement
pixel_size_in_mm = 0.00000096

# Convert the PNG to TIFF with the specified pixel size
convert_png_to_tiff_skimage(input_png_path, output_tiff_path, pixel_size_in_mm)
