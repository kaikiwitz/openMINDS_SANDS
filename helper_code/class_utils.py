# class_utils.py

class AutoInitializeAndCall:
    def __init__(self, instance_or_class, *args, **kwargs):
        if isinstance(instance_or_class, type):
            self.instance = instance_or_class(*args, **kwargs)
        else:
            self.instance = instance_or_class

    def call_methods(self, *methods_and_args):
        for method_and_arg in methods_and_args:
            method, arg = method_and_arg
            method(arg)


def replace_empty_lists(obj):
    if isinstance(obj, list) and not obj:
        return None
    elif isinstance(obj, dict):
        return {k: replace_empty_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_empty_lists(elem) for elem in obj]
    else:
        return obj