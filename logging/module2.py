from logger import logConfig


import module1
log = logConfig(name=__name__, logLevel='INFO').get_logger()

log.info('this is module2')
