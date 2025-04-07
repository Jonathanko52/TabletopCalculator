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

with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


result = []


findModel(data_dict, result)

# print(result[48]["Unit"])
print(result[48]["Model"])

count = 0

# for value in result:
    # count += 1
    # print("_________________________________")
    # print(value["Name"], count)
    # print(value["Unit"])
    # print(value["Weapon"])


# "ARES GUNSHIP"
# {'Unit': 
#  {'@id': 'e3eb-3331-b91f-eeb5', 
#   '@name': 'Ares Gunship', 
#   '@hidden': 'false', '@typeId': 'c547-1836-d8a-ff4f', 
#   '@typeName': 'Unit', 
#   'characteristics': {'characteristic': 
#                       [{'@name': 'M', '@typeId': 'e703-ecb6-5ce7-aec1', '#text': '20"'},                     
#                         {'@name': 'T', '@typeId': 'd29d-cf75-fc2d-34a4', '#text': '12'}, 
#                         {'@name': 'SV', '@typeId': '450-a17e-9d5e-29da', '#text': '2+'}, 
#                         {'@name': 'W', '@typeId': '750a-a2ec-90d3-21fe', '#text': '22'}, 
#                         {'@name': 'LD', '@typeId': '58d2-b879-49c7-43bc', '#text': '6'}, 
#                         {'@name': 'OC', '@typeId': 'bef7-942a-1a23-59f8', '#text': '0'}]
#                     }
#     }
# }

# {'Weapon': 
#   {'@id': 'a94e-7676-65b3-b21e', 
#    '@name': 'Armoured hull', 
#    '@hidden': 'false', 
#    '@typeId': '8a40-4aaa-c780-9046', 
#    '@typeName': 'Melee Weapons', 
#    'characteristics': 
#       {'characteristic': 
#         [
#           {'@name': 'Range', '@typeId': '914c-b413-91e3-a132', '#text': 'Melee'}, 
#           {'@name': 'A', '@typeId': '2337-daa1-6682-b110', '#text': '9'}, 
#           {'@name': 'WS', '@typeId': '95d1-95f-45b4-11d6', '#text': '4+'}, 
#           {'@name': 'S', '@typeId': 'ab33-d393-96ce-ccba', '#text': '9'}, 
#           {'@name': 'AP', '@typeId': '41a0-1301-112a-e2f2', '#text': '0'}, 
#           {'@name': 'D', '@typeId': '3254-9fe6-d824-513e', '#text': '1'}, 
#           {'@name': 'Keywords', '@typeId': '893f-9000-ccf7-648e', '#text': '-'}
#         ]
#       }        
#     }
# }
