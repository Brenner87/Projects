import os, logging, collections
from xml.etree import ElementTree


logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(message)s')
streamHandler=logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

def main():
    file_name='map.xml'
    full_file=os.path.abspath(os.path.join('Rooms_map', file_name))
    logger.info(full_file)
    dom=ElementTree.parse(full_file)
    root=dom.getroot()
#    for child in root:
#        print(child.tag)
#        print (child.attrib['name'])

    #new_room=ElementTree.SubElement(root, "room", attrib={"id":"8", "name":"bathroom"})
    #new_room_name=ElementTree.SubElement(new_room, "name")
    #new_room_name.text="Python_pents"
    #dom.write(full_file)
    level_map={}
    for child in root:
        level_map[child.attrib['name']]=child.attrib
        level_map[child.attrib['name']]['object'] = [item.attrib['name'] for item in child]
    #for some in root.iter('object'):
    #    print (some.attrib)
    print (level_map)


if __name__=='__main__':
    main()