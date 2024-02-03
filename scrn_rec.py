from PIL import Image
import pytesseract
import json

# Set the path to the Tesseract executable (change accordingly)
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Open the image using Pillow (PIL)
image_path = 'PATH.jpg'
try:
    img = Image.open(image_path)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')

    # Create a dictionary to store the extracted text
    result_dict = {'extracted_text': text}

    # Define the path for the JSON file
    json_file_path = 'output.json'

    # Write the dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(result_dict, json_file, indent=4)

    print(f"Extracted text has been saved to {json_file_path}")
except Exception as e:
    print(f"Error: {e}")
