from bot.bot_manager import GameBotManager

# nome do emulador utilizado: "MuMuMain", "BluestacksMain" ou "LDPlayerMain"
emulator_name = "MuMuMain"

# nome do modo de jogo: "pvp", "mission" ou "pve"
game_mode = "pve"

game = GameBotManager(emulator_name, game_mode)

game.run()
