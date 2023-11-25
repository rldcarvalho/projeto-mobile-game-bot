from bot.battle import Battle
from bot.collect_rewards import CollectRewards
from bot.select_game_mode import SelectGameMode
from bot.start_emulator import StartEmulator
from utilities.custom_timer import CustomTimer


class GameBotManager:

    def __init__(self, emulator_name, game_mode):
        self.emulator_name = emulator_name
        self.game_mode = game_mode
        self.sgm = SelectGameMode()
        self.battle = Battle()
        self.cr = CollectRewards()

    def run(self):
        StartEmulator.ajust_window(self.emulator_name)

        game_modes = {
            'pvp': self.pvp,
            'pve': self.pve,
            'mission': self.mission,
        }

        # Verifica se o modo de jogo é válido
        if self.game_mode in game_modes:
            # Executa um loop while True contendo a função correspondente
            while True:
                game_modes[self.game_mode]()
        else:
            print(f'Modo de jogo inválido: {self.game_mode}')

    def pvp(self):
        self.sgm.pvp()
        CustomTimer.sleep(3)
        self.battle.defend_tower()
        self.cr.after_pvp()

    def pve(self):
        self.battle.start_pve()
        self.battle.dont_defend_tower()
        self.cr.try_again()

    def mission(self):
        self.sgm.mission()
        self.battle.start_pve()
        self.battle.defend_tower()
        self.cr.after_mission()