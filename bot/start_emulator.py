from utilities.window_handler import window_handler
from utilities.custom_timer import CustomTimer


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

        CustomTimer.sleep(0.5)

        # Posiciona a janela no canto superior esquerdo
        wh_emulator.position_window(0, 0)

        CustomTimer.sleep(0.5)

        # Ajusta tamanho da tela
        wh_emulator.resize_window(602, 1030)
