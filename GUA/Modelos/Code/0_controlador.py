'''
Hay 4 modelos sectoriales:
1. PIUP (IPPU en ingles)
2. Residuos (Waste)
3. AFOLU
4. Energy-Transport

Se determino que pueden ejecutarse en ese orden presentado en la anterior lista.
1) IPPU, 2) Residuos y 4)Energy-Transport estan construidos con el enfoque de LFVG
3) AFOLU está construido con el enfoque de Jam Angulo-Paniagua.

Se crea este codigo para automatizar la ejecucion secuencial de los modelos y la vinculacion de datos compartidos entre sectores
para luego obtener un Tableau total con los ecenarios BAU y DDP (EL NOMBRE DE ESTE SEGUNDO ESCENARIO HAY QUE HOMOLOGARLO LUEGO
ENTRE SECTORES) en conjunto. EL ANIO BASE TAMBIEN HAY QUE HOMOLOGARLO LUEGO


Cualquier cambio profundo que se vaya a realizar en el modelo, debe hacerse copiando en su computadora las carpetas M0_IPPU, M1_Waste, M2_AFOLU o M3_Energy
y luego de las modificaciones validadas se debe, sustituir las carpetas originales por las modificadas en el repositorio correspondiente del OneDrive.
Si se realizan cambios en los codigos de Python, por favor indicar a Ignacio Alfaro Corrales sobre ello
(ialfaro@clg-cr.com, al chat de Teams o al WS +506 85406141) para tomar las medidas del caso. Recordemos que los codigos
normalmente no se modifican. Los archivos excel y csv si pero los .py no es tan usual.


Progreso:
A continuacion se ejecutan los modelos de los sectores 1) IPPU y 2) Waste
Se continua trabajando en esta integracion'''

# Recordatorio
# B2....py: Corre el modelo y la optimización de OSeMOSYS para los 2 escenarios creados
# B2....py: Unifica resultados de 2 escenarios (BAU y DDP (EL NOMBRE DE ESTE SEGUNDO ESCENARIO HAY QUE HOMOLOGARLO LUEGO ENTRE SECTORES)) y los coloca en un solo .csv

# Se llaman los codigos B1 y B2 del sector 1) IPPU
import B1_IPPU_EjecucionOSeMOSYS as run_IPPU
import B2_IPPU_AcomodoResultados as create_results_file_IPPU

# Se llaman los codigos B1 y B2 del sector 2) Waste
import B1_Waste_EjecucionOSeMOSYS as run_Waste
import B2_Waste_AcomodoResultados as create_results_file_Waste

# Se llaman los codigos AFOLU1,2 y 3 del sector 3) AFOLU
import AFOLU1_csv_generation as csv_generation
import AFOLU2_run_model_mathprog as run_AFOLU
import AFOLU3_append as create_results_file_AFOLU
#################################################
### ESTE NO POR AHORA
import AFOLU4_output_rearreg as discount_costs_AFOLU
#################################################

# Se llaman los codigos B1 y B2 del sector 3) Energy
import B1_Energy_Base_Scenarios_Adj_Parallel as run_Energy
import B2_Energy_Results_Creator_f0 as create_results_file_Energy

# Se llaman el codigo para unificar resultados en un solo csv
import C1_Unificar_Outputs_Sectoriales as join_results


def main():
       
    """ Se podria ahorrar tiempo de ejecucion si se hacen cambios en algunos sectores y en otros no, PERO HAY QUE TENER MUCHO CUIDADO Y LO
    MAS RECOMENDABLE ES EJECUTAR TODOS LOS SECTORES PARA EVITAR ERRORES. Recordar que se eligio: PIUP -> WASTE -> AFOLU -> ENERGIA como 
    orden de ejecucion. Si se hacen cambios solo en PIUP, se debe ejecutar todo. Si se hacen cambios en Waste se puede ejecutar WASTE, AFOLU 
    y ENERGIA, sin correr PIUP. Si se hacen cambios en AFOLU unicamente, se puede ejecutar AFOLU y ENERGIA y evitar ejecutar PIUP y WASTE.
    Asi sucesivamente aguas abajo.
    
    Un cambio en la tasa o year de descuento hace que haya que ejecutar todo de nuevo.
    
    La forma que se eligio hacer eso es la siguiente lista a la cual se le pueden quitar sectores manualmente, pero no es recomendable. 
    """
    ### Lista de los modelos que se quieren ejecutar
    #lista_sectores_original_completa=['PIUP','Waste','AFOLU','Energia']
    lista_sectores_ejecucion=['PIUP','Waste','AFOLU','Energia']
    
    if 'PIUP' in lista_sectores_ejecucion:
        # Se ejecuta el codigo B1 y B2 para el sector 1) IPPU
        run_IPPU.main()
        create_results_file_IPPU.main()
    
    if 'Waste' in lista_sectores_ejecucion:
        # Se ejecuta el codigo B1 y B2 para el sector 2) Waste
        run_Waste.main()
        create_results_file_Waste.main()
    
    if 'AFOLU' in lista_sectores_ejecucion:
        # Se ejecuta el codigo AFOLU1,2 y 3 para el sector 3) Waste
        csv_generation.main()
        run_AFOLU.main()
        create_results_file_AFOLU.main()
        discount_costs_AFOLU.main()
    
    if 'Energia' in lista_sectores_ejecucion:
        # Se ejecuta el codigo B1 y B2 para el sector 4) Enegy and Transport
        run_Energy.main()
        create_results_file_Energy.main()
    
    # Se ejecuta el codigo para unificar archivos de salida
    join_results.main()


# IPPU = ['A1_EstructuraModelo.py', 'A2_AcomodoDatos.py', 'A3_CambiosEscenarios.py', 'B1_EjecucionOSeMOSYS.py', 'B2_AcomodoResultados.py']
# Waste = ['A1_EstructuraModelo.py', 'A2_AcomodoDatos.py', 'A3_CambiosEscenarios.py', 'B1_EjecucionOSeMOSYS.py', 'B2_AcomodoResultados.py']
# AFOLU = ['1_csv_generation.py', '7_run_model_mathprog.py', '3_append.py', 'output_rearreg.py'] # output_rearreg.py debe ejecutarse en todos los sectores una vez que se unificaran o incluir en B2_Results_Creator_f0.py
# Energy = ['A1_Model_Structure.py', 'A2_Compiler.py', 'B1_Base_Scenarios_Adj_Parallel_lean.py', 'B2_Results_Creator_f0.py']

if __name__== "__main__":
    main()