import pygetwindow as gw


class WindowHandler:
    def __init__(self, window_title):
        self.window_title = window_title
        self.window = None

    def focus_window(self):
        windows = gw.getWindowsWithTitle(self.window_title)
        if len(windows) > 0:
            self.window = windows[0]
            self.window.activate()
            print(f"Focando na janela {self.window_title}.")
        else:
            print(f"A janela {self.window_title} não foi encontrada.")

    def position_window(self, x, y):
        if self.window is None:
            windows = gw.getWindowsWithTitle(self.window_title)
            if len(windows) > 0:
                self.window = windows[0]

        if self.window:
            self.window.moveTo(x, y)
            print(f"Posicionada a janela {self.window_title} nas coordenadas ({x}, {y}).")
        else:
            print(f"A janela {self.window_title} não foi encontrada.")

    def resize_window(self, width, height):
        if self.window is None:
            windows = gw.getWindowsWithTitle(self.window_title)
            if len(windows) > 0:
                self.window = windows[0]

        if self.window:
            self.window.resizeTo(width, height)
            print(f"Redimensionada a janela {self.window_title} para o formato {width}x{height}.")
        else:
            print(f"A janela {self.window_title} não foi encontrada.")
