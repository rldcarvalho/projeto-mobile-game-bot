import pyautogui
import pytesseract


class ImageIdentifier:
    def __init__(self):
        pass

    def is_image_on_screen(self, image_path, region=None, confidence=0.8):

        """
        Verifica se uma imagem está na tela.

        Parameters:
            image_path (str): O caminho da imagem a ser procurada.
            region (tuple): A região específica na tela onde procurar a imagem.
            confidence (float): O nível de confiança para a correspondência.

        Returns:
            bool: True se a imagem for encontrada, False caso contrário.
        """

        screen = pyautogui.screenshot(region=region)
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        return location is not None

    def extract_text_in_image(self, region=None):
        """
        Extrai texto de uma imagem na tela.

        Parameters:
            region (tuple): A região específica na tela onde extrair o texto.
            lang (str): O idioma para a extração de texto.

        Returns:
            str: O texto extraído da imagem.
        """

        screen = pyautogui.screenshot(region=region)

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        text = pytesseract.image_to_string(screen, lang="por")

        return ' '.join(text.split())
