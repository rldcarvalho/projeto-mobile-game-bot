from utilities.image_identifier import is_image_on_screen


def is_map_screen():
    image_path = "bot/screenshots/buttons/map_button.png"
    search_region = (898, 988, 72, 29)

    return is_image_on_screen(image_path, search_region)


def is_defeated_screen():
    image_path = "bot/screenshots/buttons/try_again_button.png"
    screen_region = (96, 967, 125, 33)

    return is_image_on_screen(image_path, screen_region)


def is_winner_screen():
    image_path = "bot/screenshots/buttons/win_continue_button.png"
    screen_region = (204, 966, 152, 34)

    return is_image_on_screen(image_path, screen_region)


def is_error_screen():
    # Lógica para verificar se está na tela de erro
    image_path = "bot/screenshots/screens/error_screen.png"
    image_region = (92, 508, 404, 310)

    return is_image_on_screen(image_path, image_region)


def is_pause_screen():
    # Lógica para verificar se está na tela de pause
    image_path = "bot/screenshots/screens/pause_screen.png"
    image_region = (304, 60, 45, 45)

    return is_image_on_screen(image_path, image_region)


def is_game_open_in_mumu():
    image_path = "bot/screenshots/mumu_mini_game_icon.png"
    image_region = (54, 5, 217, 30)

    return is_image_on_screen(image_path, image_region)


def is_loading_screen():
    image_path = "bot/screenshots/screens/loading_screen.png"
    image_region = (257, 307, 45, 45)

    return is_image_on_screen(image_path, image_region)


def is_searching_opponent_screen():
    image_path = "bot/screenshots/screens/searching_opponent_screen.png"
    image_region = (246, 262, 75, 73)

    return is_image_on_screen(image_path, image_region)


def is_pve_screen():
    image_path = "bot/screenshots/screens/pve_screen.png"
    image_region = (137, 101, 48, 41)

    return is_image_on_screen(image_path, image_region)


def is_mission_screen():
    image_path = "bot/screenshots/screens/mission_screen.png"
    search_region = (239, 85, 75, 95)

    return is_image_on_screen(image_path, search_region)


def is_pvp_screen():
    image_path = "bot/screenshots/screens/pvp_screen.png"
    search_region = (254, 119, 57, 58)

    return is_image_on_screen(image_path, search_region)
