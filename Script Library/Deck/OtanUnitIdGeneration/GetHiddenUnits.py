import xml.etree.ElementTree as ET

def get_hidden_units():
    tunite = ET.parse('TUniteAuSolDescriptor.xml').getroot()
    hidden_unit_list = []
    for unit in tunite:
        if unit.find('ShowInMenu')[0].text == 'False':
            hidden_unit_list += [unit.find('ClassNameForDebug').text]
    return hidden_unit_list

if __name__ == '__main__':
    print('\n'.join(get_hidden_units()))
