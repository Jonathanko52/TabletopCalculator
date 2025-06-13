import json
import xmltodict
import re 

# This is the latest, working codex converter. Parses a Warhammer 40k BattleScribe '.cat' XML file into a structured JSON.
# python3 /Users/jonathanko/IndependentStudy/TabletopCalculator/xmlToJson.py


codexName = "Necrons"
route = ('./40k/' + codexName + '.cat')

"""
Converts a unit model XML node into into  dictionary containing the unit name and characteristics.

Parameters: input (dict): A dictionary representation of a model or unit element from the XML.

Returns: dict: A dictionary with 'unitName' and 'characteristics' keys.
"""

def parseUnitModelToDictionary(input):

    returnDict = {}
    returnDict["unitName"] = input["@name"]
    returnDict["characteristics"] = input["characteristics"]["characteristic"]
    return returnDict

    if input["@name"] == "Gretchin":
        print("Found Grots in parseunitmodeltodict")


"""

Recursively traverses the XML and finds entries of type 'model' or 'unit'. 
Extracts unit and weapon information and appends it to the output list.

Parameters: input (dict | list): The parsed XML input.

Returns: outputList (list): A list to append the found model/unit dictionaries to.

"""

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

"""

Recursively finds a 'Unit' type in the XML structure and adds them to the input dictionary.

Parameters:
    input (dict | list): The parsed XML node or list of nodes.
    inputDict (dict): A dictionary where the found unit data will be stored.

"""

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
"""

Recursively finds weapon entries of type 'Melee Weapons' or 'Ranged Weapons' in the XML and adds them to the input list.

Parameters:
        input (dict | list): The XML data structure.
        inputList (list): List to append found weapon entries to.

"""

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

"""

Converts a list of characteristic entries into a dictionary.

Parameters: inputDict (list): List of characteristic dictionaries.

Returns: dict: A dictionary mapping characteristic names to their values.

"""

def characteristicHelper(inputDict):
    returnDict = {}
    for keys in inputDict:
        returnDict[keys["@name"]] = keys["#text"]
    return returnDict

"""

Converts a list of weapon entries into a list of dictionaries with weapon stats.

Parameters: inputList (list): List of weapon dictionaries from XML.

Returns: list: A list of dictionaries, each representing a weapon.

"""

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

"""

Processes the  model data and converts it into dictionary.

Parameters: extractedData (list): List of model/unit dictionaries from `findModel`.

Returns: dict: Structured data including unit name, cost, characteristics, and weapons.

"""

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


        

# --- Execution Flow Starts Here ---

# Load and parse the XML

with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

# Extract models from XML

xmlIntoModels = []

findModel(data_dict, xmlIntoModels)

# Optional: Print extracted model names

for item in xmlIntoModels:
    print(item["Name"])

# Transform into structured data

finalDict = extractedInformationIntoDictionary(xmlIntoModels)

# Write to JSON file

f = open("./Data/" + codexName + ".json", "w")
f.write(json.dumps(finalDict))

f.close()
