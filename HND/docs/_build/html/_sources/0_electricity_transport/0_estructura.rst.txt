===================================
Estructura del Modelo
===================================


El sector Energía y Transporte se modela de manera integrada para capturar las interacciones entre el consumo de energía y su uso final en el sistema de movilidad como se observa en la **Figura 3**.  Por el lado energético, se
analiza la oferta y demanda de fuentes primarias como petróleo crudo, gas natural, carbón mineral, leña, biomasa, electricidad, GLP, gasolinas, kerosene, diésel, fuel oil y coque de petróleo.
Se consideran las tecnologías de importación, exportación, producción, distribución y transformación de estas fuentes.

En cuanto al transporte, el modelo se enfoca en el transporte terrestre y analiza el uso de combustibles como diésel, gasolina, GLP, gas natural, electricidad, hidrógeno y tecnologías híbridas.
La demanda se desagrega en transporte público, privado, turístico, de carga liviana y de carga pesada. También se incluye, en escenarios estratégicos, tecnologías como trenes y teleféricos. La
caracterización del parque vehicular se basa en estadísticas nacionales y referencias internacionales, incluyendo la eficiencia energética (MJ/km) por tipo de vehículo y datos de kilometraje recorrido.
Esta estructura permite simular trayectorias futuras y evaluar el impacto de distintas políticas de descarbonización.


.. figure:: ../_static/_images/3_energia.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figura 3:** Estructura del modelo para los sectores Energía y Transporte



**Tecnologías**
Las tecnologías utilizadas en el desarrollo del modelo del subsector Energía corresponden a las presentes en la **Tabla 1**, para el subsector Transporte se presentan en la **Tabla 2**. 

.. list-table:: **Tabla 1. Tecnologías del Sector Energía**
   :widths: 25 75
   :header-rows: 1

   * - **Tech**
     - **Descripción**
   * - EXTT_CRU
     - Primaria - Extracción/Transformación - Crudo
   * - EXTT_LPG
     - Primaria - Extracción/Transformación - LPG
   * - DIST_FIR
     - Primaria - Extracción/Transformación/Distribución - Leña
   * - DIST_BIM
     - Primaria - Extracción/Transformación/Distribución - Biomasa
   * - DIST_BGS
     - Primaria - Extracción/Transformación/Distribución - Biogás
   * - DIST_CRU
     - Primaria - Importación/Distribución - Crudo
   * - DIST_NGS
     - Primaria - Importación/Distribución - Gas Natural
   * - DIST_DSL
     - Primaria - Importación/Distribución - Diesel
   * - DIST_GSL
     - Primaria - Importación/Distribución - Gasolina
   * - DIST_LPG
     - Primaria - Importación/Distribución - LPG
   * - DIST_FOI
     - Primaria - Importación/Distribución - Fuel Oil
   * - DIST_COK
     - Primaria - Importación/Distribución - Coke
   * - DIST_KER
     - Primaria - Importación/Distribución - Kerosen
   * - DIST_COA
     - Primaria - Importación/Distribución - Carbón
   * - IMP_ELE
     - Primaria - Importación - Electricidad
   * - PPHDAM
     - Central Hidroeléctrica de Embalse
   * - PPHROR
     - Central Hidroeléctrica de Paso
   * - PPGEO
     - Central Geotérmica
   * - PPWNDON
     - Central Eólica
   * - PPWNDOFF
     - Central Eólica Offshore
   * - PPPVT
     - Central Solar de Transmisión
   * - PPPVTHYD
     - Central Solar de Transmisión Hidrógeno
   * - PPPVTS
     - Central Solar de Transmisión con Baterías
   * - PPPVD
     - Central Solar Distribuida
   * - PPDHYD
     - Central Hidroeléctrica Autoproductor
   * - REF_DSL
     - Refinería Secundaria de Diesel
   * - REF_GSL
     - Refinería Secundaria de Gasolina
   * - REF_LPG
     - Refinería Secundaria de LPG
   * - REF_FOI
     - Refinería Secundaria de Fuel Oil
   * - PPBIM
     - Central de Biomasa
   * - PPBGS
     - Central de Biogás
   * - PPCOA
     - Central de Carbón
   * - PPCCTDSL
     - Ciclo Combinado y Turbina a Gas - Diesel
   * - PPCCFOIDSL
     - Ciclo Combinado - Fuel Oil y Diesel
   * - PPCCTNGS
     - Ciclo Combinado y Turbina a Gas - Gas Natural
   * - PPCCTNGSDSL
     - Ciclo Combinado y Turbina a Gas - Gas Natural y Diesel
   * - PPICEFOI
     - Motor de Combustión Interna - Fuel Oil
   * - PPICEGASFOI
     - Motor de Combustión Interna - Gas Natural y Fuel Oil
   * - PPADSL
     - Central Aislada - Diesel
   * - PPAFOI
     - Central Aislada - Fuel Oil
   * - PPANGS
     - Central Aislada - Gas Natural
   * - PPDBIM
     - Central Autoproductor - Biogás
   * - PPDBGS
     - Central Autoproductor - Biogás
   * - PPDDSL
     - Central Autoproductor - Diesel
   * - PPDFOI
     - Central Autoproductor - Fuel Oil
   * - PPDNGS
     - Central Autoproductor - Gas Natural
   * - PPDGSL
     - Central Autoproductor - Gasolina
   * - PPDGLP
     - Central Autoproductor - LPG
   * - ELE_TRANS
     - Transmisión Secundaria
   * - HYD_G_PROD
     - Producción de Hidrógeno Verde
   * - ELE_DIST
     - Distribución Secundaria
   * - HYD_DIST
     - Distribución de Hidrógeno Secundaria
   * - T5DSLCOM
     - Demanda Diesel Comercial
   * - T5GSLCOM
     - Demanda Gasolina Comercial
   * - T5NGSCOM
     - Demanda Gas Natural Comercial
   * - T5LPGCOM
     - Demanda LPG Comercial
   * - T5ELECOM
     - Demanda Eléctrica Comercial
   * - T5FIRCOM
     - Demanda Leña Comercial
   * - T5DSLIND
     - Demanda Diesel Industrial
   * - T5GSLIND
     - Demanda Gasolina Industrial
   * - T5NGSIND
     - Demanda Gas Natural Industrial
   * - T5LPGIND
     - Demanda LPG Industrial
   * - T5ELEIND
     - Demanda Eléctrica Industrial
   * - T5HYDIND
     - Demanda Hidrógeno Industrial
   * - T5COKIND
     - Demanda Coke Industrial
   * - T5BIMIND
     - Demanda Biomasa Industrial
   * - T5COAIND
     - Demanda Carbón Industrial
   * - T5FOIIND
     - Demanda Fuel Oil Industrial
   * - T5LPGRES
     - Demanda LPG Residencial
   * - T5ELERES
     - Demanda Eléctrica Residencial
   * - T5KERRES
     - Demanda Kerosen Residencial
   * - T5FIRRES
     - Demanda Leña Residencial
   * - T5BIMRES
     - Demanda Biomasa Residencial
   * - T5GSLCON
     - Demanda Gasolina Construcción
   * - T5LPGCON
     - Demanda LPG Construcción
   * - T5NGSEXP
     - Demanda Gas Natural Exportaciones
   * - T5KEREXP
     - Demanda Kerosen Exportaciones
   * - T5BIMEXP
     - Demanda Biomasa Exportaciones
   * - T5DSLTOT
     - Demanda Diesel Transporte - Otro
   * - T5GSLTOT
     - Demanda Gasolina Transporte - Otro
   * - T5ELETOT
     - Demanda Eléctrica Transporte - Otro
   * - T5GSLTAC
     - Demanda Gasolina Transporte - Aero
   * - T5KERTAC
     - Demanda Kerosen Transporte - Aero
   * - T5DSLAGR
     - Demanda Diesel Agricultura
   * - T5LPGAGR
     - Demanda LPG Agricultura
   * - T5ELEAGR
     - Demanda Eléctrica Agricultura

.. list-table:: **Tabla 2. Tecnologías del sector Transporte**
   :widths: 20 80
   :header-rows: 1

   * - **Tech**
     - **Descripción**
   * - TRAUT
     - Automóviles
   * - TRBPU
     - Buses públicos
   * - TRBTUR
     - Turismo
   * - TRMBS
     - Minibuses (Guaguas)
   * - TRMOT
     - Motocicletas
   * - TRSUV
     - SUV
   * - TRTAX
     - Taxis (Conchos)
   * - TRXTRAI
     - Tren de Pasajeros
   * - TRXTRAIFRE
     - Tren de Carga
   * - TRXTTEL
     - Teleférico
   * - TRYLF
     - Carga Liviana
   * - TRYTK
     - Carga Pesada


