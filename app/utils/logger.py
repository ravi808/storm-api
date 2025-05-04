import logging

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up and returns a logger instance with the specified name.
    Ensures that multiple handlers are not added to avoid duplicate logs.

    Args:
        name (str): Name of the logger (typically __name__ from the calling module).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)  # Create or retrieve a logger with the given name

    if not logger.handlers:
        # Prevent adding multiple handlers if already set
        handler = logging.StreamHandler()  # Output logs to the console
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)   
        logger.addHandler(handler)       

    logger.setLevel(logging.INFO)
    return logger
