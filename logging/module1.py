from logger import logConfig

log = logConfig(name=__name__, logLevel='INFO').get_logger()


log.info('this is moudle1')