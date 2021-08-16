import pytesseract
from PIL import Image

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
    output = pytesseract.image_to_string((Image.open("im1_crop.jpg")))
    print(output)
