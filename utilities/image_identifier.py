import pyautogui
import pytesseract


def is_image_on_screen(image_path, region=None, confidence=0.8):

    """
    Verifica se uma imagem está na tela.

    Parameters:
        image_path (str): O caminho da imagem a ser procurada.
        region (tuple): A região específica na tela onde procurar a imagem.
        confidence (float): O nível de confiança para a correspondência.

    Returns:
        bool: True se a imagem for encontrada, False caso contrário.
    """

    screen = pyautogui.screenshot(region=region)
    location = pyautogui.locateOnScreen(image_path, confidence=confidence)
    return location is not None


def extract_text_in_image(region=None):
    """
    Extrai texto de uma imagem na tela.

    Parameters:
        region (tuple): A região específica na tela onde extrair o texto.
        lang (str): O idioma para a extração de texto.

    Returns:
        str: O texto extraído da imagem.
    """

    screen = pyautogui.screenshot(region=region)

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(screen, lang="por")

    return ' '.join(text.split())


def find_image_on_screen(image_path, region=None, confidence=0.8):
    """
    Encontra a posição de uma imagem na tela.

    Parameters:
        - image_path (str): O caminho para a imagem PNG.
        - region (tuple): A região da tela onde a imagem será procurada.
                          Deve ser uma tupla no formato (x, y, largura, altura).
                          Se for None, a tela inteira será considerada.
        - confidence (float): A confiança mínima para considerar uma correspondência.
                             Deve estar entre 0 e 1. Quanto maior, mais confiante.

    Returns:
        - tuple or None: As coordenadas (x, y) da imagem se encontrada, ou None se não encontrada.
    """
    try:
        # Encontra a posição da imagem na tela
        location = pyautogui.locateOnScreen(image_path, region=region, confidence=confidence)

        # Retorna o centro da imagem se encontrada
        if location:
            x_center = location.left + location.width / 2
            y_center = location.top + location.height / 2
            return int(x_center), int(y_center)
        else:
            return None
    except Exception as e:
        print(f"Erro ao encontrar imagem: {e}")
        return None
