import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'


def rec_text(image):
    return pytesseract.image_to_string(image, lang='rus').replace("\n", ' ').lower()
