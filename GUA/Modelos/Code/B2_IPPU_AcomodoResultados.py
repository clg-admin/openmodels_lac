# -*- coding: utf-8 -*-
"""
@author: Luis Victor-Gallardo // 2021
"""
from datetime import date
import sys
import pandas as pd
#import os
#from copy import deepcopy
#import csv
#import numpy as np

sys.path.insert(0, '../M0_IPPU/Executables')
import local_dataset_creator_0_IPPU


def archivo_resultados():
    'Define control parameters:'
    
    run_for_first_time = True
    
    if run_for_first_time == True:
        local_dataset_creator_0_IPPU.execute_local_dataset_creator_0_outputs()
        local_dataset_creator_0_IPPU.execute_local_dataset_creator_0_inputs()
    ############################################################################################################
    df_0_output = pd.read_csv('../M0_IPPU/Executables/output_dataset_0.csv', index_col=None, header=0)
    #
    li_output = [df_0_output]
    #
    df_output = pd.concat(li_output, axis=0, ignore_index=True)
    df_output.sort_values(by=['Future.ID','Fuel','Technology','Emission','Year'], inplace=True)
    ############################################################################################################
    df_0_input = pd.read_csv('../M0_IPPU/Executables/input_dataset_0.csv', index_col=None, header=0)
    #
    li_intput = [df_0_input]
    #
    df_input = pd.concat(li_intput, axis=0, ignore_index=True)
    df_input.sort_values(by=['Future.ID','Strategy.ID','Strategy','Fuel','Technology','Emission','Season','Year'], inplace=True)
    ############################################################################################################
    #
    dfa_list = [ df_output, df_input ] #, df_price, df_distribution ]
    #
    today = date.today()
    #
    df_output = dfa_list[0]
    df_output.to_csv ( '../Salidas/0_IPPU_GUA_Output.csv', index = None, header=True)
    df_output.to_csv ( '../Salidas/0_IPPU_GUA_Output_' + str( today ).replace( '-', '_' ) + '.csv', index = None, header=True)
    #
    df_input = dfa_list[1]
    df_input.to_csv ( '../Salidas/0_IPPU_GUA_Input.csv', index = None, header=True)
    df_input.to_csv ( '../Salidas/0_IPPU_GUA_Input_' + str( today ).replace( '-', '_' ) + '.csv', index = None, header=True)

def main():
    print("*****************************************")
    print("2. Creando resultados del sector PIUP ...")
    print("*****************************************")
    archivo_resultados()
    print("********************")
    print("El proceso finalizó.")
    print("********************")

if __name__== "__main__":
    main()