import Auxiliares as AUX
import pandas as pd
import math

libro=AUX.LeerExcel("CambiosEscenarios.xlsx")
listaHojas=AUX.ListaHojas(libro)

# Hoja del SpecifiedAnnualDemand

hoja1=AUX.LeerHoja2(libro, listaHojas[0], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
    df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/SpecifiedAnnualDemand.csv", index_col=None, header=0, low_memory=False)
    lista1=list(df_Energy_output.columns)
    print(lista1)
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
    for j in range(len(df_Energy_output)):
        if df_Energy_output["FUEL"][j]==encab[i].split(";")[0]:
            df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
    
    df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/SpecifiedAnnualDemand.csv", index = None, header=True)
    

# Hoja del TotalTechnologyAnnualActivityLowerLimit

dic2={"INORG_RCY_OS":"E5_TSWTSW",
      "AD":"E5_TSWTSW",
      "COMPOST":"E5_TSWTSW",
      "LANDFILL_BG":"E5_TSWTSW",
      "LANDFILL":"E5_TSWTSW",
      "NO_CONTR_OD":"E5_TSWTSW",
      "OPEN_BURN":"E5_TSWTSW",
      "SIT_CLAN":"E5_TSWTSW",
      "OSS_INORG":"E5_TSWTSW",
      "OSS_ORG":"E5_TSWTSW",
      "NO_OSS_BLEND":"E5_TSWTSW",
      "NO_OSS_NO_COLL":"E5_TSWTSW",
      "INORG_DCOLL":"E5_TSWTSW",
      "ORG_DCOLL":"E5_TSWTSW",
      "BLEND_NO_DCOLL":"E5_TSWTSW",
      "BLEND_NO_COLL":"E5_TSWTSW",
      "INORG_SS":"E5_TSWTSW",
      "ORG_SS":"E5_TSWTSW",
      "NO_SS":"E5_TSWTSW",
      "AERO_PTAR":"E5_TWWTWW",
      "AERO_PTAR_RU":"E5_TWWTWW",
      "ANAE_LAGN":"E5_TWWTWW",
      "ANAE_LAGN_RU":"E5_TWWTWW",
      "SEPT_SYST":"E5_TWWTWW",
      "LATR":"E5_TWWTWW",
      "EFLT_DISC":"E5_TWWTWW",
      "WWWT":"E5_TWWTWW",
      "WWWOT":"E5_TWWTWW",
      "SEWERWW":"E5_TWWTWW",
      "DIRECT_DISC":"E5_TWWTWW",
      "MEAT":"E5_TSWTSW",
      "BEER":"E5_TSWTSW",
      "VEGT":"E5_TSWTSW",
      "ANIM":"E5_TSWTSW",
      "SUGR":"E5_TSWTSW",
      "DAIR":"E5_TSWTSW",
      "PETR":"E5_TSWTSW"}

#con esta lista leer del xlsx y multiplicar por los porcentajes del mismo xlsx pero de otra hoja

hoja1=AUX.LeerHoja2(libro, listaHojas[1], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
    a=0
    df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityLowerLimit.csv", index_col=None, header=0, low_memory=False)
    df_Energy_output2 = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityUpperLimit.csv", index_col=None, header=0, low_memory=False)
    lista1=list(df_Energy_output.columns)
    #print(lista1)
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
     
    #Leer la hoja SAD
    hoja2=AUX.LeerHoja2(libro, listaHojas[0], 0)
    col2=AUX.LeerCol(hoja2,dic2[encab[i].split(";")[0]]+";"+encab[i].split(";")[1])
    dic3=dict(zip(years,col2))
     
    for j in range(len(df_Energy_output)):
        if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0]:
            if df_Energy_output["TECHNOLOGY"][j] not in ['MEAT','BEER','VEGT','ANIM','SUGR','DAIR','PETR','LANDFILL_ELEC','LATR','EFLT_DISC']:
                df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]*dic3[df_Energy_output["YEAR"][j]]
            elif df_Energy_output["TECHNOLOGY"][j] in ['LATR','EFLT_DISC']:
                df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]*dic3[df_Energy_output["YEAR"][j]]
                df_Energy_output2["Value"][j]=math.ceil(dic[df_Energy_output2["YEAR"][j]]*dic3[df_Energy_output2["YEAR"][j]] * 10000) / 10000 
                a=2
            else:
                df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
                df_Energy_output2["Value"][j]=dic[df_Energy_output["YEAR"][j]]
                a=1
    
    if a==1:
        df_Energy_output2.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityUpperLimit.csv", index = None, header=True) 
    if a ==2:
        df_Energy_output2.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityUpperLimit.csv", index = None, header=True)
    df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityLowerLimit.csv", index = None, header=True)


# Hoja del TotalTechnologyAnnualActivityUpperLimit

# dic2={"OPEN_BURN":"E5_TSWTSW"}


# # #con esta lista leer del xlsx y multiplicar por los porcentajes del mismo xlsx pero de otra hoja

# hoja1=AUX.LeerHoja2(libro, listaHojas[2], 0)
# encab=AUX.LeerHeaders(hoja1)
# years=AUX.LeerCol(hoja1, encab[0])
# for i in range(1,len(encab)):
#       df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityUpperLimit.csv", index_col=None, header=0, low_memory=False)
#       lista1=list(df_Energy_output.columns)
#       #print(lista1)
#       col=AUX.LeerCol(hoja1,encab[i])
#       dic=dict(zip(years,col))
     
#       #Leer la hoja SAD
#       hoja2=AUX.LeerHoja2(libro, listaHojas[0], 0)
#       col2=AUX.LeerCol(hoja2,dic2[encab[i].split(";")[0]]+";"+encab[i].split(";")[1])
#       dic3=dict(zip(years,col2))
     
#       for j in range(len(df_Energy_output)):
#           if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0]:
#             df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]*dic3[df_Energy_output["YEAR"][j]]
    
#       df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/TotalTechnologyAnnualActivityUpperLimit.csv", index = None, header=True)


# Hoja del EmissionActivityRatio
# PARAMETER,Scenario,REGION,TECHNOLOGY,FUEL,EMISSION,MODE_OF_OPERATION,YEAR,TIMESLICE,SEASON,DAYTYPE,DAILYTIMEBRACKET,STORAGE,Value

# #con esta lista leer del xlsx y sustituir el EAR en el csv

# hoja1=AUX.LeerHoja2(libro, listaHojas[2], 0)
# encab=AUX.LeerHeaders(hoja1)
# years=AUX.LeerCol(hoja1, encab[0])
# for i in range(1,len(encab)):
#       df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionActivityRatio.csv", index_col=None, header=0, low_memory=False)
#       lista1=list(df_Energy_output.columns)
#       #print(lista1)
#       col=AUX.LeerCol(hoja1,encab[i])
#       dic=dict(zip(years,col))
      
#       for j in range(len(df_Energy_output)):
#           if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0] and df_Energy_output["EMISSION"][j]=="CO2e":
#             df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
    
#       df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionActivityRatio.csv", index = None, header=True)
      
      
# Hoja del EmissionsPenalty

hoja1=AUX.LeerHoja2(libro, listaHojas[2], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
    df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionsPenalty.csv", index_col=None, header=0, low_memory=False)
    
    lista1=list(df_Energy_output.columns)
    # print(lista1)
    # print(len(df_Energy_output))
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
    for j in range(len(years)):
        listaAux=['EmissionsPenalty',encab[i].split(";")[1],'GUA','','',encab[i].split(";")[0],'',years[j],'','','','','',dic[years[j]]]
        df_Energy_output.loc[len(df_Energy_output)] = listaAux
    
    df_Energy_output = df_Energy_output.drop_duplicates(subset = ['EMISSION','YEAR'],keep = 'last')
    df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/EmissionsPenalty.csv", index = None, header=True)
    
    
# Hoja del CapitalCost

hoja1=AUX.LeerHoja2(libro, listaHojas[3], 0)
encab=AUX.LeerHeaders(hoja1)
years=AUX.LeerCol(hoja1, encab[0])
for i in range(1,len(encab)):
    df_Energy_output = pd.read_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/CapitalCost.csv", index_col=None, header=0, low_memory=False)
    lista1=list(df_Energy_output.columns)
    print(lista1)
    col=AUX.LeerCol(hoja1,encab[i])
    dic=dict(zip(years,col))
    for j in range(len(df_Energy_output)):
        if df_Energy_output["TECHNOLOGY"][j]==encab[i].split(";")[0]:
            df_Energy_output["Value"][j]=dic[df_Energy_output["YEAR"][j]]
    
    df_Energy_output.to_csv("A2_Output_Params/"+encab[i].split(";")[1]+"/CapitalCost.csv", index = None, header=True)
    
    
########################################################################
########### COPIAAMOS CARPETAS DE A2_Outputs_Params a B1_Outputs_Params
########################################################################
        
from distutils.dir_util import copy_tree


DIRECTORIO_ORIGEN = "./A2_Output_Params/"
DIRECTORIO_DESTINO = "./B1_Output_Params/"


print("Copiando...")
copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO)
print("Copiado")

########################################################################

