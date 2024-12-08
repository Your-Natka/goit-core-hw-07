def input_error(func):
    def wrapper(args, book):
        try:
            return func(args, book)
        except ValueError as e:
            return f"Error: {e}"
        except IndexError:
            return "Error: Missing arguments."
        except Exception as e:
            return f"Unexpected error: {e}"
    return wrapper