import logging
from xml.etree import ElementTree

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(message)s')
streamhandler=logging.StreamHandler()
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)

def main():
    game=map_jorney('map.xml', 'goal')
    game.createMap()
    game.checkObjectsExistance()
    log.debug('game map:')
    [log.debug(item) for item in game.level_map]
    log.info('Objects to find: {}'.format(game.goals))
    log.debug('Position at the start of the game: {}'.format(game.Pos))
    log.debug('result at start: {}'.format(game.output))
    game.move()
    log.debug('Here is the result: {}'.format(game.output))
    log.debug('{} objects found from {}'.format(game.found, len(game.goals)))
    log.debug('level_map:')
    [log.debug(item) for item in game.level_map]
    log.info('Result:')
    [log.info(i) for i in game.output]




class map_jorney(object):
    def __init__(self, mapFile, goalFile):
        try:
            self.tree= ElementTree.parse(mapFile)
        except FileExistsError as file_err:
            log.error("File doesn't exist, please try once more!")
            exit()
        except Exception as err:
            log.error("Not able to parse your file. Please try once more " + err)
            exit()
        try:
            file_handler=open(goalFile, 'r')
            goal=[i.rstrip() for i in open(goalFile,'r')]
        except Exception as e:
            log.error("can't reach your {} file. Please try once more.".format(e))
            exit()
        try:
            self.startPos = goal[0]
            self.goals = goal[1:]
        except Exception as str_err:
            log.error ("{} Please try once more".format(str_err))
            exit()
        self.level_map = []
        self.output=[]
        self.found=0

    def createMap(self):
        for child in self.tree.getroot():
            self.level_map.append(child.attrib)
            self.level_map[-1]['object'] = [item.attrib['name'] for item in child ]
        [item.update({'visited':False}) for item in self.level_map]
        self.Pos=self.startPos

    def checkObjectsExistance(self):
        objects=[i for room in self.level_map for i in room['object']]
        for obj in self.goals:
            if obj not in objects:
                self.output.append('Object {} is missing on map'.format(obj))
                self.goals.remove(obj)


    def discoverRoom(self,item):
        item['visited']=True
        for obj in item['object']:
            if len(list(filter(lambda x: obj in x, self.output)))<1:
                log.debug('{} found in {}'.format(obj,item['name']))
                if obj in self.goals:
                    self.found += 1
                    self.output.append('{} ({}/{})'.format(obj, self.found, len(self.goals)))
                else: self.output.append(obj)
                log.debug('{} found from {}'.format(self.found,len(self.goals)))


    def move(self):
        worldSides=['west', 'east', 'north', 'south']
        if self.found == len(self.goals):
            self.output.append("Objective accomplished.")
            log.info("Objective accomplished. Exiting...")
            return
        for item in self.level_map:
            if item['name'] == self.Pos:
                log.debug('new iteration in: {}:{}'.format(item['name'], item['id']))
                self.discoverRoom(item)
                currentSides={key:item[key] for key in item  if key in worldSides}
                visitedCounter=0
                for side in currentSides:
                    nextSides={key:self.level_map[int(currentSides[side])-1][key]
                                for key in self.level_map[int(currentSides[side])-1] if key in worldSides}
                    roomObj=self.level_map[int(currentSides[side])-1]
                    log.debug('Sides in the next room: {}. Visited:{}. Number of sides: {}'.format(nextSides,
                                            roomObj['visited'], len(nextSides)))
                    if len(currentSides) < 2:
                        roomObj['visited']=False
                        for i in nextSides:
                            if roomObj[i] == item['id']:
                                del roomObj[i]
                    if roomObj['visited'] is False:
                        log.debug('moving {}'.format(side))
                        self.output.append(side)
                        log.debug('{} direction to {}(id:{}) from {}(id:{})'
                            .format(side, roomObj['name'],
                            self.level_map[int(item[side])-1]['id'], item['name'], item['id']))
                        self.Pos=self.level_map[int(item[side])-1]['name']
                    else: visitedCounter+=1
                if visitedCounter==len(currentSides) and self.found!=len(self.goals):
                    self.output.append("Not able to reach other objects")
                    log.error("There is no way to next rooms")
                    return
                self.move()
                break



if __name__=='__main__':
    main()