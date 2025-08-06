===================================
Estructura del modelo
===================================

El sector Procesos Industriales y Uso de Productos (PIUP), es uno de los sectores de mitigación estudiados por el Panel Intergubernamental de Expertos sobre el Cambio Climático (en inglés Intergovernmental Panel on Climate Change o conocido también por sus siglas IPCC). En Ecuador, el sector PIUP abarca varias categorías y subcategorías emisoras de GEI, de acuerdo con el INGEI de la 5ta Comunicación Nacional (5CN) del Ecuador (MAATE, n.d.), que se enlistan a continuación:

- **Categoría 2A: Industria de los minerales**
    - **Subcategoría 2A1:** Producción de Cemento
    - **Subcategoría 2A2:** Producción de Cal
    - **Subcategoría 2A3:** Producción de Vidrio
    - **Subcategoría 2A4a:** Cerámica
    - **Subcategoría 2A4b:** Otros Usos de la Soda Ash
- **Categoría 2C: Industria de los metales**
    - **Subcategoría 2C1:** Producción de Hierro y Acero
    - **Subcategoría 2C5:** Producción de Plomo
- **Categoría 2D: Uso de Productos no Energéticos de combustibles y de solventes**
    - **Subcategoría 2D1:** Uso de Lubricantes
    - **Subcategoría 2D2:** Uso de Cera Parafina
- **Categoría 2F: Uso de Productos como sustitutos para las substancias que agotan la capa de ozono**
    - **Subcategoría 2F1:** Refrigeración y Aire Acondicionado

Basado en lo anterior, se construye un modelo en la herramienta OSeMOSYS para poder representar la actividad y las emisiones anuales de las categorías y subcategorías del sector, así como para facilitar la construcción de varios escenarios basado en la adopción de diversas políticas, acciones o iniciativas. De forma simplificada, el modelo se ilustra en la Figura 1.

.. figure:: ../_static/_images/PIUP_RSS.png
   :alt: Diagrama del sector 
   :width: 100%
   :align: center

   Figura 1. Diagrama de referencia del modelo del sector PIUP.

En las Tablas 1, 2 y 3 se incluye la nomenclatura de los sets Technologies, Commodities y Emission del modelo de la Figura 1.

*Tabla 1: Tecnologías incluidas en el modelo OSeMOSYS del sector PIUP.*

.. table::
   :align: center

   +---------------------------------------------------------+---------------------+
   | Descripción                                             | Código              |
   +=========================================================+=====================+
   | Suministro de materia prima para clinker                | RAW_MAT_CLK         |
   +---------------------------------------------------------+---------------------+
   | Suministro de materia prima para cemento                | RAW_MAT_CEM         |
   +---------------------------------------------------------+---------------------+
   | Clinker importado o almacenado                          | IMP_STOR            |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC                                      | IMP_REFR_AC         |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC23                                    | IMP_HFC23           |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC32                                    | IMP_HFC32           |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC125                                   | IMP_HFC125          |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC134a                                  | IMP_HFC134a         |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC143a                                  | IMP_HFC143a         |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC152a                                  | IMP_HFC152a         |
   +---------------------------------------------------------+---------------------+
   | Importación de HFC227ea                                 | IMP_HFC227ea        |
   +---------------------------------------------------------+---------------------+
   | Otros procesos industriales y uso de productos          | OTHER_IPPU          |
   +---------------------------------------------------------+---------------------+
   | Producción de clinker tradicional                       | PROD_CLK_TRAD       |
   +---------------------------------------------------------+---------------------+
   | Producción de cemento                                   | PROD_CEM            |
   +---------------------------------------------------------+---------------------+
   | Demanda - Producción de cemento                         | T5CEM_PRODIND       |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC                                           | T5REFR_ACIPPU       |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC23                                         | T5HFC23IPPU         |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC32                                         | T5HFC32IPPU         |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC125                                        | T5HFC125IPPU        |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC134a                                       | T5HFC134aIPPU       |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC143a                                       | T5HFC143aIPPU       |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC152a                                       | T5HFC152aIPPU       |
   +---------------------------------------------------------+---------------------+
   | Demanda - HFC227ea                                      | T5HFC227eaIPPU      |
   +---------------------------------------------------------+---------------------+
   | Demanda - Otros procesos industriales y uso de productos| T5OTHER_IPPUIPPU    |
   +---------------------------------------------------------+---------------------+
   | Producción de Cal                                       | LIME_PROD           |
   +---------------------------------------------------------+---------------------+
   | Producción de Vidrio                                    | GLASS_PROD          |
   +---------------------------------------------------------+---------------------+
   | Cerámica                                                | CERAMICS            |
   +---------------------------------------------------------+---------------------+
   | Otros usos de Soda Ash                                  | SODA_ASH            |
   +---------------------------------------------------------+---------------------+
   | Producción de Hierro y Acero                            | IRON_STEEL          |
   +---------------------------------------------------------+---------------------+
   | Producción de Plomo                                     | LEAD_PROD           |
   +---------------------------------------------------------+---------------------+
   | Uso de Lubricantes                                      | LUBRI               |
   +---------------------------------------------------------+---------------------+
   | Uso de Ceras de parafina                                | PARAFFIN            |
   +---------------------------------------------------------+---------------------+
   | Demanda - Producción de Cal                             | T5LIME_PRODIPPU     |
   +---------------------------------------------------------+---------------------+
   | Demanda - Producción de Vidrio                          | T5GLASS_PRODIPPU    |
   +---------------------------------------------------------+---------------------+
   | Demanda - Cerámica                                      | T5CERAMICSIPPU      |
   +---------------------------------------------------------+---------------------+
   | Demanda - Otros usos de Soda Ash                        | T5SODA_ASHIPPU      |
   +---------------------------------------------------------+---------------------+
   | Demanda - Producción de Hierro y Acero                  | T5IRON_STEELIPPU    |
   +---------------------------------------------------------+---------------------+
   | Demanda - Producción de Plomo                           | T5LEAD_PRODIPPU     |
   +---------------------------------------------------------+---------------------+
   | Demanda - Uso de Lubricantes                            | T5LUBRIIPPU         |
   +---------------------------------------------------------+---------------------+
   | Demanda - Uso de Ceras de parafina                      | T5PARAFFINIPPU      |
   +---------------------------------------------------------+---------------------+

*Tabla 2: Commodities incluidos en el modelo OSeMOSYS del sector PIUP.*

.. table:: 
   :align: center

   +----------------------------------------------------------+---------------------+
   | Descripción                                              | Código              |
   +==========================================================+=====================+
   | Materia prima para Clinker                               | RAW_MAT_CLK         |
   +----------------------------------------------------------+---------------------+
   | Materia prima para cemento                               | RAW_MAT_CEM         |
   +----------------------------------------------------------+---------------------+
   | Producción de Clinker                                    | CLK_PROD            |
   +----------------------------------------------------------+---------------------+
   | Refrigeración y Aire Acondicionado                       | REFR_AC             |
   +----------------------------------------------------------+---------------------+
   | HFC23                                                    | HFC23               |
   +----------------------------------------------------------+---------------------+
   | HFC32                                                    | HFC32               |
   +----------------------------------------------------------+---------------------+
   | HFC125                                                   | HFC125              |
   +----------------------------------------------------------+---------------------+
   | HFC134a                                                  | HFC134a             |
   +----------------------------------------------------------+---------------------+
   | HFC143a                                                  | HFC143a             |
   +----------------------------------------------------------+---------------------+
   | HFC152a                                                  | HFC152a             |
   +----------------------------------------------------------+---------------------+
   | HFC227ea                                                 | HFC227ea            |
   +----------------------------------------------------------+---------------------+
   | Otros procesos industriales y uso de productos           | OTHER_IPPU          |
   +----------------------------------------------------------+---------------------+
   | Producción de cemento                                    | CEM_PROD            |
   +----------------------------------------------------------+---------------------+
   | Demanda - Producción de cemento                          | E5INDCEM_PROD       |
   +----------------------------------------------------------+---------------------+
   | Demanda - Refrigeración y Aire Acondicionado             | E5IPPUREFR_AC       |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC23                                          | E5IPPUHFC23         |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC32                                          | E5IPPUHFC32         |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC125                                         | E5IPPUHFC125        |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC134a                                        | E5IPPUHFC134a       |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC143a                                        | E5IPPUHFC143a       |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC152a                                        | E5IPPUHFC152a       |
   +----------------------------------------------------------+---------------------+
   | Demanda - HFC227ea                                       | E5IPPUHFC227ea      |
   +----------------------------------------------------------+---------------------+
   | Demanda - Otros procesos industriales y uso de productos | E5IPPUOTHER_IPPU    |
   +----------------------------------------------------------+---------------------+
   | Producción de Cal                                        | LIME_PROD           |
   +----------------------------------------------------------+---------------------+
   | Producción de Vidrio                                     | GLASS_PROD          |
   +----------------------------------------------------------+---------------------+
   | Cerámica                                                 | CERAMICS            |
   +----------------------------------------------------------+---------------------+
   | Otros usos de Soda Ash                                   | SODA_ASH            |
   +----------------------------------------------------------+---------------------+
   | Producción de Hierro y Acero                             | IRON_STEEL          |
   +----------------------------------------------------------+---------------------+
   | Producción de Plomo                                      | LEAD_PROD           |
   +----------------------------------------------------------+---------------------+
   | Uso de Lubricantes                                       | LUBRI               |
   +----------------------------------------------------------+---------------------+
   | Uso de Ceras de parafina                                 | PARAFFIN            |
   +----------------------------------------------------------+---------------------+
   | Demanda - Producción de Cal                              | E5IPPULIME_PROD     |
   +----------------------------------------------------------+---------------------+
   | Demanda - Producción de Vidrio                           | E5IPPUGLASS_PROD    |
   +----------------------------------------------------------+---------------------+
   | Demanda - Cerámica                                       | E5IPPUCERAMICS      |
   +----------------------------------------------------------+---------------------+
   | Demanda - Otros usos de Soda Ash                         | E5IPPUSODA_ASH      |
   +----------------------------------------------------------+---------------------+
   | Demanda - Producción de Hierro y Acero                   | E5IPPUIRON_STEEL    |
   +----------------------------------------------------------+---------------------+
   | Demanda - Producción de Plomo                            | E5IPPULEAD_PROD     |
   +----------------------------------------------------------+---------------------+
   | Demanda - Uso de Lubricantes                             | E5IPPULUBRI         |
   +----------------------------------------------------------+---------------------+
   | Demanda - Uso de Ceras de parafina                       | E5IPPUPARAFFIN      |
   +----------------------------------------------------------+---------------------+


*Tabla 3: Emisiones incluidas en el modelo OSeMOSYS del sector PIUP.*

.. table::
   :align: center

   +--------------------------------------------------------------------------+-------------+
   | Descripción                                                              | Código      |
   +==========================================================================+=============+
   | Dióxido de carbono equivalente producido por Hidrofluorocarbonos         | CO2e_HFC    |
   +--------------------------------------------------------------------------+-------------+
   | Dióxido de carbono equivalente producido por el proceso de producción de | CO2e_CEM    |
   | cemento                                                                  |             |
   +--------------------------------------------------------------------------+-------------+
   | Dióxido de carbono equivalente producido por otros Procesos Industriales | CO2e_IPPU   |
   | y Uso de Productos                                                       |             |
   +--------------------------------------------------------------------------+-------------+