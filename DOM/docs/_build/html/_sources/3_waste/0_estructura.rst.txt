===================================
Estructura del Modelo
===================================


El sector residuos, en cuanto a la generación de emisiones de GEI, se divide en dos grandes categorías: residuos sólidos y aguas residuales, representadas en la **Figura 15** y **Figura 16** 
respectivamente. En la primera categoría, las emisiones se originan principalmente por la descomposición de materia orgánica en sitios de disposición final o
durante tratamientos específicos. Para capturar no solo las emisiones sino también las inversiones, operaciones y externalidades asociadas, el modelo del sector residuos
sólidos se estructura en varias etapas: generación, separación, recolección, y disposición final o tratamiento.

Esta estructura permite simular trayectorias futuras y evaluar el impacto de distintas políticas de descarbonización.


.. figure:: ../_static/_images/13_wastesolid.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figura 15:** Esquema resumen de los aspectos considerados para el sector residuos, del tipo sólidos.

.. figure:: ../_static/_images/14_wasteliquid.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figura 16:** Esquema resumen de los aspectos considerados para el sector residuos, del tipo líquidos.



**Tecnologías**

Las tecnologías utilizadas en el desarrollo del modelo del sector corresponden a las presentes en la **Tabla 7**.

 .. list-table:: **Tabla 7.** Tecnologías modeladas para el sector Residuos
   :header-rows: 1
   :widths: 30 70
   :class: longtable

   * - **Tech**
     - **Descripción**

   * - INORG_RCY_OS
     - Reciclaje de residuos inorgánicos separados en sitio de disposición final

   * - AD
     - Digestión anaerobia

   * - COMPOST
     - Compostaje

   * - LANDFILL
     - Relleno sanitario

   * - NO_CONTR_OD
     - Botadero a cielo abierto

   * - COPROC
     - Coprocesamiento

   * - INCIN
     - Incineración controlada

   * - OPEN_BURN
     - Quema a cielo abierto

   * - SIT_CLAN
     - Disposición en sitios clandestinos

   * - OSS_INORG
     - Separación de residuos inorgánicos en sitio de disposición final

   * - OSS_ORG
     - Separación de residuos orgánicos en sitio de disposición final

   * - NO_OSS_BLEND
     - No separación de residuos mezclados en sitio de disposición final

   * - NO_OSS_NO_COLL
     - No recolección de residuos sólidos en sitio de disposición final

   * - INORG_DCOLL
     - Recolección diferenciada de residuos inorgánicos

   * - ORG_DCOLL
     - Recolección diferenciada de residuos orgánicos

   * - BLEND_NO_DCOLL
     - Recolección no diferenciada de residuos mezclados

   * - BLEND_NO_COLL
     - No recolección de residuos sólidos

   * - INORG_SS
     - Separación de residuos inorgánicos en la fuente

   * - ORG_SS
     - Separación de residuos orgánicos en la fuente

   * - NO_SS
     - No separación de residuos en la fuente

   * - LANDFILL_ELEC
     - Recuperación de metano para generación de electricidad

   * - T5TSWTSW
     - Generación nacional de residuos sólidos

   * - AERO_PTAR
     - Planta de tratamiento aerobica centralizada

   * - AERO_PTAR_RU
     - Reúso de agua tratada proveniente de una planta centralizada de tratamiento aeróbico de aguas residuales

   * - ANAE_LAGN
     - Laguna anaeróbica

   * - ANAE_LAGN_RU
     - Reúso de agua tratada proveniente de una laguna anaeróbica

   * - SEPT_SYST
     - Sistema séptico

   * - LATR
     - Letrina

   * - EFLT_DISC
     - Vertido de efluentes al medio acuático

   * - SEWER_NO_T
     - Aguas residuales recolectadas no tratadas

   * - WWWT
     - Aguas residuales con tratamiento

   * - WWWOT
     - Aguas residuales sin tratamiento

   * - SEWERWW
     - Aguas residuales recolectadas

   * - DIRECT_DISC
     - Aguas residuales no recolectadas

   * - IWW
     - Aguas residuales industriales

   * - T5TWWTWW
     - Generación nacional de aguas residuales
