import xml.etree.ElementTree as ET
import json

codexName = "Imperium - Space Marines"


armyList = []

unit = {"name":"", "characteristics":{}}


def findCharacteristic(elementList):
    if elementList is None:
        return
    returnDictionary = {}
    
    for element in elementList:
        returnDictionary = {}
        if(element.tag == "{http://www.battlescribe.net/schema/catalogueSchema}characteristics"):
            for child in element:
                returnDictionary[child.attrib["name"]] = child.text
        else:
           findCharacteristic(element)
    return returnDictionary

def findProfile(elementList):
    if elementList is None:
        return
    
    for element in elementList:
        if(element.tag == "{http://www.battlescribe.net/schema/catalogueSchema}profiles"):
            for child in element:
                if(child.attrib["typeName"].lower() == "unit"):
                    armyList.append(convertUnitProfile(child))             
        else:
           findProfile(element)



def convertUnitProfile(unitElement):
    convertedUnit = {"name":unitElement.attrib["name"], "characteristics":findCharacteristic(unitElement)}
    return convertedUnit

def convertWeaponProfile(weaponElement):
    convertedUnit = {"name":unitElement.attrib["name"], "characteristics":findCharacteristic(unitElement)}
    return convertedUnit


# Parse the XML file
tree = ET.parse('./40k/' + codexName + '.cat')
# tree = ET.parse('./40k/Imperium - White Scars.cat')
root = tree.getroot()

# # Find all book titles using namespace
count = 0
secondCount = 0
sharedSelectionEntries = root.find('./{http://www.battlescribe.net/schema/catalogueSchema}sharedSelectionEntries')


for selectionEntry in sharedSelectionEntries:
  if(selectionEntry.attrib["type"] == "unit" or selectionEntry.attrib["type"] == "model"):
    count += 1
    # print()
    # print("********************")
    # print()
    # print("UNIT NAME: ", selectionEntry.attrib["name"], selectionEntry.attrib["id"])
    # findCharacteristic(selectionEntry.findall("."))
    findProfile(selectionEntry.findall("."))


f = open("./Data/" + codexName + ".json", "a")
for unit in armyList:
    jsonString = json.dumps(unit)
    jsonString += "\n"
    f.write(jsonString)
f.close()




    #   <costs>
    #     <cost name="pts" typeId="51b2-306e-1021-d207" value="185"/>
    #   </costs>


