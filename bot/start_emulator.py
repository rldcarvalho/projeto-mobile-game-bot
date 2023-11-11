from utilities.window_handler import window_handler
import time


class StartEmulator:
    def ajust_window(name):
        # inicia a classe de focar janela
        wh_ldp = window_handler(name)

        # foca a janela
        wh_ldp.focus_window()

        time.sleep(1)

        # Posiciona a janela no canto superior esquerdo
        wh_ldp.position_window(0, 0)

        time.sleep(1)

        # Ajusta tamanho da tela
        wh_ldp.resize_window(602, 1030)