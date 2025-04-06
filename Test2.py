import json
import xmltodict

codexName = "Imperium - Adeptus Custodes"
route = ('./40k/' + codexName + '.cat')

def parseUnitModelToDictionary(input):
    returnDict = {}
    returnDict["unitName"] = input["@name"]
    returnDict["characteristics"] = input["characteristics"]["characteristic"]
    return returnDict


def findUnitModel(input, outputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if "@typeName" in keys:
                if(input["@typeName"]== "Model" or input["@typeName"]== "Unit"):
                    # print(input)
                    outputList.append(parseUnitModelToDictionary(input))
            else:
                findUnitModel(input[keys],outputList)
    if type(input) == list:
        for values in range(len(input)):
                findUnitModel(input[values],outputList)
        


with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


result = []
findUnitModel(data_dict,result)
for value in result:
    print(value["unitName"])
    print(value["characteristics"])



