# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os, os.path
import sys




if __name__ == '__main__':
    ## Part 1 Load the sheet InputAR from the B1_Scenario_Config.xlsx file
    base_configuration_InputAR = pd.read_excel( '../M3_Energy/B1_Scenario_Config.xlsx', sheet_name='InputAR')

    # Load the fuel and technologies to a list
    fuel_list = base_configuration_InputAR['Fuel'].unique().tolist()
    tech_list = base_configuration_InputAR['Tech'].tolist()

    ## Part 2 test modify csv file directly
    current_path = os.getcwd()
    #model_file = current_path + "../M3_Energy/A2_Output_Params/NDP/InputActivityRatio.csv"
    model_file = "../M3_Energy/A2_Output_Params/NDP/InputActivityRatio.csv"

    #Load pandas
    df_inputactivityratio = pd.read_csv(model_file)

    # Filter to work only with the fuel_list and tech_list of the entire sheet
    df_inputactivityratio_filtered = df_inputactivityratio[
        (df_inputactivityratio['FUEL'].isin(fuel_list)) &
        (df_inputactivityratio['TECHNOLOGY'].isin(tech_list))][['TECHNOLOGY', 'FUEL', 'YEAR', 'Value']]


    for fuel in fuel_list:
        for counter, tech in enumerate(tech_list):
            new_values = base_configuration_InputAR[(base_configuration_InputAR['Fuel'] == fuel) & (base_configuration_InputAR['Tech'] == tech)]
            new_values = new_values.loc[:,2018:2050].values.flatten().tolist()
            new_values = [round(e, 4) for e in new_values]

            # Replace the values in the df_inputactivityratio_filtered
            df_inputactivityratio_filtered.loc[(df_inputactivityratio_filtered['FUEL'] == fuel) & (df_inputactivityratio_filtered['TECHNOLOGY'] == tech), 'Value'] = new_values


    # Replace the mew values in the df_inputactivityratio_filtered to the original df_inputactivityratio
    df_inputactivityratio.loc[df_inputactivityratio['FUEL'].isin(fuel_list) & df_inputactivityratio['TECHNOLOGY'].isin(tech_list), 'Value'] = df_inputactivityratio_filtered['Value']

    # Save the modified df_inputactivityratio_filtered to a new csv file in A2 and B2 A2_Output_Params directories
    df_inputactivityratio.to_csv('../M3_Energy/A2_Output_Params/NDP/InputActivityRatio.csv', index=False)
    df_inputactivityratio.to_csv('../M3_Energy/B1_Output_Params/NDP/InputActivityRatio.csv', index=False)
    #
    print('Done, InputActivityRatio.csv files has been updated')
