def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            return str(e)
    return wrapper