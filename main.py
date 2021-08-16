from ocr import ocr

if __name__ == '__main__':
    # Define crop values
    # eg: 713 734 426 545
    crop_values = {"xmin": 426, "ymin": 713, "xmax": 545, "ymax": 734}

    # Define image to process
    img_filename = "assets/examples/im1.jpg"

    # Crop region of interest and save
    cropped_roi_filename = ocr.crop_roi(img_filename, crop_values)
    print("Cropped ROI saved at: {}".format(cropped_roi_filename))

    # Run OCR on roi
    result = ocr.run_tesseract(cropped_roi_filename)
    print(result)
