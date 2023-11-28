from bot.game_restarter import GameRestarter
from utilities.custom_timer import CustomTimer
from bot.loading_screen import LoadingScreen
from utilities.click_manager import click_with_variation, click_if_image_found_with_variation
from utilities.image_identifier import is_image_on_screen


class CollectRewards:
    def __init__(self):
        pass

    def after_mission(self):
        print("Coletando recompensas")
        count = 0
        while count <= 6:
            if self.is_winner():
                print("Vencedor. Continuando")
                self.winner_mission_continue()
                break
            elif self.is_defeated():
                print("Perdedor. Continuando")
                self.return_to_map()
                break
            else:
                if count > 5:
                    raise RuntimeError("Recompensa não encontrada.")
                count += 1
                CustomTimer.sleep(3, 1)

    def after_pvp(self):

        print("coletando XP")
        click_location = (284, 981)

        count = 0
        while count <= 6 and self.is_winner():
            click_with_variation(click_location, 50, 15)
            print("retornando a tela de pvp")
            count += 1
            CustomTimer.sleep(5, 1)

        if count > 5:
            raise RuntimeError("Emulador travou")

        LoadingScreen.wait()
        CustomTimer.sleep(2, 1)

    def return_to_map(self):
        click_location = (400, 986)

        while self.is_defeated():
            click_with_variation(click_location, 50, 15)
            print("retornar ao mapa")
            CustomTimer.sleep(3, 1)

        LoadingScreen.wait()
        CustomTimer.sleep(3, 1)

    def winner_mission_continue(self):
        click_location = (284, 981)

        while self.is_winner():
            click_with_variation(click_location, 50, 15)
            print("retornando ao mapa para coletar recompensa")
            CustomTimer.sleep(3, 1)

        LoadingScreen.wait()

        CustomTimer.sleep(3, 1)
        self.collect_mission_reward()

    @staticmethod
    def collect_mission_reward():
        image_path = "bot/screenshots/buttons/get_mission_reward_button.png"
        screen_region = (224, 799, 108, 31)
        click_location = (279, 810)

        click_if_image_found_with_variation(
            image_path, click_location, screen_region, 30, 15)
        CustomTimer.sleep(3, 1)

        # clica no icone do mapa para previnir cartas q uparam
        click_with_variation((282, 971), 20, 20)
        CustomTimer.sleep(3, 1)

    def try_again(self):
        image_path = "bot/screenshots/buttons/try_again_button.png"
        screen_region = (96, 967, 125, 33)

        if self.is_defeated():
            print("tentando novamente")
            while is_image_on_screen(image_path, screen_region):
                click_with_variation((158, 985), 50, 15)
                CustomTimer.sleep(3, 1)

            LoadingScreen.wait()
        else:
            GameRestarter.check_and_handle_error()

    @staticmethod
    def is_defeated():
        image_path = "bot/screenshots/buttons/try_again_button.png"
        screen_region = (96, 967, 125, 33)

        return is_image_on_screen(image_path, screen_region)

    @staticmethod
    def is_winner():
        image_path = "bot/screenshots/buttons/win_continue_button.png"
        screen_region = (204, 966, 152, 34)

        return is_image_on_screen(image_path, screen_region)

    # def collect_chest(self):
    #     cm = ClickManager()

    #     cm.click_with_variation((57, 971), 15, 15)
    #     time.sleep(1)

    # def have_chest(self):
    #     im = ImageIdentifier()
    #     image_path = "bot/screenshots/have_chest_reward.png"
    #     screen_region = (13, 394, 89, 90)

    #     return im.is_image_on_screen(image_path, screen_region)
