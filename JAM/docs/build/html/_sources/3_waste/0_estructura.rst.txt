===================================
Estructura del modelo
===================================

El sector energético analiza el consumo de energía, considerando la oferta 
primaria de combustibles, su producción, importación y exportación.  
Las categorías utilizadas se basan en el INGEI de la 5ta Comunicación 
Nacional (5CN) del Ecuador (MAATE, n.d.).

.. list-table:: *Tabla 3. Categorías del INGEI consideradas en el modelo de energía*
   :header-rows: 1
   :widths: 10 30 60

   * - Categoría INGEI
     - Nombre
     - Descripción
   * - 1A1
     - Industrias de energía como actividad principal
     - Abarca tecnologías de generación eléctrica reportadas en informes de ARCONEL (2022)
   * - 1A2
     - Industrias manufactureras y de la construcción
     - Engloba el consumo por tipo de combustible según el Balance de Energía Nacional (MEM, 2023).
   * - 1A3
     - Transporte
     - Incluye el consumo energético del sector transporte en todas sus formas.
   * - 1A4
     - Otros sectores
     - Registra el consumo por tipo de combustible en el sector residencial, comercial y público.
   * - 1A5
     - No especificado
     - Incluye otras categorías energéticas no detalladas en el Balance de Energía Nacional.
   * - 1B
     - Emisiones fugitivas
     - Se asocian a la producción de petróleo y gas natural.

.. image:: ../_static/_images/energia_estructura.png
   :align: center
   :alt: Figura2 - Estructura del modelo de energía

*Figura 2. Estructura del modelo de energía*



**Vectores energéticos**


*Tabla 4. Vectores energético incluidos en el modelo de energía*


+--------------------------------------------------+--------+
| Vector energético                                | Código |
+==================================================+========+
| Crudo de petróleo en yacimiento                  | E0CRU  |
+--------------------------------------------------+--------+
| Crudo de petróleo para consumo                   | E1CRU  |
+--------------------------------------------------+--------+
| Gas natural en yacimiento                        | E0NGS  |
+--------------------------------------------------+--------+
| Gas natural para consumo                         | E1NGS  |
+--------------------------------------------------+--------+
| Leña                                             | E1FIR  |
+--------------------------------------------------+--------+
| Biomasa                                          | E1BIM  |
+--------------------------------------------------+--------+
| Electricidad importada                           | E1ELE  |
+--------------------------------------------------+--------+
| Electricidad para transmisión                    | E1ELE  |
+--------------------------------------------------+--------+
| Electricidad para distribución                   | E2ELE  |
+--------------------------------------------------+--------+
| Electricidad para consumo                        | E3ELE  |
+--------------------------------------------------+--------+
| Gas licuado de Petróleo (GLP)                    | E0LPG  |
+--------------------------------------------------+--------+
| Gasolina                                         | E0GSL  |
+--------------------------------------------------+--------+
| Keroseno                                         | E1KER  |
+--------------------------------------------------+--------+
| Jet Fuel                                         | E1JET  |
+--------------------------------------------------+--------+
| Diesel                                           | E1DSL  |
+--------------------------------------------------+--------+
| Fuel Oil                                         | E1FO1  |
+--------------------------------------------------+--------+
| Biogasolina                                      | E1BGS  |
+--------------------------------------------------+--------+
| Coque de petróleo                                | E1COK  |
+--------------------------------------------------+--------+
| Otros productos de petróleo no energético        | E1OPE  |
+--------------------------------------------------+--------+
| Desechos municipales no biomasa                  | E1RDF  |
+--------------------------------------------------+--------+
| Óleos de desecho                                 | E1OID  |
+--------------------------------------------------+--------+
| Carbón de coque                                  | E1COA  |
+--------------------------------------------------+--------+
| Gas asociado                                     | E0GRE  |
+--------------------------------------------------+--------+

**Emisiones**


*Tabla 5. Clasificación de emisiones estimadas en el modelo de energía*


+-------------+----------------------------------------------------------------------------+
| Código      | Descripción                                                                |
+=============+============================================================================+
| CO2_sources | Dióxido de carbono equivalente de fuentes primarias de energía             |
+-------------+----------------------------------------------------------------------------+
| CO2e_DE     | Dióxido de carbono equivalente por consumo en sectores (residencial,       |
|             | comercial, transporte, agricultura, …)                                     |
+-------------+----------------------------------------------------------------------------+
| CO2_DE      | Dióxido de carbono por consumo en sectores (residencial, comercial,        |
|             | transporte, agricultura, …)                                                |
+-------------+----------------------------------------------------------------------------+
| CH4_DE      | Metano por consumo en sectores (residencial, comercial, transporte,        |
|             | agricultura, …)                                                            |
+-------------+----------------------------------------------------------------------------+
| N2O_DE      | Óxido nitroso por consumo en sectores (residencial, comercial, transporte, |
|             | agricultura, …)                                                            |
+-------------+----------------------------------------------------------------------------+
| CO2e_PP     | Dióxido de carbono equivalente por consumo en plantas eléctricas           |
+-------------+----------------------------------------------------------------------------+
| CO2_PP      | Dióxido de carbono por consumo en plantas de generación eléctrica          |
+-------------+----------------------------------------------------------------------------+
| CH4_PP      | Metano por consumo en plantas de generación eléctrica                      |
+-------------+----------------------------------------------------------------------------+
| N2O_PP      | Óxido nitroso por consumo en plantas de generación eléctrica               |
+-------------+----------------------------------------------------------------------------+
| CO2e_REF    | Dióxido de carbono equivalente por refinación de combustibles fósiles      |
+-------------+----------------------------------------------------------------------------+
| CO2_REF     | Dióxido de carbono por refinación de combustibles fósiles                  |
+-------------+----------------------------------------------------------------------------+
| CH4_REF     | Metano por refinación de combustibles fósiles                              |
+-------------+----------------------------------------------------------------------------+
| N2O_REF     | Óxido nitroso por refinación de combustibles fósiles                       |
+-------------+----------------------------------------------------------------------------+
| CO2e_FUG    | Dióxido de carbono equivalente por producción de combustibles fósiles      |
+-------------+----------------------------------------------------------------------------+
| CO2_FUG     | Dióxido de carbono por producción de combustibles fósiles                  |
+-------------+----------------------------------------------------------------------------+
| CH4_FUG     | Metano por producción de combustibles fósiles                              |
+-------------+----------------------------------------------------------------------------+
| N2O_FUG     | Óxido nitroso por producción de combustibles fósiles                       |
+-------------+----------------------------------------------------------------------------+


**Tecnologías**

*Tabla 6. Tecnologías incluidas en el modelo de energía*


+----------------------------------------------------------------------+---------------+
| Descripción                                                          | Código        |
+======================================================================+===============+
| Importación/Distribución - Diesel                                    | DIST_DSL      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Gasolina                                  | DIST_GSL      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Gas Natural                               | DIST_NGS      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Gas Licuado de Petróleo (GLP)             | DIST_LPG      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Coque                                     | DIST_COK      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Keroseno                                  | DIST_KER      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Jet Fuel                                  | DIST_JET      |
+----------------------------------------------------------------------+---------------+
| Extracción/Transformación Directa - Leña                             | DIST_FIR      |
+----------------------------------------------------------------------+---------------+
| Extracción/Transformación Directa - Carbón Vegetal                   | DIST_CHA      |
+----------------------------------------------------------------------+---------------+
| Extracción/Transformación Directa - Biomasa                          | DIST_BIM      |
+----------------------------------------------------------------------+---------------+
| Extracción/Transformación Directa - Biogasolina                      | DIST_BGS      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Otros Productos Energéticos               | DIST_OPE      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Residuos Municipales no Biomasa           | DIST_RDF      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Óleos de Desecho                          | DIST_OID      |
+----------------------------------------------------------------------+---------------+
| Reservas - Gas Natural                                               | EXTT_NGS      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Gas de Refinería                          | ADD_GRE       |
+----------------------------------------------------------------------+---------------+
| Extracción/Transformación - Crudo                                    | EXTT_CRU      |
+----------------------------------------------------------------------+---------------+
| Importación - Crudo                                                  | DIST_CRU      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Carbón                                    | DIST_COA      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Fuel Oil                                  | DIST_FOI      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Represa Amazonas Grande (+450 MW) | PPHDAMAB      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Represa Amazonas Mediana (<450 MW)| PPHDAMAM      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Represa Amazonas Pequeña (<50 MW) | PPHDAMAS      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Represa Pacífico Mediana (<450 MW)| PPHDAMPM      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Represa Pacífico Pequeña (<50 MW) | PPHDAMPS      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Paso Amazonas Grande (+450 MW)    | PPHRORAB      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Paso Amazonas Mediana (<450 MW)   | PPHRORAM      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Paso Amazonas Pequeña (<50 MW)    | PPHRORAS      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Paso Pacífico Mediana (<450 MW)   | PPHRORPM      |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica de Paso Pacífico Pequeña (<50 MW)    | PPHRORPS      |
+----------------------------------------------------------------------+---------------+
| Transformación - Geotérmica                                          | PPGEO         |
+----------------------------------------------------------------------+---------------+
| Transformación - Eólica                                              | PPWNDON       |
+----------------------------------------------------------------------+---------------+
| Transformación - Eólica Distribuida                                  | PPWNDD        |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica Aislada                              | PPIHD         |
+----------------------------------------------------------------------+---------------+
| Transformación - Hidroeléctrica Distribuida                          | PPHD          |
+----------------------------------------------------------------------+---------------+
| Transformación - Solar de Transmisión                                | PPPVT         |
+----------------------------------------------------------------------+---------------+
| Transformación - Solar de Transmisión con Almacenamiento             | PPPVTS        |
+----------------------------------------------------------------------+---------------+
| Transformación - Solar Distribuido                                   | PPPVD         |
+----------------------------------------------------------------------+---------------+
| Transformación - Solar Distribuido con Almacenamiento                | PPPVDS        |
+----------------------------------------------------------------------+---------------+
| Importación - Electricidad                                           | IMPELE        |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Gasolina                                  | DIST_GSL      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Jet Fuel                                  | DIST_JET      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Diesel                                    | DIST_DSL      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - Fuel Oil                                  | DIST_FOI      |
+----------------------------------------------------------------------+---------------+
| Importación/Distribución - GLP                                       | DIST_LPG      |
+----------------------------------------------------------------------+---------------+
| Transmisión de Electricidad                                          | ELE_TRANS     |
+----------------------------------------------------------------------+---------------+
| Distribución de Electricidad                                         | ELE_DIST      |
+----------------------------------------------------------------------+---------------+
| Transformación - Biomasa                                             | PPBIM         |
+----------------------------------------------------------------------+---------------+
| Transformación - Biogás                                              | PPBGS         |
+----------------------------------------------------------------------+---------------+
| Transformación - Gas Natural                                         | PPNGS         |
+----------------------------------------------------------------------+---------------+
| Transformación - Diesel                                              | PPDSL         |
+----------------------------------------------------------------------+---------------+
| Transformación - Fuel Oil                                            | PPFOI         |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - Diesel                                        | REF_DSL       |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - Gasolina                                      | REF_GSL       |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - GLP                                           | REF_LPG       |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - Fuel Oil                                      | REF_FOI       |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - Jet Fuel                                      | REF_JET       |
+----------------------------------------------------------------------+---------------+
| Refinería Secundaria - Otros Productos Energéticos                   | REF_OPE       |
+----------------------------------------------------------------------+---------------+
| Central Aislada - Refinería de Crudo                                 | PPCRU         |
+----------------------------------------------------------------------+---------------+
| Central Aislada - Refinería de Diesel                                | PPRDSL        |
+----------------------------------------------------------------------+---------------+
| Central Aislada - Refinería de Gas Natural                           | PPRNGS        |
+----------------------------------------------------------------------+---------------+
| Planta Distribuida - Fuel Oil                                        | PPDFOI        |
+----------------------------------------------------------------------+---------------+
| Planta Distribuida - Diesel                                          | PPDDSL        |
+----------------------------------------------------------------------+---------------+
| Central Aislada - GLP                                                | PPILPG        |
+----------------------------------------------------------------------+---------------+
| Central Aislada - Biomasa/Residuos                                   | PPIBIM        |
+----------------------------------------------------------------------+---------------+
| Producción - Crudo                                                   | PROCRU        |
+----------------------------------------------------------------------+---------------+
| Producción - Gas Natural                                             | PRONGS        |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Comercial                                     | T5DSLCOM      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Comercial                                        | T5LPGCOM      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Comercial                               | T5ELECOM      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Comercial                                   | T5FOICOM      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gas Natural para Residencial                              | T5NGSRES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Residencial                                 | T5GSLRES      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Residencial                                      | T5LPGRES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Residencial                             | T5ELERES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Keroseno para Residencial                                 | T5KERRES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Leña para Residencial                                     | T5FIRRES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Carbón Vegetal para Residencial                           | T5CHARES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Otros productos petroleros no energéticos para Residencial| T5OPERES      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Público                                 | T5ELEPUB      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Industrial                                    | T5DSLIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Industrial                                  | T5GSLIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gas Natural para Industrial                               | T5NGSIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Industrial                              | T5ELEIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Hidrógeno para Industrial                                 | T5HYDIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Industrial                                       | T5LPGIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Biomasa para Industrial                                   | T5BIMIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Leña para Industrial                                      | T5FIRIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Industrial                                  | T5FOIIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Construcción                                  | T5DSLCON      |
+----------------------------------------------------------------------+---------------+
| Demanda de Desechos municipales no biomasa para Industrial           | T5RDFIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Óleos de Desecho para Industrial                          | T5OIDIND      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Construcción                            | T5ELECON      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Construcción                                | T5FOICON      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Construcción y otros                        | T5GSLCON      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Construcción y otros                             | T5LPGCON      |
+----------------------------------------------------------------------+---------------+
| Demanda de Otros productos petroleros para Construcción              | T5OPECON      |
+----------------------------------------------------------------------+---------------+
| Demanda de Crudo para Exportaciones                                  | T5CRUEXP      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Exportaciones                                 | T5DSLEXP      |
+----------------------------------------------------------------------+---------------+
| Demanda de Jet Fuel y otros para Exportaciones                       | T5JETEXP      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Exportaciones                               | T5FOIEXP      |
+----------------------------------------------------------------------+---------------+
| Demanda de Jet Fuel y otros para Transporte - Aéreo                  | T5JETTAE      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Transporte - Marítimo                         | T5DSLTMA      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gas Natural para Transporte - Marítimo                    | T5NGSTMA      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Transporte - Marítimo                            | T5LPGTMA      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Transporte - Marítimo                   | T5ELETMA      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Transporte - Marítimo                       | T5FOITMA      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Transporte - Carretera                        | T5DSLTRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Transporte - Carretera                      | T5GSLTRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gas Natural para Transporte - Carretera                   | T5NGSTRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Transporte - Carretera                           | T5LPGTRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Electricidad para Transporte - Carretera                  | T5ELETRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Biocombustible/Biogás para Transporte - Carretera         | T5BGSTRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Transporte - Carretera                      | T5FOITRO      |
+----------------------------------------------------------------------+---------------+
| Demanda de Coque de Petróleo Industrial                              | T5INDCOK      |
+----------------------------------------------------------------------+---------------+
| Demanda de Residuos Vegetales Industriales                           | T5VEGWAS      |
+----------------------------------------------------------------------+---------------+
| Demanda de Fuel Oil para Transporte                                  | T5TRNFOI      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Comercial                                   | T5COMGSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Transporte Aéreo                            | T5TAEGSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Transporte Marítimo                         | T5TMAGSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Transporte de Carga Pesada                    | T5TCADSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Transporte de Carga Pesada                  | T5TCAGSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Keroseno para Construcción                                | T5CONKER      |
+----------------------------------------------------------------------+---------------+
| Demanda de Diesel para Agricultura                                   | T5AGRDSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de GLP para Agricultura                                      | T5AGRLPG      |
+----------------------------------------------------------------------+---------------+
| Demanda de Gasolina para Agricultura                                 | T5AGRGSL      |
+----------------------------------------------------------------------+---------------+
| Demanda de Otros productos petroleros no energéticos para Agricultura| T5AGROTP      |
+----------------------------------------------------------------------+---------------+
