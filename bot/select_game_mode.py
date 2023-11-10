from utilities.click_manager import ClickManager
import time


class SelectGameMode:

    def pvp():
        # Defina o caminho da imagem que deseja procurar
        image_path = "bot/screenshots/pvp_button.png"

        # Defina a localização do clique se a imagem for encontrada
        click_location = (422, 863)

        # Defina a região de busca na tela (x, y, largura, altura)
        search_region = (320, 817, 176, 82)

        # Verifica se a imagem está na tela e clica se encontrada na região especificado
        cm = ClickManager()
        cm.click_if_image_found_with_variation(
            image_path, click_location, search_region, 50, 15)

        time.sleep(1)
