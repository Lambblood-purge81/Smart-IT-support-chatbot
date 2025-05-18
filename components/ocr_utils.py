from PIL import Image
import pytesseract

def extract_text_from_image(image_file):
    img = Image.open(image_file)
    return pytesseract.image_to_string(img)
