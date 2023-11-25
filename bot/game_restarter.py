from bot.exceptions import RestartLoopException
from bot.loading_screen import LoadingScreen
from utilities.click_manager import ClickManager
from utilities.custom_timer import CustomTimer
from utilities.image_identifier import ImageIdentifier


class GameRestarter:

    @staticmethod
    def restart_game():
        # Código para clicar no botão "OK" e reiniciar o jogo
        cm = ClickManager()

        cm.click_with_variation((289, 636), 40, 15)
        CustomTimer.sleep(13)

        LoadingScreen.wait()

        CustomTimer.sleep(10)

        if is_pause_screen():
            print("Partida em andamento identificada")
            # clica no botão de pause
            cm.click_with_variation((326, 83), 5, 5)

            CustomTimer.sleep(1, 1)

            print("Rendendo-se")
            # clica no botão render-se
            cm.click_with_variation((471, 171), 30, 10)

            CustomTimer.sleep(2, 1)

            LoadingScreen.wait()

    @staticmethod
    def check_and_handle_error():
        if is_error_screen():
            print("Erro detectado. Reiniciando o jogo.")
            GameRestarter.restart_game()
            raise RestartLoopException


def is_error_screen():
    # Lógica para verificar se está na tela de erro
    im = ImageIdentifier()
    image_path = "bot/screenshots/screens/error_screen.png"
    image_region = (242, 616, 84, 44)

    return im.is_image_on_screen(image_path, image_region)


def is_pause_screen():
    # Lógica para verificar se está na tela de pause
    im = ImageIdentifier()
    image_path = "bot/screenshots/screens/pause_screen.png"
    image_region = (304, 60, 45, 45)

    return im.is_image_on_screen(image_path, image_region)