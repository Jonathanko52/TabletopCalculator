import json
import xmltodict
import re 

codexName = "Imperium - Adeptus Custodes"
route = ('./40k/' + codexName + '.cat')

def parseUnitModelToDictionary(input):
    returnDict = {}
    returnDict["unitName"] = input["@name"]
    returnDict["characteristics"] = input["characteristics"]["characteristic"]
    return returnDict


def findModel(input, outputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if keys == "@type":
                if(input["@type"]== "model"):
                    outputList.append(input)
            else:
                findModel(input[keys],outputList)
    if type(input) == list:
        for values in range(len(input)):
                findModel(input[values],outputList)



def findUnit(input, outputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if "@typeName" in keys:
                if(input["@typeName"]== "Unit"):
                    outputList.append(parseUnitModelToDictionary(input))
            else:
                findUnit(input[keys],outputList)
    if type(input) == list:
        for values in range(len(input)):
                findUnit(input[values],outputList)
        
def findWeapon(input, outputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if "@typeName" in keys:
                if(input["@typeName"]== "Melee Weapons" or input["@typeName"]== "Ranged Weapons"):
                    outputList.append(parseUnitModelToDictionary(input))
            else:
                findWeapon(input[keys],outputList)
    if type(input) == list:
        for values in range(len(input)):
                findWeapon(input[values],outputList)

with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


result1 = []

result2 = []

result3 = []

findModel(data_dict, result1)

findUnit(result1, result2)

findWeapon(result1, result3)

# print(result1[0])

for value in result1:
    print(value["@name"])
print("_________________________________")
for value in result2:
    print(value["unitName"])
print("_________________________________")
for value in result3:
    print(value)

print(len(result1))
print(len(result2))
print(len(result3))

