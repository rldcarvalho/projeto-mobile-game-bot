import pygetwindow as gw


class window_handler:
    def __init__(self, window_title):
        self.window_title = window_title
        self.window = None

    def focus_window(self):
        windows = gw.getWindowsWithTitle(self.window_title)
        if len(windows) > 0:
            self.window = windows[0]
            self.window.activate()
            print(f"Focused on {self.window_title} window.")
        else:
            print(f"{self.window_title} window not found.")

    def position_window(self, x, y):
        if self.window is None:
            windows = gw.getWindowsWithTitle(self.window_title)
            if len(windows) > 0:
                self.window = windows[0]

        if self.window:
            self.window.moveTo(x, y)
            print(f"Positioned {self.window_title} window at ({x}, {y}).")
        else:
            print(f"{self.window_title} window not found.")

    def resize_window(self, width, height):
        if self.window is None:
            windows = gw.getWindowsWithTitle(self.window_title)
            if len(windows) > 0:
                self.window = windows[0]

        if self.window:
            self.window.resizeTo(width, height)
            print(f"Resized {self.window_title} window to {width}x{height}.")
        else:
            print(f"{self.window_title} window not found.")
