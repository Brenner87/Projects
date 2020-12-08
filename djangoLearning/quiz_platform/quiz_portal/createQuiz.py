import logging
from xml.etree import ElementTree

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(message)s')
streamhandler=logging.StreamHandler()
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)


def main():
    test_file='my_first_test.xml'
    xmlHandler=Constructor(test_file)
    print(xmlHandler.quiz)
    answers=xmlHandler.displayQuiz()
    print(xmlHandler.validateQuiz(answers))





class Constructor:
    def __init__(self, xmlFile):
        self.xmlFile=xmlFile
        tree=self.openXML(self.xmlFile)
        self.quiz=self.createQuize(tree)


    def openXML(self, xmlFile):
        try:
            tree = ElementTree.parse(xmlFile)
        except Exception as err:
            log.error('Was not able to parce {}: {}'.format(xmlFile, err))
            exit()
        return tree

    def createQuize(self,tree):
        quiz={}
        try:
            root=tree.getroot()
            quiz['quiz'] =root.text.strip()
            quiz['questions']=[self.buildQuestion(i) for i in root]
        except Exception as err:
            log.fatal('Something wrong with {}: {}'.format(self.xmlFile,err))
        return quiz

    def buildQuestion(self, question):
        my_question = [i.text for i in question]
        result = [int(i.attrib['id']) for i in question if 'correct' in i.attrib.keys()]
        my_question.insert(0, question.text.strip())
        my_question.append(result)
        return my_question

    def displayQuiz(self):
        print(self.quiz['quiz'])
        print()
        print()
        answers=[]
        for question in self.quiz['questions']:
            print('{} :'.format(question[0]))
            print('='*20)
            for option in question[1:-1]:
                print('{}. {}'.format(question.index(option), option))
            answers.append(list(map(int, input('Your answer, separated with space:').split(' '))))
            print('='*20)
            print()
        return answers



    def validateQuiz(self, inputData):
        answers=[i[-1] for i in self.quiz['questions']]
        if len(answers) !=len(inputData):
            log.error('Questions number do not match answers number')
            exit()
        totalError=[]
        for i in range(len(inputData)):
            if answers[i]!=inputData[i]:
                print('{}: правильный ответ - {}'.format(self.quiz['questions'][i][0], ','.join(map(str, answers[i]))))
                totalError.append(i)
        return 'Your score: {}/{}'.format(str(len(inputData)-len(totalError)), str(len(inputData)))








if __name__=='__main__':
    main()