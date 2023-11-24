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

while not emulator_monitor.is_emulator_stuck():
    sgm.mission()
    battle.start_pve()
    battle.defend_tower()
    cr.after_mission()

emulator_monitor.stop_monitoring()
