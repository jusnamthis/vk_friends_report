import logging


def init_logger():
    logger = logging.getLogger('get_friends.log')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('get_friends.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

