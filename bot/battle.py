import time
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier


class Battle:
    def __init__(self):
        pass

    def start():
        cm = ClickManager()

        image_path = "bot/screenshots/start_button.png"
        search_region = (236, 806, 85, 61)
        click_location = (279, 839)

        cm.click_if_image_found_with_variation(
            image_path, click_location, search_region, 50, 50)

        time.sleep(0.5)

    def have_mana():
        id = ImageIdentifier()

        four_mana_path = "bot/screenshots/four_mana.png"
        four_mana_region = (160, 983, 157, 41)

        return id.is_image_on_screen(four_mana_path, four_mana_region)

    def play_minion():
        cm = ClickManager()

        minion_region_center = (340, 870)
        base_tower = (278, 670)

        cm.click_with_variation(minion_region_center, 200, 50)
        time.sleep(0.5)
        cm.click_with_variation(base_tower, 100, 50)
        time.sleep(0.5)

    def defend_tower(self):
        count = 0
        while count < 6:
            if (self.have_mana()):
                self.play_minion()
                count = 0
                time.sleep(1)
            else:
                count += 1
                print(count)
                time.sleep(2)
