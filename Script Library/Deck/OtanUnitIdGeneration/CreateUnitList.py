
"""
This is a simple Python script to help write the OtanUnitIds xml file. It expects a text file with all the ClassNameForDebug strings for every unit, which you can get by using powercrystals' Table Exporter.
"""

import GetHiddenUnits
import pandas as pd
import json

exclude_list = ["Unit_KHS_MI_8TV", "Unit_AH1S_Cobra", "Unit_AH_1F_JAP", "Unit_M42_Duster_JAP", "Unit_M35_Cargo", "Unit_MI_4AV", "Unit_UAZ_469A_vz59", "Unit_TO55_NK", "Unit_T34_85M1", "Unit_T34_85M" , "Unit_ASU_85M", "Unit_BM_24M", "Unit_BRDM_2_Strela_1M", "Unit_M110_JAP"] # Put units you want to remove here
exclude_list += GetHiddenUnits.get_hidden_units()
only_1_fob = True

def get_unit_list():
    final_data = {'num_included': 0, 'num_excluded': 0, 'excluded': {'buildings': [], 'units': []}, 'included': {'buildings': [], 'units': []}}
    df = pd.read_csv('TUniteDescriptor.csv')
    for unit in df['ClassNameForDebug']:
        if unit.startswith('Building_'):
            if only_1_fob:
                if len(final_data['included']['buildings']) == 0:
                    final_data['included']['buildings'] += [unit]
                else:
                    final_data['excluded']['buildings'] += [unit]
            else:
                final_data['included']['buildings'] += [unit]
            
    df = pd.read_csv('TUniteAuSolDescriptor.csv')
    for unit in df['ClassNameForDebug']:
        if unit not in exclude_list:
            final_data['included']['units'] += [unit]
        else:
            final_data['excluded']['units'] += [unit]

    final_data['num_excluded'] = len(final_data['excluded']['buildings']) + len(final_data['excluded']['units'])
    final_data['num_included'] = len(final_data['included']['buildings']) + len(final_data['included']['units'])
    return final_data

if __name__ == '__main__':
    print(json.dumps(get_unit_list(), indent=2))
