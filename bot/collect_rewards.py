import os
import time
from bot.loading_screen import LoadingScreen
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier


class CollectRewards:
    def __init__(self):
        pass

    def after_mission(self):
        count = 0
        if self.is_winner():
            print("Vencedor. Continuando")
            self.winner_mission_continue()
        elif self.is_defeated():
            print("Perdedor. Continuando")
            self.return_to_map()
        else:
            if count > 5:
                print("Recompensa não encontrada. Encerrando")
                os._exit(0)

            count += 1
            time.sleep(2)

    def return_to_map(self):
        cm = ClickManager()
        click_location = (400, 986)

        while self.is_defeated():
            cm.click_with_variation(click_location, 50, 15)
            print("retornar ao mapa")
            time.sleep(1)

        print("Inicio do loading")
        LoadingScreen.wait()
        time.sleep(2)

    def winner_mission_continue(self):
        cm = ClickManager()

        print("continuando")
        click_location = (284, 981)

        while self.is_winner():
            cm.click_with_variation(click_location, 50, 15)
            print("retornando ao mapa para coletar recompensa")
            time.sleep(1)

        print("Inicio do loading")
        LoadingScreen.wait()

        time.sleep(3)
        self.collect_mission_reward()

    def collect_mission_reward(self):
        cm = ClickManager()

        image_path = "bot/screenshots/buttons/get_mission_reward_button.png"
        screen_region = (224, 799, 108, 31)
        click_location = (279, 810)

        cm.click_if_image_found_with_variation(
            image_path, click_location, screen_region, 30, 15)
        time.sleep(2)

    def is_defeated(self):
        im = ImageIdentifier()
        image_path = "bot/screenshots/buttons/try_again_button.png"
        screen_region = (96, 967, 125, 33)

        return im.is_image_on_screen(image_path, screen_region)

    def is_winner(self):
        im = ImageIdentifier()
        image_path = "bot/screenshots/buttons/win_continue_button.png"
        screen_region = (204, 966, 152, 34)

        return im.is_image_on_screen(image_path, screen_region)

    # def collect_chest(self):
    #     cm = ClickManager()

    #     cm.click_with_variation((57, 971), 15, 15)
    #     time.sleep(1)

    # def have_chest(self):
    #     im = ImageIdentifier()
    #     image_path = "bot/screenshots/have_chest_reward.png"
    #     screen_region = (13, 394, 89, 90)

    #     return im.is_image_on_screen(image_path, screen_region)