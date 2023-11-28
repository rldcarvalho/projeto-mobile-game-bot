from bot.game_restarter import GameRestarter
from utilities.click_manager import ClickManager
from utilities.custom_timer import CustomTimer
from utilities.image_identifier import is_image_on_screen


class Battle:
    def __init__(self):
        pass

    # Realiza o procedimento para iniciar partida PVE
    def start_pve(self):
        cm = ClickManager()

        print("Inicio da partida")
        CustomTimer.sleep(2)

        # Variáveis para encontrar o botão de inciar a partida
        image_path = "bot/screenshots/buttons/start_button.png"
        search_region = (236, 806, 85, 61)

        count = 0
        while count < 3:
            if is_image_on_screen(image_path, search_region):
                click_location = (279, 839)
                cm.click_with_variation(click_location, 50, 50)
                print("Batalha iniciada")
                CustomTimer.sleep(1, 0.5)
                break
            else:
                print("clique aleatorio na tela")
                cm.click_with_variation((273, 1006), 100, 10)
                CustomTimer.sleep(3, 0.5)
                count += 1

        if count >= 3:
            GameRestarter.check_and_handle_error()

    # Seleciona minions aleatoriamente e os coloca perto da torre até a partida acabar
    def defend_tower(self):
        print("Começando a soltar os minions")

        count = 0
        while count < 6:
            if self.have_mana():
                self.play_minion()
                count = 0
                CustomTimer.sleep(1, 0.5)
            else:
                count += 1
                CustomTimer.sleep(2, 0.5)
        print("Fim da batalha, parando de soltar minions")

        GameRestarter.check_and_handle_error()

    # Aguarda a partida acabar sem jogar minions
    def dont_defend_tower(self):
        count = 0
        while count < 5:
            if self.have_mana():
                count = 0
                CustomTimer.sleep(2)
            else:
                count += 1
                CustomTimer.sleep(2)
        print("Fim da batalha")

        GameRestarter.check_and_handle_error()

    # Verifica se está com pelo menos 4 de mana
    def have_mana(self):

        four_mana_path = "bot/screenshots/four_mana.png"
        four_mana_region = (160, 983, 157, 41)

        return is_image_on_screen(four_mana_path, four_mana_region)

    # Seleciona um minion aleatório e o coloca em baixo da torre
    def play_minion(self):
        cm = ClickManager()

        minion_region_center = (340, 870)
        base_tower = (278, 670)

        cm.click_with_variation(minion_region_center, 200, 50)
        CustomTimer.sleep(0.5, 0.5)
        cm.click_with_variation(base_tower, 100, 50)
        CustomTimer.sleep(0.5, 0.5)
