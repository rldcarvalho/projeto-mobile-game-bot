from utilities.window_handler import window_handler
import time


class StartEmulator:
    def ajust_window(name):
        """
        Ajusta a janela do emulador.

        Parameters:
        - name (str): Nome da janela do emulador.
        """
        wh_emulator = window_handler(name)

        # foca a janela
        wh_emulator.focus_window()

        time.sleep(0.5)

        # Posiciona a janela no canto superior esquerdo
        wh_emulator.position_window(0, 0)

        time.sleep(0.5)

        # Ajusta tamanho da tela
        wh_emulator.resize_window(602, 1030)
