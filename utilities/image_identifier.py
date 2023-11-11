import pyautogui


class ImageIdentifier:
    def __init__(self):
        pass

    # busca a imagem requisitada podendo ser adicionado uma região de busca
    def is_image_on_screen(self, image_path, region=None, confidence=0.8):
        screen = pyautogui.screenshot(region=region)
        screen.save("captured_region.png")
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        return location is not None
