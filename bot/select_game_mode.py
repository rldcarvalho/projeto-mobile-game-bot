import os
import random
from bot.loading_screen import LoadingScreen
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier
import time


class SelectGameMode:
    def __init__(self):
        pass

    def mission(self):
        # clica no botão do mapa central se já não estiver
        self.center_map()

        # clica no botão de missão se já não estiver na tela
        self.go_to_mission_screen()
        time.sleep(1)

        # verifica se está na tela de missoes
        if not self.is_in_mission_screen():
            os._exit(0)

        # inicia uma missão aleatória
        self.select_mission()
        time.sleep(1)

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

    def pve(self):
        cm = ClickManager()
        im = ImageIdentifier()

        # vai para o mapa central
        self.center_map()

        # abre um mapa do mundo
        image_path = "bot/screenshots/buttons/map_button.png"
        search_region = (137, 101, 48, 41)
        if not im.is_image_on_screen(image_path, search_region):
            print("Abrindo um mapa no mundo")
            cm.click_with_variation((295, 454), 15, 20)
            time.sleep(2)

        # retrocece até chegar no primeiro mapa
        self.return_to_first_map()

        # clica para entrar na partida
        self.select_pve_map()

        # Tela de loading
        LoadingScreen.wait()

    def pve_loser(self, number):
        cm = ClickManager()
        im = ImageIdentifier()

        locations = {
            1: (307, 256),
            2: (307, 377),
            3: (307, 497),
            4: (307, 618),
            5: (307, 737),
        }

        click_location = locations.get(number, (0, 0))

        image_path = "bot/screenshots/screens/pve_screen.png"
        search_region = (137, 101, 48, 41)
        if im.is_image_on_screen(image_path, search_region):
            print(f"Abrindo o mapa numero {number}")
            cm.click_with_variation(click_location, 70, 15)
            time.sleep(1)

            print("iniciando a missão PVE")
            cm.click_with_variation((393, 919), 30, 15)
            time.sleep(1.5)

            # Tela de loading
            LoadingScreen.wait()
        else:
            print("página de missão não encontrada. Bot finalizado")
            os._exit(0)

    def center_map(self):
        cm = ClickManager()
        im = ImageIdentifier()

        # Variáveis para encontrar o botão de mapa
        image_path = "bot/screenshots/buttons/map_button.png"
        search_region = (898, 988, 72, 29)

        # Verifica se está na tela de mapa, se não, vai para ela
        if not im.is_image_on_screen(image_path, search_region):
            print("Indo para o mapa central")
            click_location = (282, 970)
            cm.click_with_variation(click_location, 2, 15)

            time.sleep(1)

    def go_to_mission_screen(self):
        cm = ClickManager()

        # Verifica se está na tela de missoes, se não, vai para ela
        if (not self.is_in_mission_screen()):
            click_location = (151, 863)
            cm.click_with_variation(click_location, 70, 15)
            print("Entrando na tela de missões")

            time.sleep(1)

    def is_in_mission_screen(self):
        im = ImageIdentifier()
        image_path = "bot/screenshots/screens/mission_screen.png"
        search_region = (239, 85, 75, 95)

        return im.is_image_on_screen(image_path, search_region)

    def select_mission(self):
        # Variáveis do clique e zonas dos botões de opções de missão
        mission_buttons = ((91, 814), (278, 814), (465, 814))
        search_regions = ((15, 685, 155, 94), (205, 685,
                          155, 94), (389, 685, 155, 94))

        # combina as missões e regiões em uma variável e mistura a ordem
        combined_missions = list(zip(mission_buttons, search_regions))
        random.shuffle(combined_missions)

        bad_mission = "Hogger"

        im = ImageIdentifier()
        cm = ClickManager()

        for (button, region) in combined_missions:
            print("iteracao")
            if not self.is_bad_mission(bad_mission, region):
                cm.click_with_variation(button, 50, 10)
                print("Missão selecionada")
                break

    def is_bad_mission(self, text, region):
        im = ImageIdentifier()
        extracted_text = im.extract_text_in_image(region)

        return text == extracted_text

    def return_to_first_map(self):
        cm = ClickManager()
        im = ImageIdentifier()
        image_path = "bot/screenshots/screens/pve_screen.png"
        search_region = (137, 101, 48, 41)

        if im.is_image_on_screen(image_path, search_region):
            image_button_path = "bot/screenshots/buttons/return_arrow_button.png"
            search_button_region = (48, 119, 54, 59)

            print("retornando ao primeiro mapa")
            while im.is_image_on_screen(image_button_path, search_button_region, 0.95):
                cm.normal_click((75, 149), 0.15)
                time.sleep(1)

            print("Primeiro mapa encontrado")
            time.sleep(1)

    def select_pve_map(self):
        cm = ClickManager()
        print("Clicando na missão PVE")
        cm.click_with_variation((297, 256), 70, 15)
        time.sleep(1)

        print("iniciando a missão PVE")
        cm.click_with_variation((393, 919), 30, 15)
        time.sleep(1.5)
