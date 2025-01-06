from PIL import Image

def image_converter(image_input, image_output_file, file_to_convert_to):
    """Will convert image to specified format"""

    try:
        image = Image.open(image_input)
        image.save(image_output_file, file_to_convert_to)
        print(f"Conversion to {image_output_file} successful!")
    except Exception as e:
        print(f"Exception encountered: {e}")



input_path = input("Enter the desired image file you want to convert: ")
output_path = input("Enter the output path you want your converted image to be called (include the .format of the desired file type at the end): ")
file_format = input("Enter the format of image you want your image to be converted to (i.e. PNG, JPEG etc.)")

#converts image to desired type
image_converter(input_path, output_path, file_format)

