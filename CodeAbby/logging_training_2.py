import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('logging_test_2.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#logging.basicConfig(filename='logging_test_2.log',level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

def main():
    emp_1=Employee('John', 'Smiht')
    emp_2=Employee('Corey', 'Schafer')
    emp_3=Employee('Panas', 'Didko')



class Employee:

    def __init__(self, first, last):
        self.first=first
        self.last=last
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


main()
