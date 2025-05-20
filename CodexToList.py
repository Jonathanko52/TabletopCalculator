import xml.etree.ElementTree as ET
import json

codexName = "Imperium - Adeptus Custodes"


armyList = []

unit = {"name":"", "Characteristics":{}}


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



# Master function for finding the profile of the unit. Currently utilizies convert unit profile helper funciton, 
# which also uses findcharacteristic helper funciton. going to ahve to split those more
def findProfile(elementList):
    if elementList is None:
        return
    returnObj = {}
    for element in elementList:
        if(element.tag == "{http://www.battlescribe.net/schema/catalogueSchema}profiles"):
            for child in element:
                if(child.attrib["typeName"].lower() == "unit"):
                    returnObj["Name"] = child.attrib["name"]
                    convertUnitProfile(child,returnObj)
                    return returnObj          
                
        foundValue = findProfile(element)
        if foundValue is not None:
            return foundValue





#Funciton for recursively finding unit cost

def findCost(elementList, unitPointValue = "0"):
    if elementList is None:
        return None
    for element in elementList:
        if(element.tag == "{http://www.battlescribe.net/schema/catalogueSchema}costs"):
            for child in element:
                if(child.attrib["name"] == "pts" and child.attrib["value"] != "0"):
                    unitPointValue = child.attrib["value"]
                    return unitPointValue
                  
        foundValue = findCost(element, unitPointValue)
        if foundValue is not None:
            return foundValue


def findWeaponProfile(elementList):
    if elementList is None:
        return
    returnDictionary = {}
    
    for element in elementList:
        returnDictionary = {}
        if(element.tag == "{http://www.battlescribe.net/schema/catalogueSchema}characteristics" 
           and child.attrib["typeName"] == "Melee Weapons"):
            for child in element:
                returnDictionary[child.attrib["name"]] = child.text
        else:
           findCharacteristic(element)
    return returnDictionary



def convertUnitProfile(unitElement,unitObject):
    unitObject["Characteristics"]= findCharacteristic(unitElement)
    return unitObject

def convertWeaponProfile(unitElement,unitObject):
    unitObject["Weapons"]= findWeaponProfile(unitElement)
    return unitObject

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
    # print("COUNT", count)
    unitObject = findProfile(selectionEntry.findall("."))
    unitObject["Cost"] = findCost(selectionEntry.findall("."))
    unitObject["Weapon"] = findWeaponProfile(selectionEntry.findall("."))
    armyList.append(unitObject)

# Tests to see if army list is filled
for item in armyList:
    print()
    print("********************")
    print()
    # print("UNIT NAME: ", item["Name"])
    # print("UNIT COST: ", item["Cost"])
    # print("UNIT STATS: ", item["Characteristics"])
    print(item)



# Writes the file.
f = open("./Data/" + codexName + ".json", "a")
jsonString = json.dumps(armyList)
f.write(jsonString)
f.close()