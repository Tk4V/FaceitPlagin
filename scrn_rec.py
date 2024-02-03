from PIL import Image
import pytesseract
import json

#PATH TO THE TESSERACT
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

#OPEN IMAGE
image_path = 'PATH.jpg'
try:
    img = Image.open(image_path)
    #IMAGE TO STR
    text = pytesseract.image_to_string(img, lang='eng')

    #CREATE JSON
    result_dict = {'extracted_text': text}

    #JSON PATH
    json_file_path = 'output.json'

    #OUTPUT TO FILE
    with open(json_file_path, 'w') as json_file:
        json.dump(result_dict, json_file, indent=4)

    print(f"Extracted text has been saved to {json_file_path}")
except Exception as e:
    print(f"Error: {e}")
