import pytesseract
from PIL import Image
import cv2
import re


def crop_roi(raw_img_filename, crop_values):
    img = cv2.imread(raw_img_filename)
    roi = img[crop_values["ymin"]: crop_values["ymax"], crop_values["xmin"]: crop_values["xmax"]]

    cropped_image_filename = "assets/cropped/{}_cropped.jpg".format("test")
    cv2.imwrite(cropped_image_filename, roi)

    return cropped_image_filename


def run_tesseract(img_filename):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
    img = Image.open(img_filename)
    output = pytesseract.image_to_string(img)

    return re.sub(r"[^0-9.,$]+", r' ', output)
