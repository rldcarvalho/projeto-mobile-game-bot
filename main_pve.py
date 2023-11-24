from bot.battle import Battle
from bot.collect_rewards import CollectRewards
from bot.select_game_mode import SelectGameMode
from bot.start_emulator import StartEmulator
from utilities.emulator_monitor import EmulatorMonitor
from utilities.image_identifier import ImageIdentifier
import time

sgm = SelectGameMode()
battle = Battle()
cr = CollectRewards()

# nome do emulador utilizado
emulator_name = "MuMuMain"

# Mapeamento de configurações para cada emulador
emulator_settings = {
    "LDPlayer": {
        "icon_path": "bot/screenshots/screens/game_icon_ldplayer.png",
        "monitor_region": (593, 231, 59, 51),
    },
    "BluestacksMain": {
        "icon_path": "bot/screenshots/screens/game_icon_bluestacks.png",
        "monitor_region": (410, 190, 52, 47),
    },
    "MuMuMain": {
        "icon_path": "bot/screenshots/screens/game_icon_bluestacks.png",
        "monitor_region": (410, 190, 52, 47),
    }
}

# Obtém as configurações do emulador atual
settings = emulator_settings.get(emulator_name, {})
icon_path = settings.get("icon_path", "")
monitor_region = settings.get("monitor_region", (0, 0, 0, 0))

# Ajustando a tela e iniciando o monitoramento do funcionamento do jogo
StartEmulator.ajust_window(emulator_name)
emulator_monitor = EmulatorMonitor(icon_path, monitor_region)
emulator_monitor.start_monitoring()

# Seleciona a missão da tela para fazer. Entre com a posição de 1 a 5:
sgm.pve_loser(3)

while not emulator_monitor.is_emulator_stuck():
    battle.start_pve()
    battle.dont_defend_tower()
    cr.try_again()

emulator_monitor.stop_monitoring()
