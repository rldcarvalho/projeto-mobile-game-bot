

class RestartLoopException(Exception):
    pass


class LoadingStuckException(Exception):
    def __init__(self, message):
        super().__init__(message)
