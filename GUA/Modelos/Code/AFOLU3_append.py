# import pandas as pd

# ############
# sector = 'land'
# #sector = 'energy'
# #sector = 'water'
# ############
 
# #sce1 = 'BAU'
# #sce2 = 'PEN'

# data_output1 = './0_files/0_energy/BAU_0_Output.csv'
# data_output2 = './0_files/0_energy/NDP_0_Output.csv'


# df1 = pd.read_csv(data_output1)
# df2 = pd.read_csv(data_output2)

# df2 = df1.append(df2)

# df2.to_csv( '../Salidas/2_AFOLU_Output_integrated_output.csv', index = None, header=True)

import pandas as pd

def archivo_resultados():
    ############
    sector = 'land'
    ############
    
    sce = ['BAU', 'NDP']
    
    dfacum= pd.DataFrame()
    
    for z in sce:
        data_output_name = '../M2_AFOLU/2_Model/'+z+'/data_'+sector+'_'+z+ '_Output.csv'
        df1 = pd.read_csv(data_output_name,low_memory=False)
        dfacum=dfacum._append(df1)
    
    dfacum.to_csv( '../Salidas/2_AFOLU_GUA_Output.csv', index = None, header=True)
    
    
def archivo_entradas():
    ############
    sector = 'land'
    ############
    
    sce = ['BAU', 'NDP']
    
    dfacum= pd.DataFrame()
    
    for z in sce:
        data_output_name = '../M2_AFOLU/2_Model/'+z+'/data_'+sector+'_'+z+ '_Input.csv'
        df1 = pd.read_csv(data_output_name)
        dfacum=dfacum._append(df1)
    
    dfacum.to_csv( '../Salidas/2_AFOLU_GUA_Input.csv', index = None, header=True)


def main():
    print("******************************************")
    print("7. Creando resultados del sector AFOLU ...")
    print("******************************************")
    archivo_resultados()
    archivo_entradas()
    print("********************")
    print("El proceso finalizó.")
    print("********************")

if __name__== "__main__":
    main()
