import json
import xmltodict
import re 

codexName = "Orks"
route = ('./40k/' + codexName + '.cat')

def parseUnitModelToDictionary(input):
    returnDict = {}
    returnDict["unitName"] = input["@name"]
    returnDict["characteristics"] = input["characteristics"]["characteristic"]
    return returnDict

    if input["@name"] == "Gretchin":
        print("Found Grots in parseunitmodeltodict")

def findModel(input, outputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if keys == "@type":
                if(input["@type"]== "model" or input["@type"]== "unit"):
                    if input["@name"] == "Gretchin":
                        print("Found Grots in findModel")
                    resultUnit = {}
                    resultWeapon = []
                    findUnit(input,resultUnit)
                    findWeapon(input,resultWeapon)
                    result = {
                        "Name": input["@name"],
                        "Unit": resultUnit,
                        "Weapon": resultWeapon,
                        "Model": input
                        }
                    outputList.append(result)
            else:
                findModel(input[keys],outputList)
    if type(input) == list:
        for values in range(len(input)):
                findModel(input[values],outputList)



def findUnit(input, inputDict):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if "@typeName" in keys:
                if(input["@typeName"]== "Unit"):
                    inputDict["Unit"] = input
            else:
                findUnit(input[keys], inputDict)
    if type(input) == list:
        for values in range(len(input)):
                findUnit(input[values], inputDict)
        
def findWeapon(input,inputList):
    if input is None:
      return
    
    if type(input) == dict:
        for keys in input:
            if "@typeName" in keys:
                if(input["@typeName"]== "Melee Weapons" or input["@typeName"]== "Ranged Weapons"):
                    inputList.append(input)
            else:
                findWeapon(input[keys], inputList)
    if type(input) == list:
        for values in range(len(input)):
                findWeapon(input[values], inputList)

def characteristicHelper(inputDict):
    returnDict = {}
    for keys in inputDict:
        returnDict[keys["@name"]] = keys["#text"]
    return returnDict

def weaponHelper(inputList):
    returnList = []
    returnDict = {}
    for item in inputList:
        returnDict["Name"] = item["@name"]
        characteristics = item["characteristics"]["characteristic"]
        for keys in characteristics:
            returnDict[keys["@name"]] = keys["#text"]
        returnList.append(returnDict)
    
    return returnList


def extractedInformationIntoDictionary(extractedData):
    returnDict = {}
    for model in extractedData:
        returnUnit = {}
        returnCharacteristic = []
        cost = 0
        test = model["Model"]

        # Retrieve Name of Model:
        returnUnit["Name"] = model["Name"]
        # Retrieve Cost of Model:
        if "profiles" in model["Model"] and "costs" in model["Model"]:
            if type(test["costs"]["cost"]) == list:
                cost = test["costs"]["cost"][0]["@value"]
            else:
                cost = test["costs"]["cost"]["@value"]
            returnUnit["Cost"] = cost
            if model["Name"] == "Gretchin":
                print("NAME", model["Name"])
                print("COST", cost)
        # Retrive Characteristics of Model:
            if not "Unit" in model["Unit"]:
                print(model["Name"])
                continue
            characteristics = model["Unit"]["Unit"]["characteristics"]["characteristic"]
            returnCharacteristic = characteristics
            
        if len(returnCharacteristic) > 0:
            returnUnit["characteristics"] = characteristicHelper(returnCharacteristic)
            returnUnit["Weapons"] = weaponHelper(model["Weapon"])
            returnDict[test["@name"]] = returnUnit
    return returnDict


        

with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


xmlIntoModels = []

findModel(data_dict, xmlIntoModels)

# for item in xmlIntoModels:
#     print(item["Name"])

finalDict = extractedInformationIntoDictionary(xmlIntoModels)

# f = open("./Data/" + codexName + ".json", "w")
# f.write(json.dumps(finalDict))

# f.close()
