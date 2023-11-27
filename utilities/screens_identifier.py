from utilities.image_identifier import ImageIdentifier

ii = ImageIdentifier()


def is_map_screen():
    image_path = "bot/screenshots/buttons/map_button.png"
    search_region = (898, 988, 72, 29)

    return ii.is_image_on_screen(image_path, search_region)
