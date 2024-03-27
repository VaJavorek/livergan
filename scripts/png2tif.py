from PIL import Image
from pathlib import Path

# Function to convert PNG to TIFF with specified pixel size in mm
def convert_png_to_tiff(png_path, tiff_path, pixel_size_mm):
    # Load the .png image
    input_png = Image.open(png_path)
    
    # Convert pixel size from mm to inches (1 inch = 25.4 mm)
    pixel_size_inch = pixel_size_mm / 25.4
    
    # Calculate the resolution in pixels per inch (DPI)
    dpi = 1 / pixel_size_inch

    # Save the image as a .tif file with the specified resolution
    input_png.save(tiff_path, format='TIFF', dpi=(dpi, dpi), compression="tiff_lzw")
    print(f"Image saved as {tiff_path} with a resolution of {dpi:.2f} DPI.")

# Path to the uploaded .png file    
input_png_path = './PIG-002_J-18-0092_HE__-1_split_176.png'
output_tiff_path = 'desired_output_path.tif'

# Pixel size in mm as per the requirement
pixel_size_in_mm = 0.00000096

# Convert the PNG to TIFF with the specified pixel size
convert_png_to_tiff(input_png_path, output_tiff_path, pixel_size_in_mm)
