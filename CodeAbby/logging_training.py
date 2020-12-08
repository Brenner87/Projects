 import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler('logging_test.log')
file_handler.setFormatter(formatter)

stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#logging.basicConfig(filename='logging_test.log',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    num_1 = 10
    num_2 = 0

    add_result=add(num_1, num_2)
    logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    sub_result=substract(num_1, num_2)
    logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
    mul_result=multiply(num_1, num_2)
    logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
    div_result=divide(num_1, num_2)
    logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


if __name__=='__main__':
    main()