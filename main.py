from bot.bot_manager import GameBotManager

# nome do emulador utilizado
emulator_name = "MuMuMain"

# nome do modo de jogo
game_mode = "mission"

game = GameBotManager(emulator_name, game_mode)

game.run()
