import pyautogui
import threading
import time

from utilities.image_identifier import ImageIdentifier


class EmulatorMonitor:
    def __init__(self, icon_path, region):
        self.icon_path = icon_path
        self.region = region
        self.stopped = False
        self.monitor_thread = None

    def is_emulator_stuck(self):
        im = ImageIdentifier()
        return im.is_image_on_screen(self.icon_path, self.region)

    def monitor_emulator(self):
        print("o emulador está sendo monitorado")
        while not self.stopped:
            if self.is_emulator_stuck():
                print("Emulador travou. Parando o bot.")
                # implementar código de reiniciar o jogo
                break

            print(".")
            time.sleep(3)  # Ajuste de intervalo do scan da imagem

    def start_monitoring(self):
        self.stopped = False
        self.monitor_thread = threading.Thread(target=self.monitor_emulator)
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.stopped = True
        self.monitor_thread.join()
