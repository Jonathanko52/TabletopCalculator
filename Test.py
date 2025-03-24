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

count = 0
for key in data_dict["catalogue"]["sharedSelectionEntries"]["selectionEntry"]:
    count += 1
    print("_______________LINE BREAK_____________")
    print(key)
print(count)