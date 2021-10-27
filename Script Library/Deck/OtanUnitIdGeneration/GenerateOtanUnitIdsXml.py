"""
This is a simple Python script to help write the OtanUnitIds xml file. It expects a text file with all the ClassNameForDebug strings for every unit, which you can get by using powercrystals' Table Exporter.
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

with open('HideUnits.xml', 'w+') as out:
    out.write(total_excluded_string)
