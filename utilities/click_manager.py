from utilities.image_identifier import ImageIdentifier
import pyautogui
import random
from utilities.custom_timer import CustomTimer


class ClickManager:
    ii = ImageIdentifier()

    def __init__(self):
        pass

    def normal_click(self, coordinates, duration=0.1):
        x, y = coordinates
        pyautogui.click(x, y, duration=duration)

    def long_click(self, coordinates, duration=1):
        x, y = coordinates
        pyautogui.mouseDown(x, y)
        CustomTimer.sleep(duration)
        pyautogui.mouseUp(x, y)

    def drag_and_drop(self, start_coordinates, end_coordinates, duration=1):
        start_x, start_y = start_coordinates
        end_x, end_y = end_coordinates

        pyautogui.mouseDown(start_x, start_y)
        CustomTimer.sleep(duration)
        pyautogui.moveTo(end_x, end_y)
        pyautogui.mouseUp()

    def click_with_variation(self, base_coordinates, x_variation, y_variation):
        base_x, base_y = base_coordinates
        x = random.uniform(base_x - x_variation, base_x + x_variation)
        y = random.uniform(base_y - y_variation, base_y + y_variation)
        self.normal_click((x, y))

    def click_if_image_found(self, image_path, click_location, search_region=None):
        ii = ImageIdentifier()
        if ii.is_image_on_screen(image_path, region=search_region):
            self.normal_click(click_location)
        else:
            print("Imagem não encontrada na tela")

    def click_if_image_found_with_variation(self, image_path, click_location, search_region=None, x_variation=10, y_variation=10):
        ii = ImageIdentifier()
        if ii.is_image_on_screen(image_path, search_region):
            self.click_with_variation(click_location, x_variation, y_variation)
        else:
            print("Imagem não encontrada na tela")
