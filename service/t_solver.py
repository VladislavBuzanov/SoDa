import pytesseract
from server import Config

pytesseract.pytesseract.tesseract_cmd = Config.tesseract_path


def rec_text(image):
    return pytesseract.image_to_string(image, lang='rus').replace("\n", ' ').lower()
