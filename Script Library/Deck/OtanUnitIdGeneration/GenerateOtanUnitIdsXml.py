"""
This is a simple Python script to help write the OtanUnitIds xml file. It expects a text file with all the ClassNameForDebug strings for every unit, which you can get by using powercrystals' Table Exporter.
"""

import CreateUnitList

total_string = ''
unit_list = CreateUnitList.get_unit_list()

for idx, building in enumerate(unit_list['buildings']):
    total_string += f"""\
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
        
for idx, unit in enumerate(unit_list['units'], len(unit_list['buildings'])):
    total_string += f"""\
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
    out.write(total_string)
