class AutoInitializeAndCall:
    def __init__(self, class_type, *args, **kwargs):
        self.instance = class_type(*args, **kwargs)

    def call_methods(self, *methods):
        for method in methods:
            method()

def replace_empty_lists(obj):
    if isinstance(obj, list) and not obj:
        return None
    elif isinstance(obj, dict):
        return {k: replace_empty_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_empty_lists(elem) for elem in obj]
    else:
        return obj