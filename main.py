
from bot.battle import Battle
from bot.collect_rewards import CollectRewards
from bot.select_game_mode import SelectGameMode
from bot.start_emulator import StartEmulator

sgm = SelectGameMode()
battle = Battle()
cr = CollectRewards()

StartEmulator.ajust_window("LDPlayer")
sgm.mission()
battle.start()
battle.defend_tower()
cr.after_mission()
