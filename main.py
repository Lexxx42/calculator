from logg import logging
import controller


# logging.warning("Main menu, wrong item selected.")
def main():
    logging.info('Start program.')
    controller.session()
    logging.info('Session finish')


if __name__ == '__main__':
    main()
