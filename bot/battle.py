from bot.game_restarter import GameRestarter
from utilities.click_manager import click_with_variation
from utilities.custom_timer import CustomTimer
from utilities.image_identifier import is_image_on_screen


class Battle:
    def __init__(self):
        pass

    # Realiza o procedimento para iniciar partida PVE
    def start_pve(self):
        print("Inicio da partida")
        CustomTimer.sleep(2)

        # Variáveis para encontrar o botão de inciar a partida
        image_path = "bot/screenshots/buttons/start_button.png"
        search_region = (236, 806, 85, 61)

        count = 0
        while count < 3:
            if is_image_on_screen(image_path, search_region):
                click_location = (279, 839)
                click_with_variation(click_location, 50, 50)
                print("Batalha iniciada")
                CustomTimer.sleep(1, 0.5)
                break
            else:
                print("clique aleatorio na tela")
                click_with_variation((273, 1006), 100, 10)
                CustomTimer.sleep(3, 0.5)
                count += 1

        if count >= 3:
            GameRestarter.check_and_handle_error()

    # Seleciona minions aleatoriamente e os coloca perto da torre até a partida acabar
    def defend_tower(self):
        print("Começando a soltar os minions")

        count = 0
        while count < 12:
            if self.have_mana():
                self.play_minion()
                count = 0
                CustomTimer.sleep(1.5, 0.5)
            else:
                count += 1
                CustomTimer.sleep(1, 0.5)
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

    @staticmethod
    def have_mana():
        # Verifica se está com pelo menos 6 de mana
        mana_image_path = "bot/screenshots/six_mana.png"
        four_mana_region = (282, 989, 35, 29)
        six_mana_region = (167, 986, 229, 35)

        return is_image_on_screen(mana_image_path, six_mana_region, 0.90)

    # Seleciona um minion aleatório e o coloca em baixo da torre
    def play_minion(self):

        minion_region_center = (340, 870)
        base_tower = (278, 670)

        click_with_variation(minion_region_center, 200, 50)
        CustomTimer.sleep(0.5, 0.5)
        click_with_variation(base_tower, 100, 50)
        CustomTimer.sleep(0.5, 0.5)

#TODO ajustar para 6 mana