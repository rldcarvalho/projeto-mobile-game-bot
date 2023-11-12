import pyautogui
import pytesseract


class ImageIdentifier:
    def __init__(self):
        pass

    # busca a imagem requisitada podendo ser adicionado uma região de busca
    def is_image_on_screen(self, image_path, region=None, confidence=0.8):
        screen = pyautogui.screenshot(region=region)
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        return location is not None

    def extract_text_in_image(self, region=None):
        screen = pyautogui.screenshot(region=region)

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        text = pytesseract.image_to_string(screen, lang="por")

        return ' '.join(text.split())
