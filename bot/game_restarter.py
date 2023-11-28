from bot.exceptions import RestartLoopException
from bot.loading_screen import LoadingScreen
from utilities.click_manager import click_with_variation, normal_click
from utilities.custom_timer import CustomTimer
from utilities.image_identifier import is_image_on_screen, find_image_on_screen
from utilities.screens_identifier import is_map_screen


class GameRestarter:

    @staticmethod
    def restart_generic_error():
        # Código para clicar no botão "OK" e reiniciar o jogo
        click_with_variation((289, 636), 40, 15)
        CustomTimer.sleep(13)

        LoadingScreen.wait()

        GameRestarter.check_in_match()

    @staticmethod
    def restart_in_loading():
        # reinicia o jogo no emulador MuMu
        print("Tentando reiniciar o Jogo")

        if is_game_open_in_mumu():
            # fecha o jogo
            image_path = "bot/screenshots/mumu_mini_game_icon.png"
            image_region = (54, 5, 217, 30)

            click_location = find_image_on_screen(image_path, image_region)

            normal_click(click_location)

            CustomTimer.sleep(1)

            # inicia o jogo

            image_path = "bot/screenshots/mumu_game_icon.png"
            image_region = (48, 192, 474, 761)

            click_location = find_image_on_screen(image_path, image_region)

            normal_click(click_location)

            CustomTimer.sleep(13)

            LoadingScreen.wait()

            GameRestarter.check_in_match()

    @staticmethod
    def check_and_handle_error():
        if is_error_screen():
            print("Erro detectado. Reiniciando o jogo.")
            GameRestarter.restart_generic_error()
            raise RestartLoopException

    @staticmethod
    def check_in_match():
        if not is_map_screen():
            CustomTimer.sleep(10)

            if is_pause_screen():
                print("Partida em andamento identificada")
                # clica no botão de pause
                click_with_variation((326, 83), 5, 5)

                CustomTimer.sleep(1, 1)

                print("Rendendo-se")
                # clica no botão render-se
                click_with_variation((471, 171), 30, 10)

                CustomTimer.sleep(2, 1)

                LoadingScreen.wait()



def is_error_screen():
    # Lógica para verificar se está na tela de erro
    image_path = "bot/screenshots/screens/error_screen.png"
    image_region = (242, 616, 84, 44)

    return is_image_on_screen(image_path, image_region)


def is_pause_screen():
    # Lógica para verificar se está na tela de pause
    image_path = "bot/screenshots/screens/pause_screen.png"
    image_region = (304, 60, 45, 45)

    return is_image_on_screen(image_path, image_region)


def is_game_open_in_mumu():
    image_path = "bot/screenshots/mumu_mini_game_icon.png"
    image_region = (54, 5, 217, 30)

    return is_image_on_screen(image_path, image_region)