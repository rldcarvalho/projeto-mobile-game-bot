import time
from utilities.click_manager import ClickManager
from utilities.image_identifier import ImageIdentifier


class Battle:
    def __init__(self):
        pass

    # Realiza o procedimento para iniciar partida PVE
    def start(self):
        cm = ClickManager()
        im = ImageIdentifier()

        print("Inicio da partida")
        time.sleep(2)

        # Variáveis para encontrar o botão de inciar a partida
        image_path = "bot/screenshots/buttons/start_button.png"
        search_region = (236, 806, 85, 61)

        count = 0
        while count < 3:
            if im.is_image_on_screen(image_path, search_region):
                click_location = (279, 839)
                cm.click_with_variation(click_location, 50, 50)
                print("Batalha iniciada")
                time.sleep(1)
                break
            else:
                print("clique aleatorio na tela")
                cm.click_with_variation((280, 650), 100, 100)
                time.sleep(6)
                count += 1

    # Seleciona minions aleatoriamente e os coloca perto da torre até a partida acabar
    def defend_tower(self):
        count = 0
        while count < 6:
            if (self.have_mana()):
                self.play_minion()
                count = 0
                time.sleep(1)
            else:
                count += 1
                time.sleep(2)
        print("Fim da batalha, parando de soltar minions")

    # Verifica se está com pelo menos 4 de mana
    def have_mana(self):
        id = ImageIdentifier()

        four_mana_path = "bot/screenshots/four_mana.png"
        four_mana_region = (160, 983, 157, 41)

        return id.is_image_on_screen(four_mana_path, four_mana_region)

    # Seleciona um minion aleatório e o coloca em baixo da torre
    def play_minion(self):
        cm = ClickManager()

        minion_region_center = (340, 870)
        base_tower = (278, 670)

        cm.click_with_variation(minion_region_center, 200, 50)
        time.sleep(0.5)
        cm.click_with_variation(base_tower, 100, 50)
        time.sleep(0.5)
