import random
from bot.loading_screen import LoadingScreen
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier
import time


class SelectGameMode:
    def __init__(self):
        pass

    def mission(self):
        cm = ClickManager()

        self.center_map()

        # clica no botão de missão
        click_location = (151, 863)
        cm.click_with_variation(click_location, 100, 15)
        print("Aberto menu de missões")

        time.sleep(1)

        # inicia uma missão aleatória
        self.select_mission()

        time.sleep(1)

        print("Inicio do loading")
        LoadingScreen.wait()

    def pvp(self):
        cm = ClickManager()

        self.center_map()

        # Variáveis para encontrar e clicar no botão de JxJ
        image_path = "bot/screenshots/buttons/pvp_button.png"
        search_region = (320, 817, 176, 82)
        click_location = (422, 863)

        # Verifica se a imagem está na tela e clica se encontrada na região especificado
        cm.click_if_image_found_with_variation(
            image_path, click_location, search_region, 50, 15)

        time.sleep(1)

        # clica no botão para procurar partida

    def center_map(self):
        cm = ClickManager()
        im = ImageIdentifier()

        # Variáveis para encontrar o botão de mapa
        image_path = "bot/screenshots/buttons/map_button.png"
        search_region = (898, 988, 72, 29)

        # Verifica se está na tela de mapa, se não, vai para ela
        if (not im.is_image_on_screen(image_path, search_region)):
            click_location = (282, 970)
            cm.click_with_variation(click_location, 2, 15)

            time.sleep(1)

    def select_mission(self):
        # Variáveis do clique e zonas dos botões de opções de missão
        mission_buttons = ((91, 814), (278, 814), (465, 814))
        search_regions = ((15, 685, 155, 94), (205, 685,
                          155, 94), (389, 685, 155, 94))

        # combina as missões e regiões em uma variável e mistura a ordem
        combined_missions = list(zip(mission_buttons, search_regions))
        random.shuffle(combined_missions)

        bad_mission = "bot/screenshots/minions/hogger_mission.png"

        im = ImageIdentifier()
        cm = ClickManager()

        for (button, region) in combined_missions:
            if not im.is_image_on_screen(bad_mission, region, confidence=1):
                cm.click_with_variation(button, 50, 10)
                print("Missão selecionada")
                break
