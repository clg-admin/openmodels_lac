# -*- coding: utf-8 -*-
import pandas as pd
#import os
import numpy as np
#import math
import ast

# 'Funcion para leer los archivos dentro de un directorio'
# def ListaArchivos( Nombre_carpeta ):
#     listaArchivos = os.listdir( Nombre_carpeta )
#     return listaArchivos

'Funcion para hacer una copia de una lista'
def CopiaLista(lista):
    copia=list()
    for i in lista:
        copia.append(i)
    return copia

'Funcion para hacer una lista de ceros de cierto tamano'
def ListaCeros(tam):
    copia=list()
    for i in range(tam):
        copia.append(0)
    return copia

'Funcion para hacer un idice para ordenar los Dataframes'
def IndiceOrdenTabla(lista, nuevo_elemento, indice):
    copia=CopiaLista(lista)
    copia.insert(indice,nuevo_elemento)
    return copia

'Funcion para eliminar repetidos de una lista'
def EliminarRepetidos(lista):
    salida=list()
    for i in range(len(lista)):
        if lista[i] not in salida:
            salida.append(lista[i])
    return salida

'''Funcion para eliminar nans de una lista'''
def EliminarNoStr(lista):
    salida=list()
    for i in range(len(lista)):
        if type(lista[i])==str:
            salida.append(lista[i])
    return salida

def join_results():
    'Lista con los archivos de salida sectoriales a unificar'
    lista_archivos_salida_sectoriales=["0_IPPU_GUA_Output.csv","1_Waste_GUA_Output.csv","2_AFOLU_GUA_Output.csv","3_Energy_GUA_Output.csv"]
    
    'Lista con los anios para filtrar de ser necesario si el archivo es muy pesado'
    filtro_anios=[2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2030,2035,2040,2045,2050]
    
    'En teoria, solo hay 1 archivo de salida por sector en donde están todos los escenarios y estarán todos los futuros'
    ###########################################################################################################
    ### ENERGY
    ###########################################################################################################
    df_Energy_output = pd.read_csv("../Salidas/"+lista_archivos_salida_sectoriales[3], index_col=None, header=0, low_memory=False)
    # MUY IMPORTANTE ESTA LISTA AUXILIAR PARA NO REPETIR UN NOMBRE DE COLUMNA EN UN DATAFRAME
    lista_aux=list(df_Energy_output.columns)
    'Energia tiene mas comulnas que el resto de sectores por lo que vamos a completar el resto con la misma cantidad de columnas'
    'Se agrega la columna de sector al Dataframe de Energia'
    df_Energy_output=df_Energy_output.assign(Sector='Energy')
    lista1=list(df_Energy_output.columns)
    # print(lista1)
    # print(len(lista1))
    #print(df_Energy_output)
    techs_energy=list(df_Energy_output['Technology'])
    techs_energy=EliminarRepetidos(techs_energy)
    techs_energy=EliminarNoStr(techs_energy)
    
    
    file = open("Sec_Energy.txt", "r")
    contents = file.read()
    Sec_Energy = ast.literal_eval(contents)
    file.close()
    
    
    'Se procede a hacer eso para cada sector'
    ###########################################################################################################
    ### AFOLU
    ###########################################################################################################
    df_AFOLU_output = pd.read_csv("../Salidas/"+lista_archivos_salida_sectoriales[2], index_col=None, header=0,low_memory=False)
    df_AFOLU_output.rename(columns = {'Run.ID':'Strategy'}, inplace = True)
    df_AFOLU_output.drop(['Fuel.DESCRIPTION', 'Technology.DESCRIPTION', 'Emission.DESCRIPTION', 'RateOfDemand', 'NumberOfNewTechnologyUnits', 'RateOfActivity', 'RateOfTotalActivity', 'TotalAnnualTechnologyActivityByMode', 'TotalTechnologyModelPeriodActivity', 'RateOfProductionByTechnologyByMode', 'RateOfProductionByTechnology', 'ProductionByTechnologyAnnual', 'RateOfProduction', 'Production', 'RateOfUseByTechnologyByMode', 'RateOfUseByTechnology', 'UseByTechnologyAnnual', 'UseAnnual', 'TotalCapacityInReserveMargin', 'DemandNeedingReserveMargin', 'TotalREProductionAnnual', 'RETotalProductionOfTargetFuelAnnual', 'AnnualTechnologyEmissionByMode', 'ModelPeriodEmissions'], axis='columns', inplace=True)
    df_AFOLU_output.insert(1,'Future.ID', ListaCeros(len(df_AFOLU_output)))
    df_AFOLU_output=df_AFOLU_output.assign(DistanceDriven=np.NaN)
    df_AFOLU_output=df_AFOLU_output.assign(Fleet=np.NaN)
    df_AFOLU_output=df_AFOLU_output.assign(NewFleet=np.NaN)
    df_AFOLU_output=df_AFOLU_output.assign(ProducedMobility=np.NaN)
    df_AFOLU_output=df_AFOLU_output.assign(FilterFuelType=np.NaN)
    df_AFOLU_output=df_AFOLU_output.assign(FilterVehicleType=np.NaN)
    
    ################################################################
    
    'Se agrega la columna de sector'
    df_AFOLU_output=df_AFOLU_output.assign(Sector='AFOLU')
    #print(df_AFOLU_output)
    techs_AFOLU=list(df_AFOLU_output['Technology'])
    techs_AFOLU=EliminarRepetidos(techs_AFOLU)
    techs_AFOLU=EliminarNoStr(techs_AFOLU)
    lista2=list(df_AFOLU_output.columns)
    # for i in range(len(lista1)):
    #     if lista1[i] not in lista2:
    #         print(lista1[i])
    # print(lista2)
    # print(len(lista2))
    # for i in range(len(lista2)):
    #     if lista2[i] not in lista1:
    #         print(lista2[i])
    
    file = open("Sec_AFOLU.txt", "r")
    contents = file.read()
    Sec_AFOLU = ast.literal_eval(contents)
    file.close()
    
    ###########################################################################################################
    ### PIUP
    ###########################################################################################################
    df_PIUP_output = pd.read_csv("../Salidas/"+lista_archivos_salida_sectoriales[0], index_col=None, header=0)
    
    df_PIUP_output=df_PIUP_output.assign(DistanceDriven=np.NaN)
    df_PIUP_output=df_PIUP_output.assign(Fleet=np.NaN)
    df_PIUP_output=df_PIUP_output.assign(NewFleet=np.NaN)
    df_PIUP_output=df_PIUP_output.assign(ProducedMobility=np.NaN)
    df_PIUP_output=df_PIUP_output.assign(FilterFuelType=np.NaN)
    df_PIUP_output=df_PIUP_output.assign(FilterVehicleType=np.NaN)
    'Se agrega la columna de sector'
    df_PIUP_output=df_PIUP_output.assign(Sector='PIUP')
    #print(df_PIUP_output)
    lista3=list(df_PIUP_output.columns)
    # print(lista3)
    # print(len(lista3))
    # for i in range(len(lista1)):
    #     if lista1[i] not in lista3:
    #         print(lista1[i])
    
    ###########################################################################################################
    ### Waste
    ###########################################################################################################
    df_Waste_output = pd.read_csv("../Salidas/"+lista_archivos_salida_sectoriales[1], index_col=None, header=0, low_memory=False)
    df_Waste_output=df_Waste_output.assign(DistanceDriven=np.NaN)
    df_Waste_output=df_Waste_output.assign(Fleet=np.NaN)
    df_Waste_output=df_Waste_output.assign(NewFleet=np.NaN)
    df_Waste_output=df_Waste_output.assign(ProducedMobility=np.NaN)
    df_Waste_output=df_Waste_output.assign(FilterFuelType=np.NaN)
    df_Waste_output=df_Waste_output.assign(FilterVehicleType=np.NaN)
    'Se agrega la columna de sector'
    df_Waste_output=df_Waste_output.assign(Sector='Waste')
    #print(df_Waste_output)
    lista4=list(df_Waste_output.columns)
    print(lista4)
    # print(len(lista4))
    # for i in range(len(lista1)):
    #     if lista1[i] not in lista3:
    #         print(lista1[i])
    
    # ###########################################################################################################
    # ### NO UTILIZAR
    # ###########################################################################################################
    'Se ordenan los dataframes con el orden del Dataframe de Energia'
    df_Energy_output=df_Energy_output[IndiceOrdenTabla(lista_aux, 'Sector', 2)]
    df_AFOLU_output=df_AFOLU_output[IndiceOrdenTabla(lista_aux, 'Sector', 2)]
    df_PIUP_output=df_PIUP_output[IndiceOrdenTabla(lista_aux, 'Sector', 2)]
    df_Waste_output=df_Waste_output[IndiceOrdenTabla(lista_aux, 'Sector', 2)]
    # print(df_Energy_output)
    # print(df_AFOLU_output)
    # print(df_PIUP_output)
    # print(df_Waste_output)
    # ###########################################################################################################
    
    ###########################################################################################################
    'Se reunen los 4 Dataframes'
    df_output = df_Energy_output._append(df_AFOLU_output)
    df_output = df_output._append(df_PIUP_output)
    df_output = df_output._append(df_Waste_output)
    ### Usamos diferentes nombres para escenarios entonces con esta linea siguiente los ponemos todos iguales
    #df_output['Strategy'] = df_output['Strategy'].replace(['DDP'], 'NDP')
    
    #####################################################################
    ### Usamos los diccionarios para ser más especificos con los sectores
    #####################################################################
    llaves=list(Sec_AFOLU.keys())
    col_sector=df_output['Sector'].values.tolist()
    df_output['SectorEspecifico'] = col_sector
    for i in range(len(llaves)):
        df_output.loc[df_output['Technology'] == llaves[i], 'SectorEspecifico'] =  Sec_AFOLU[llaves[i]]
    
    
    llaves=list(Sec_Energy.keys())
    for i in range(len(llaves)):
        df_output.loc[df_output['Technology'] == llaves[i], 'SectorEspecifico'] =  Sec_Energy[llaves[i]]
    
    ###########################################################################################################
    ### Escribir archivo unificado y filtrado por anios
    ###########################################################################################################
    df_output.sort_values(by=['Sector','Strategy','Future.ID','Fuel','Technology','Year','Emission'], inplace=True)
    #print(df_output.columns)
    df_output.to_csv ( '../f0_OSMOSYS_GUA_Output.csv', index = None, header=True)
    #print(df_output)
    # df_filter_year = df_output[df_output['Year'].isin(filtro_anios)]
    # df_filter_year.to_csv ( '../f0_OSMOSYS_GUA_Output_Filtrado.csv', index = None, header=True)

def main():
    print("*****************************************************")
    print("10. Unificando los archivos de salida sectoriales ...")
    print("*****************************************************")
    join_results()
    print("********************")
    print("El proceso finalizó.")
    print("********************")

if __name__== "__main__":
    main()