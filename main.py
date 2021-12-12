#!/usr/bin/env python3

import os
import sys

from logger.init_logger import init_logger
from core.connector import VKConnector
from core.reader import VKReader
from core.writer import CSVWriter
from core.saver import save_friends


def main():
    logger.debug('Starting app and get connection')
    session = VKConnector(os.getenv('TOKEN'))
    logger.debug('Get friends from VK DB')
    reader = VKReader(session.vk, os.getenv('USER_ID'))
    logger.debug('Open file for reading')
    writer = CSVWriter()
    logger.debug('Write info about friends to file')
    save_friends(reader, writer)
    logger.debug('The end')


if __name__ == '__main__':
    logger = init_logger()
    try:
        main()
    except Exception as err:
        print(err)
        logger.error(err)
        sys.exit()
