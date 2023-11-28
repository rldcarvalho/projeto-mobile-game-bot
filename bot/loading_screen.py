from bot.exceptions import LoadingStuckException
from utilities.image_identifier import is_image_on_screen
from utilities.custom_timer import CustomTimer
from utilities.screens_identifier import is_loading_screen, is_searching_opponent_screen


class LoadingScreen:
    @staticmethod
    def wait():
        print("Aguardando o loading")
        count = 0
        while is_loading_screen():
            count += 1
            if count >= 50:
                raise LoadingStuckException("Tempo limite de espera atingido. Emulador pode ter travado.")
            CustomTimer.sleep(1)

        CustomTimer.sleep(1, 1)

    @staticmethod
    def searching_opponent():
        print("Buscando oponente")
        count = 0
        while is_searching_opponent_screen():
            count += 1
            if count >= 20:
                raise LoadingStuckException("Tempo limite de espera atingido. Emulador pode ter travado.")
            CustomTimer.sleep(1)

        CustomTimer.sleep(1)
