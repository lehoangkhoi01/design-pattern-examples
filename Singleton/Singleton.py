class SingletonNew:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # Be careful with __init__ - it's called every time
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True