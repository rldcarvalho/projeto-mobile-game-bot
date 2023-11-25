from utilities.custom_timer import CustomTimer
from bot.loading_screen import LoadingScreen
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier


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
        cm = ClickManager()

        print("coletando XP")
        click_location = (284, 981)

        count = 0
        while count <= 6 and self.is_winner():
            cm.click_with_variation(click_location, 50, 15)
            print("retornando a tela de pvp")
            count += 1
            CustomTimer.sleep(5, 1)

        if count > 5:
            raise RuntimeError("Emulador travou")

        LoadingScreen.wait()
        CustomTimer.sleep(2, 1)

    def return_to_map(self):
        cm = ClickManager()
        click_location = (400, 986)

        while self.is_defeated():
            cm.click_with_variation(click_location, 50, 15)
            print("retornar ao mapa")
            CustomTimer.sleep(3, 1)

        LoadingScreen.wait()
        CustomTimer.sleep(3, 1)

    def winner_mission_continue(self):
        cm = ClickManager()

        click_location = (284, 981)

        while self.is_winner():
            cm.click_with_variation(click_location, 50, 15)
            print("retornando ao mapa para coletar recompensa")
            CustomTimer.sleep(3, 1)

        LoadingScreen.wait()

        CustomTimer.sleep(3, 1)
        self.collect_mission_reward()

    @staticmethod
    def collect_mission_reward():
        cm = ClickManager()

        image_path = "bot/screenshots/buttons/get_mission_reward_button.png"
        screen_region = (224, 799, 108, 31)
        click_location = (279, 810)

        cm.click_if_image_found_with_variation(
            image_path, click_location, screen_region, 30, 15)
        CustomTimer.sleep(3, 1)

        # clica no icone do mapa para previnir cartas q uparam
        cm.click_with_variation((282, 971), 20, 20)
        CustomTimer.sleep(3, 1)

    def try_again(self):
        im = ImageIdentifier()
        cm = ClickManager()
        image_path = "bot/screenshots/buttons/try_again_button.png"
        screen_region = (96, 967, 125, 33)

        if self.is_defeated():
            print("tentando novamente")
            while im.is_image_on_screen(image_path, screen_region):
                cm.click_with_variation((158, 985), 50, 15)
                CustomTimer.sleep(2, 0.5)

            LoadingScreen.wait()

    @staticmethod
    def is_defeated():
        im = ImageIdentifier()
        image_path = "bot/screenshots/buttons/try_again_button.png"
        screen_region = (96, 967, 125, 33)

        return im.is_image_on_screen(image_path, screen_region)

    @staticmethod
    def is_winner():
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
