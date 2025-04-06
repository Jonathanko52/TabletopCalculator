import json
import xmltodict

codexName = "Imperium - Adeptus Custodes"
route = ('./40k/' + codexName + '.cat')


with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


# for key in data_dict["catalogue"]:
#     print("KEY", key)

# for key in data_dict["catalogue"]["sharedSelectionEntries"]:
#     print("KEY", key)

nested = False
for key in data_dict["catalogue"]["sharedSelectionEntries"]["selectionEntry"]:
    # Identifies a unit entry
    if(key["@type"] == "model" or key["@type"] == "unit"):
        print("_______________LINE BREAK_____________")
        print("NAME:",key["@name"])
        # Weapons Profiles
        if "selectionEntryGroups" in key:
            allEntryGroups = key["selectionEntryGroups"]['selectionEntryGroup']["selectionEntries"]["selectionEntry"]
            if "selectionEntries" in allEntryGroups:
                # print("CASE 2: Single profile Datasheets")
                # print(allEntryGroups["selectionEntries"]['selectionEntry'])
                for value in allEntryGroups["selectionEntries"]['selectionEntry']:
                    if type(value) is dict:
                            unitProfile = value["profiles"]["profile"]
                            characteristics = unitProfile["characteristics"]['characteristic']
                            print("NAME: ", unitProfile["@name"])
                            print("CHARACTERISTICS: ", characteristics[0])
                            print("CHARACTERISTICS: ", characteristics[1])
                            print("CHARACTERISTICS: ", characteristics[2])
                            print("CHARACTERISTICS: ", characteristics[3])
                            print("CHARACTERISTICS: ", characteristics[4])
                            print("CHARACTERISTICS: ", characteristics[5])
                            print("CHARACTERISTICS: ", characteristics[6])
                            print("TYPE: ", unitProfile["@typeName"])
                            
                            # print("Characteristics: ", value["characteristics"])
                        # for innerkeys in value:
                        #     print("ENTRY: ", innerkeys)
            # else:
            #     for value in allEntryGroups:
            #         if(type(value) is dict):
            #             # print("CASE 1: Multiple weapon loadout datasheets")
            #             print(value)




        # if "selectionEntries" in key:
            # allEntries = key["selectionEntries"]['selectionEntry']
            # print("_______________SELECTION ENTRIES_____________")
            # print("TYPE:",len(allEntries))
            # for value in  allEntries:
            #     print(value)

     


