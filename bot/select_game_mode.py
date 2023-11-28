import os
import random
from bot.loading_screen import LoadingScreen
from utilities.click_manager import click_with_variation, normal_click
from utilities.image_identifier import is_image_on_screen, extract_text_in_image
from utilities.custom_timer import CustomTimer


class SelectGameMode:
    def __init__(self):
        pass

    def mission(self):
        # clica no botão do mapa central se já não estiver
        self.center_map()

        # clica no botão de missão se já não estiver na tela
        self.go_to_mission_screen()
        CustomTimer.sleep(1, 0.5)

        # verifica se está na tela de missoes
        if not self.is_in_mission_screen():
            os._exit(0)

        # inicia uma missão aleatória
        self.select_mission()
        CustomTimer.sleep(1, 0.5)

        LoadingScreen.wait()

    def pvp(self):

        if not self.is_in_pvp_screen():
            self.center_map()
            self.go_to_pvp_screen()

        CustomTimer.sleep(1, 1)

        # clica no botão para procurar partida
        click_with_variation((410, 950), 50, 15)

        CustomTimer.sleep(1)

        LoadingScreen.searching_opponent()

        LoadingScreen.wait()

    def pve(self):
        # vai para o mapa central
        self.center_map()

        # abre um mapa do mundo
        image_path = "bot/screenshots/buttons/map_button.png"
        search_region = (137, 101, 48, 41)
        if not is_image_on_screen(image_path, search_region):
            print("Abrindo um mapa no mundo")
            click_with_variation((295, 454), 15, 20)
            CustomTimer.sleep(2, 1)

        # retrocece até chegar no primeiro mapa
        self.return_to_first_map()

        # clica para entrar na partida
        self.select_pve_map()

        # Tela de loading
        LoadingScreen.wait()

    @staticmethod
    def pve_loser(number):
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
        if is_image_on_screen(image_path, search_region):
            print(f"Abrindo o mapa numero {number}")
            click_with_variation(click_location, 70, 15)
            CustomTimer.sleep(1, 1)

            print("iniciando a missão PVE")
            click_with_variation((393, 919), 30, 15)
            CustomTimer.sleep(1.5)

            # Tela de loading
            LoadingScreen.wait()

    @staticmethod
    def center_map():
        # Variáveis para encontrar o botão de mapa
        image_path = "bot/screenshots/buttons/map_button.png"
        search_region = (898, 988, 72, 29)

        # Verifica se está na tela de mapa, se não, vai para ela
        if not is_image_on_screen(image_path, search_region):
            print("Indo para o mapa central")
            click_location = (282, 970)
            click_with_variation(click_location, 2, 15)

            CustomTimer.sleep(1, 2)

    def go_to_mission_screen(self):
        # Verifica se está na tela de missoes, se não, vai para ela
        if not self.is_in_mission_screen():
            click_location = (151, 863)
            click_with_variation(click_location, 70, 15)
            print("Entrando na tela de missões")

            CustomTimer.sleep(1, 2)

    @staticmethod
    def is_in_mission_screen():
        image_path = "bot/screenshots/screens/mission_screen.png"
        search_region = (239, 85, 75, 95)

        return is_image_on_screen(image_path, search_region)

    def go_to_pvp_screen(self):
        # Verifica se está na tela de pvp, se não, vai para ela
        if not self.is_in_pvp_screen():
            click_location = (422, 863)
            click_with_variation(click_location, 50, 15)
            print("Entrando na tela de pvp")

            CustomTimer.sleep(1, 2)

    @staticmethod
    def is_in_pvp_screen():
        image_path = "bot/screenshots/screens/pvp_screen.png"
        search_region = (254, 119, 57, 58)

        return is_image_on_screen(image_path, search_region)

    def select_mission(self):
        # Variáveis do clique e zonas dos botões de opções de missão
        mission_buttons = ((91, 814), (278, 814), (465, 814))
        search_regions = ((15, 685, 155, 94), (205, 685,
                          155, 94), (389, 685, 155, 94))

        # combina as missões e regiões em uma variável e mistura a ordem
        combined_missions = list(zip(mission_buttons, search_regions))
        random.shuffle(combined_missions)

        bad_mission = "Hogger"

        for (button, region) in combined_missions:
            print("iteracao")
            if not self.is_bad_mission(bad_mission, region):
                click_with_variation(button, 50, 10)
                print("Missão selecionada")
                break

    @staticmethod
    def is_bad_mission(text, region):
        extracted_text = extract_text_in_image(region)

        return text == extracted_text

    @staticmethod
    def return_to_first_map():
        image_path = "bot/screenshots/screens/pve_screen.png"
        search_region = (137, 101, 48, 41)

        if is_image_on_screen(image_path, search_region):
            image_button_path = "bot/screenshots/buttons/return_arrow_button.png"
            search_button_region = (48, 119, 54, 59)

            print("retornando ao primeiro mapa")
            while is_image_on_screen(image_button_path, search_button_region, 0.95):
                normal_click((75, 149), 0.15)
                CustomTimer.sleep(1, 1)

            print("Primeiro mapa encontrado")
            CustomTimer.sleep(1, 1)

    @staticmethod
    def select_pve_map():
        print("Clicando na missão PVE")
        click_with_variation((297, 256), 70, 15)
        CustomTimer.sleep(1, 1)

        print("iniciando a missão PVE")
        click_with_variation((393, 919), 30, 15)
        CustomTimer.sleep(1, 2)
