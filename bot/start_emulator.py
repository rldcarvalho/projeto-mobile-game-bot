from utilities.windowhandler import WindowHandler
from utilities.custom_timer import CustomTimer


class StartEmulator:
    def ajust_window(name):
        """
        Ajusta a janela do emulador.

        Parameters:
        - name (str): Nome da janela do emulador.
        """
        wh_emulator = WindowHandler(name)

        # foca a janela
        wh_emulator.focus_window()

        CustomTimer.sleep(0.5)

        # Posiciona a janela no canto superior esquerdo
        wh_emulator.position_window(0, 0)

        CustomTimer.sleep(0.5)

        # Ajusta tamanho da tela
        width = 602
        height = 1030

        if name == "MuMuMain":
            width = 567
            height = 1035

        wh_emulator.resize_window(width, height)
