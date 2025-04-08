"""from PIL import Image

im = Image.open("Kernal.png")

rgb_im = im.convert('RGB')

rgb_im.save('Kernal.jpg')"""

from PIL import Image
import os

def convert_png_to_jpg(file_path, output_path=None):
    """
    Convert a PNG image to a JPG image.
    
    Args:
        file_path (str): Path to the PNG image file.
        output_path (str): Path to save the converted JPG image. 
                           If None, saves in the same directory with .jpg extension.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found. Please check the file path.")
        return
    
    try:
        # Open the PNG image
        im = Image.open(file_path)
        
        # Convert to RGB
        rgb_im = im.convert('RGB')
        
        # Define output path if not provided
        if output_path is None:
            output_path = os.path.splitext(file_path)[0] + ".jpg"
        
        # Save the converted image
        rgb_im.save(output_path)
        print(f"Image converted and saved successfully at: {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    # Path to the input PNG file
    file_path = r"D:\Vs_Code\Python\ALL_Codes_Python\Own_Project_Com_Code\Kernal.png"
    
    # Optional: Provide an output path, or leave as None to save in the same directory
    output_path = r"D:\Vs_Code\Python\ALL_Codes_Python\Own_Project_Com_Code\K.jpg"
    
    # Convert the image
    convert_png_to_jpg(file_path, output_path)
