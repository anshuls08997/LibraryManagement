def handle_exceptions(func):
    """
    Decorator to catch unexpected exceptions in user flows,
    print user-friendly error messages, and prevent crashes.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print("An unexpected error occurred. Please try again or contact support.")
    return wrapper
