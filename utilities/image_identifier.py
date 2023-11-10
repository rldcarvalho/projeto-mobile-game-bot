import pyautogui


class ImageIdentifier:
    def __init__(self):
        pass

    # busca a imagem requisitada podendo ser adicionado uma região de busca
    def is_image_on_screen(self, image_path, region=None):
        screen = pyautogui.screenshot(region=region)
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        return location is not None
