def initialize_and_call(class_type, method_name, *args, **kwargs):
    instance = class_type(*args, **kwargs)
    method = getattr(instance, method_name)
    method()

def initialize_and_call_loop(class_type, method_name, *args, **kwargs):
    instance = class_type(*args, **kwargs)
    method = getattr(instance, method_name)
    method()