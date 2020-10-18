import os
import re

import cv2.cv2 as cv2
import pytesseract


def get_text_from_image(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # inverts the image
    gray = cv2.bitwise_not(gray)
    extracted_text = pytesseract.image_to_string(gray, lang='eng', config='--psm 3')
    return extracted_text


def remove_symbols(input_str):
    # removes unwanted characters and symbols
    input_str = re.sub('[^a-zA-Z]+', ' ', input_str)
    input_str_list = input_str.split(" ")
    output_str_list = []
    # remove all the words if their size is less than 2
    for val in input_str_list:
        if len(val) >= 2:
            output_str_list.append(val)
    # join filtered words and capitalize each word using title method
    return " ".join(output_str_list).title()


images = os.listdir("static/text_extraction_images")
for image in images:
    name = get_text_from_image(f"static/text_extraction_images/{image}")
    print(f"From file = {image}, Got = {remove_symbols(name)}")
