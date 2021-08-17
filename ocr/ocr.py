import pytesseract
from PIL import Image
import cv2
import re
import os

from template import get_template_crop_values

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"


def crop_roi(raw_img_filename, crop_values, return_img_object=False):
    img = cv2.imread(raw_img_filename)
    roi = img[crop_values["ymin"]: crop_values["ymax"], crop_values["xmin"]: crop_values["xmax"]]

    if return_img_object:
        return roi

    cropped_image_filename = "assets/cropped/{}_cropped.jpg".format("test")
    cv2.imwrite(cropped_image_filename, roi)

    return cropped_image_filename


def run_tesseract_given_path(img_filename):
    img = Image.open(img_filename)
    output = pytesseract.image_to_string(img)

    return re.sub(r"[^0-9.,$]+", r' ', output)


def run_tesseract(img):
    output = pytesseract.image_to_string(img)

    return re.sub(r"[^0-9.,$]+", r' ', output)


def run_ocr(folder_path, template_name):
    ACCEPTABLE_IMAGE_TYPE = ('.png', '.jpg', '.jpeg')
    files = os.listdir(folder_path)
    output_list = []
    for file in files:
        path = os.path.join(folder_path, file)
        print(path)
        if os.path.isfile(path) and file.lower().endswith(ACCEPTABLE_IMAGE_TYPE):
            print(path)
            crop_values = get_template_crop_values(template_name)
            try:
                img = Image.fromarray(crop_roi(path, crop_values, return_img_object=True))
                output_list.append(run_tesseract(img))
            except ValueError as e:
                print(e)

    if output_list is not []:
        save_output(output_list)


def save_output(output_list):
    with open("ocr_output.txt", "w+") as f:
        f.writelines(output_list)
