from bot.battle import Battle
from bot.collect_rewards import CollectRewards
from bot.select_game_mode import SelectGameMode
from bot.start_emulator import StartEmulator
from utilities.emulator_monitor import EmulatorMonitor
from utilities.image_identifier import ImageIdentifier

sgm = SelectGameMode()
battle = Battle()
cr = CollectRewards()

icon_path = "bot/screenshots/game_icon.png"
monitor_region = (11, 2, 33, 32)
emulator_monitor = EmulatorMonitor(icon_path, monitor_region)
emulator_monitor.start_monitoring()

StartEmulator.ajust_window("LDPlayer")
while not emulator_monitor.is_emulator_stuck():
    sgm.mission()
    battle.start()
    battle.defend_tower()
    cr.after_mission()

emulator_monitor.stop_monitoring()
