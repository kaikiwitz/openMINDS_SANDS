class AutoInitializeAndCall:
    def __init__(self, class_type, *args, **kwargs):
        self.instance = class_type(*args, **kwargs)

    def call_methods(self, *methods):
        for method in methods:
            method()
