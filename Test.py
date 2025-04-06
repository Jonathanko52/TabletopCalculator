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
    if(key["@type"] == "model" or key["@type"] == "unit"):
        print("_______________LINE BREAK_____________")
        print("NAME:",key["@name"])
        if "selectionEntryGroups" in key:
            allEntryGroups = key["selectionEntryGroups"]['selectionEntryGroup']["selectionEntries"]["selectionEntry"]
            # if

            for value in allEntryGroups:
                print("VALUE TYPE:", type(value))
                if(type(value) is dict):
                    print("CASE 1:")
                    print(value)
                if(type(value) is str):
                    print("CASE 2:")
                    print(value)



        # if "selectionEntries" in key:
            # allEntries = key["selectionEntries"]['selectionEntry']
            # print("_______________SELECTION ENTRIES_____________")
            # print("TYPE:",len(allEntries))
            # for value in  allEntries:
            #     print(value)

     


