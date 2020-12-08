import os
import logging
import re
from datetime import *


log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
#file_handler=logging.FileHandler('logging_test_2.log')
#file_handler.setFormatter(formatter)
#logger.addHandler(file_handler)
streamhandler=logging.StreamHandler()
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)

def main():
    date_range = {'startDay': '1',
                  'startMonth': '1',
                  'startYear': '2012',
                  'endDay': '23',
                  'endMonth': '1',
                  'endYear': '2013'}

    startDate = date(int(date_range['startYear']), int(date_range['startMonth']),
                     int(date_range['startDay']))
    endDate = date(int(date_range['endYear']), int(date_range['endMonth']),
                   int(date_range['endDay']))

    myData=dataHandler(startDate, endDate)


class dataHandler:
    def __init__(self, startDate, endDate):
        self.startDate=startDate
        self.endDate=endDate
        for i in range(self.startDate.year, self.endDate.year+1):
            try:
                self.fileContent=self.getDataFromFile(self.openFileForYear(i))
            except Exception as err:
                log.error('Something wrong with data file for {} year: {}'.format(str(i), err))
            #[print(i) for i in self.fileContent]


    def openFileForYear(self, year):
        file_name=os.path.join('LPO_weatherdata-master',
                               'Environmental_Data_Deep_Moor_{}.txt'.format(str(year)))
        try:
            f=open(file_name)
        except Exception as err:
            log.error('The exception has occured: {}'.format(err))
            exit()
        return f


    def getDataFromFile(self, fileHandler):
        if fileHandler is None:
            return
        fileData=[]
        for i in fileHandler.readlines()[1:]:
            try:
                string = re.split('\s+', i)
                dateFromFile = date(*list(map(int, string[0].split('_'))))
                if self.startDate <= dateFromFile<= self.endDate:
                    fileData.append([dateFromFile,
                                     float(string[2]),
                                     float(string[3]),
                                     float(string[8])])
            except Exception as err:
                log.error('Incorrect data. {}'.format(err))
        return fileData






if __name__ == '__main__':
    main()