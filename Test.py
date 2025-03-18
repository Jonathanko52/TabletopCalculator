import json
import xmltodict

codexName = "Imperium - Adeptus Custodes"
route = ('./40k/' + codexName + '.cat')


with open(route) as xml_file:
    data_dict = xmltodict.parse(xml_file.read())