===================================
Estructura del Modelo
===================================


El componente PIUP (Procesos Industriales y Uso de Productos) incluye procesos industriales que generan emisiones de GEI distintas a la combustión,
como la producción de clinker en la fabricación de cemento. También abarca el uso de productos con propiedades de GEI, como lubricantes, ceras, solventes
y gases refrigerantes, que pueden liberarse por fugas o mala disposición de equipos. Este sector no contempla el consumo energético industrial, ya que ese
aspecto se analiza en otros sectores del modelo multisectorial. La **Figura 10** presenta un resumen de los elementos considerados en la modelación.ficiencia energética
(MJ/km) por tipo de vehículo y datos de kilometraje recorrido.

Esta estructura permite simular trayectorias futuras y evaluar el impacto de distintas políticas de descarbonización.


.. figure:: ../_static/_images/10_ipu.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figura 10:** Estructura del modelo para el sector PIUP



**Tecnologías**

Las tecnologías utilizadas en el desarrollo del modelo del sector corresponden a las presentes en la **Tabla 5**.

  .. list-table:: **Tabla 5.** Tecnologías del PIUP
   :header-rows: 1
   :widths: 25 75
   :class: longtable

   * - **Tech**
     - **Descripción**

   * - RAW_MAT_CLK
     - Suministro de materia prima para clinker

   * - RAW_MAT_CEM
     - Suministro de materia prima para cemento

   * - IMP_STOR
     - Clinker importado o almacenado

   * - PROD_CLK_TRAD
     - Producción de clinker tradicional

   * - PROD_CEM
     - Producción de cemento

   * - PROD_CAL
     - Proceso de producción de cal

   * - PROD_FERRO
     - Proceso de producción de ferroniquel

   * - REFR_AC
     - Refrigeración y aire acondicionado

   * - OTHER
     - Otras emisiones

   * - T5CEM_PRODCEM_PROD
     - Producción nacional de cemento
