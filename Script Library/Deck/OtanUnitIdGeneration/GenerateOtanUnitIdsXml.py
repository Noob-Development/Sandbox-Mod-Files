"""
This is a simple Python script to help write the OtanUnitIdChanges.txt text file to paste into OtanUnitIds.xml file that the installer will use.
It calls CreateUnitList to get a dictionary of which units to include, then writes the XML based on that.
It also uses unites.csv which you can get by using powercrystals' Table Exporter to print in-game names of units that have been removed.
"""

import CreateUnitList

total_included_string = ''
unit_list = CreateUnitList.get_unit_list()

for idx, building in enumerate(unit_list['included']['buildings']):
    total_included_string += f"""\
        <change property="OtanUnitIds" operation="append" type="map">
            <map>
                <key type="UInt32">{idx+1}</key>
                <value type="ObjectReference">
                    <reference table="TUniteDescriptor">
                        <matchconditions>
                            <matchcondition type="property" property="ClassNameForDebug">{building}</matchcondition>
                        </matchconditions>
                    </reference>
                </value>
            </map>
        </change>\n"""
        
for idx, unit in enumerate(unit_list['included']['units'], len(unit_list['included']['buildings'])):
    total_included_string += f"""\
            <change property="OtanUnitIds" operation="append" type="map">
                <map>
                    <key type="UInt32">{idx+1}</key>
                    <value type="ObjectReference">
                        <reference table="TUniteAuSolDescriptor">
                            <matchconditions>
                                <matchcondition type="property" property="ClassNameForDebug">{unit}</matchcondition>
                            </matchconditions>
                        </reference>
                    </value>
                </map>
            </change>\n"""

# =Writes OtanUnitIdChanges text file=
with open('OtanUnitIdChanges.txt', 'w+') as out:
    out.write(total_included_string)

total_excluded_string = ''

for building in unit_list['excluded']['buildings']:
    total_excluded_string += f'''
    <ndfpatch ndf="pc\\ndf\\patchable\\gfx\\everything.ndfbin" table="TUniteDescriptor" name="Remove {building}">
        <matchconditions>
			<matchcondition type="property" property="ClassNameForDebug">{building}</matchcondition>
		</matchconditions>
		<changes>
			<change operation="set" property="ShowInMenu" key="0" type="Boolean">False</change>
		</changes>
	</ndfpatch>'''
for unit in unit_list['excluded']['units']:
    total_excluded_string += f'''
    <ndfpatch ndf="pc\\ndf\\patchable\\gfx\\everything.ndfbin" table="TUniteAuSolDescriptor" name="Remove {unit}">
        <matchconditions>
			<matchcondition type="property" property="ClassNameForDebug">{unit}</matchcondition>
		</matchconditions>
		<changes>
			<change operation="set" property="ShowInMenu" key="0" type="Boolean">False</change>
		</changes>
	</ndfpatch>'''

# =Write HideUnits xml for logging purposes=
with open('HideUnits.xml', 'w+') as out:
    out.write(total_excluded_string)


# =Print excluded units list with wargame names=
names_dict = {}
with open('unites.csv', encoding='utf-8') as file:
    for line in file.readlines():
        hash, text = line.split(', ', 1)
        names_dict[hash] = text[:-1]
print('EXLCUDED UNITS:')
for unit in unit_list['excluded']['units']:
    tunite = unit_list['tunite']
    hash = tunite.loc[tunite['ClassNameForDebug'] == unit]['NameInMenuToken'].iloc[0]
    print(f'{unit}: {names_dict.get(hash, "NONE")}')