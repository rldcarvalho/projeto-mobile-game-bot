from utilities.image_identifier import ImageIdentifier
import os
import time


class LoadingScreen:
    def wait():
        im = ImageIdentifier()

        image_path = "bot/screenshots/screens/loading_screen.png"
        search_region = (257, 307, 45, 45)

        count = 0
        while im.is_image_on_screen(image_path, search_region):
            count += 1
            if count >= 50:
                print("Emulador travou")
                os._exit(0)
            time.sleep(1)
