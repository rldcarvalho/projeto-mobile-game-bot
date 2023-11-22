from utilities.image_identifier import ImageIdentifier
import os
import time


class LoadingScreen:
    @staticmethod
    def wait():
        im = ImageIdentifier()

        image_path = "bot/screenshots/screens/loading_screen.png"
        search_region = (257, 307, 45, 45)

        print("Inicio do loading")
        count = 0
        while im.is_image_on_screen(image_path, search_region):
            count += 1
            if count >= 50:
                raise TimeoutError("Tempo limite de espera atingido. Emulador pode ter travado.")
            time.sleep(1)

    @staticmethod
    def searching_opponent():
        im = ImageIdentifier()

        image_path = "bot/screenshots/screens/searching_opponent_screen.png"
        search_region = (246, 262, 75, 73)

        print("Buscando oponente")
        count = 0
        while im.is_image_on_screen(image_path, search_region):
            count += 1
            if count >= 20:
                raise TimeoutError("Tempo limite de espera atingido. Emulador pode ter travado.")
            time.sleep(1)

        time.sleep(1)
