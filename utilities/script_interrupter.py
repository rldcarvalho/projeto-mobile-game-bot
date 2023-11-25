import os
import threading
import time
import keyboard


class ScriptInterrupter:
    def __init__(self):
        self.is_running = True
        self.key_thread = threading.Thread(target=self.check_key)

    def start(self):
        self.key_thread.start()

    def stop(self):
        print("Bot interrompido.")
        self.is_running = False

    def check_key(self):
        while self.is_running:
            if keyboard.is_pressed("p"):
                self.stop()
                os._exit(0)  # Encerra imediatamente o script
            time.sleep(1)

#TODO ajustar exception para interromper corretamente