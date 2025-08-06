===================================
Estructura del modelo
===================================
El sector USCUSS analiza los cambios de uso de suelo y las emisiones y absorciones de CO2 provenientes de estos cambios, así como las absorciones debido a las áreas forestales protegidas. Las categorías analizadas se encuentran en la **Tabla 27**.


.. list-table:: *Tabla 27. Categorías del INGEI consideradas en el modelo de USCUSS*
   :header-rows: 1

   * - Código
     - Descripción
   * - 3B1a
     - Tierras forestales que permanecen como tales
   * - 3B1b
     - Cambios de tierra de cultivo a tierras forestales
   * - 3B1b
     - Cambios de pastizales a tierras forestales
   * - 3B1b
     - Cambios de humedales a tierras forestales
   * - 3B1b
     - Cambios de otras tierras a tierras forestales
   * - 3B2b
     - Cambios de tierras forestales a tierras de cultivo
   * - 3B2b
     - Cambios de humedales a tierras de cultivo
   * - 3B2b
     - Cambios de otras tierras a tierras de cultivo
   * - 3B3b
     - Cambios de tierras forestales a pastizales
   * - 3B3b
     - Cambios de tierras cultivo a pastizales
   * - 3B3b
     - Cambios de humedales a pastizales
   * - 3B3b
     - Cambios de otras tierras a pastizales
   * - 3B4b
     - Cambios de tierras forestales a humedales
   * - 3B4b
     - Cambios de tierras cultivo a humedales
   * - 3B4b
     - Cambios de pastizales a humedales
   * - 3B5b
     - Cambios de tierras forestales a asentamientos
   * - 3B5b
     - Cambios de tierras cultivo a asentamientos
   * - 3B5b
     - Cambios de pastizales a asentamientos
   * - 3B6b
     - Cambios de tierras forestales a otras tierras
   * - 3B6b
     - Cambios de tierras cultivo a otras tierras
   * - 3B6b
     - Cambios de pastizales a otras tierras

Las tierras forestales fueron subdivididas según los tipos de bosque, según la clasificación del INGEI:

- Seco andino
- Seco pluvioestacional
- Siempre verde andino montano
- Siempre verde andino pie montano
- Siempre verde andino ceja andina
- Siempre verde de tierras bajas de la Amazonía
- Siempre verde de tierras bajas del Chocó
- Manglar
- Moretal

**Emisiones**

El modelo del sector USCUSS únicamente contabiliza emisiones y absorciones de CO2.


**Tecnologías**

.. list-table:: *Tabla 28 Tecnologías de uso de suelo incluidas en el modelo de USCUSS*
   :header-rows: 1

   * - Código
     - Descripción
   * - LU_FOR
     - Suelo forestal
   * - LU_WET
     - Suelo humedales
   * - LU_CROP
     - Suelo tierras de cultivo
   * - LU_PAS
     - Suelo pastizales
   * - LU_SET
     - Suelo asentamientos
   * - LU_OTL
     - Suelo otros usos
   * - LU_NPRAND
     - B. Seco Andino - protegido
   * - LU_NUNAND
     - B. Seco Andino - no protegido
   * - LU_NPRPFO
     - Plantación forestal - protegido
   * - LU_NUNPFO
     - Plantación forestal - no protegido
   * - LU_NPRPLU
     - B. Pluvioestacional - protegido 
   * - LU_NUNPLU
     - B. Pluvioestacional - no protegido 
   * - LU_NPRMON
     - B. Siempre verde andino Montano - protegido
   * - LU_NUNMON
     - B. Siempre verde andino Montano - no protegido
   * - LU_NPRPIE
     - B. Siempre verde andino Pie montano - protegido
   * - LU_NUNPIE
     - B. Siempre verde andino Pie montano - no protegido
   * - LU_NPRCEJ
     - B. Siempre verde andino de Ceja Andina - protegido
   * - LU_NUNCEJ
     - B. Siempre verde andino de Ceja Andina - no protegido
   * - LU_NPRAMA
     - B. Siempre verde de tierras bajas de la Amazonía - protegido
   * - LU_NUNAMA
     - B. Siempre verde de tierras bajas de la Amazonía - no protegido
   * - LU_NPRCHO
     - B. Siempre verde de tierras bajas del Chocó - protegido
   * - LU_NUNCHO
     - B. Siempre verde de tierras bajas del Chocó - no protegido
   * - LU_RAR
     - Área restaurada
   * - LU_PLA
     - Plantación forestal
   * - LU_NPRMAN
     - Manglar - protegido
   * - LU_NUNMAN
     - Manglar - no protegido
   * - LU_NPRMOR
     - Moretal - protegido
   * - LU_NUNMOR
     - Moretal - no protegido
   * - T5WETCOB
     - Cobertura humedales
   * - T5SETCOB
     - Cobertura asentamientos
   * - T5BURCOB
     - Cobertura quemas
   * - T5OTLCOB
     - Cobertura otros usos 
   * - T5NPRAND
     - Cobertura B. Seco Andino - protegido
   * - T5NUNAND
     - Cobertura B. Seco Andino - no protegido
   * - T5NPRPLU
     - Cobertura B. Pluvioestacional protegido
   * - T5NUNPLU
     - Cobertura B. Pluvioestacional - no protegido
   * - T5NPRMON
     - Cobertura B. Siempre verde andino Montano - protegido
   * - T5NUNMON
     - Cobertura B. Siempre verde andino Montano - no protegido
   * - T5NPRPIE
     - Cobertura B. Siempre verde andino Pie montano - protegido
   * - T5NUNPIE
     - Cobertura B. Siempre verde andino Pie montano - no protegido
   * - T5NPRCEJ
     - Cobertura B. Siempre verde andino de Ceja Andina - protegido
   * - T5NUNCEJ
     - Cobertura B. Siempre verde andino de Ceja Andina - no protegido
   * - T5NPRAMA
     - Cobertura B. Siempre verde de tierras bajas de la Amazonía - protegido
   * - T5NUNAMA
     - Cobertura B. Siempre verde de tierras bajas de la Amazonía - no protegido
   * - T5NPRCHO
     - Cobertura B. Siempre verde de tierras bajas del Chocó - protegido
   * - T5NUNCHO
     - Cobertura B. Siempre verde de tierras bajas del Chocó - no protegido
   * - T5RARBOS
     - Cobertura Área restaurada
   * - T5PLABOS
     - Cobertura Plantación forestal
   * - T5NPRMAN
     - Cobertura Manglar - protegido
   * - T5NUNMAN
     - Cobertura Manglar - no protegido
   * - T5NPRMOR
     - Cobertura Moretal - protegido
   * - T5NUNMOR
     - Cobertura Moretal - no protegido
   * - T5NPRPFO
     - Cobertura Plantación forestal - protegido
   * - T5NUNPFO
     - Cobertura Plantación forestal - no protegido
   * - SUPCAMCROAND
     - Cambio de tierras de cultivo a B. Seco Andino
   * - SUPCAMCROPLU
     - Cambio de tierras de cultivo a B. Pluvioestacional
   * - SUPCAMCROMON
     - Cambio de tierras de cultivo a B. Siempre verde andino Montano
   * - SUPCAMCROPIE
     - Cambio de tierras de cultivo a B. Siempre verde andino Pie montano
   * - SUPCAMCROCEJ
     - Cambio de tierras de cultivo a B. Siempre verde andino de Ceja Andina
   * - SUPCAMCROAMA
     - Cambio de tierras de cultivo a B. Siempre verde de tierras bajas de la Amazonía
   * - SUPCAMCROCHO
     - Cambio de tierras de cultivo a B. Siempre verde de tierras bajas del Chocó
   * - SUPCAMCROMAN
     - Cambio de tierras de cultivo a Manglar
   * - SUPCAMCROMOR
     - Cambio de tierras de cultivo a Moretal
   * - SUPCAMCROPFO
     - Cambio de tierras de cultivo a Plantación forestal
   * - SUPCAMGRAAND
     - Cambio de pastizales a B. Seco Andino
   * - SUPCAMGRAPLU
     - Cambio de pastizales a B. Pluvioestacional
   * - SUPCAMGRAMON
     - Cambio de pastizales a B. Siempre verde andino Montano
   * - SUPCAMGRAPIE
     - Cambio de pastizales a B. Siempre verde andino Pie montano
   * - SUPCAMGRACEJ
     - Cambio de pastizales a B. Siempre verde andino de Ceja Andina
   * - SUPCAMGRAAMA
     - Cambio de pastizales a B. Siempre verde de tierras bajas de la Amazonía
   * - SUPCAMGRACHO
     - Cambio de pastizales a B. Siempre verde de tierras bajas del Chocó
   * - SUPCAMGRAMAN
     - Cambio de pastizales a Manglar
   * - SUPCAMGRAMOR
     - Cambio de pastizales a Moretal
   * - SUPCAMGRAPFO
     - Cambio de pastizales a Plantación forestal
   * - SUPCAMHUMAND
     - Cambio de humedales a B. Seco Andino
   * - SUPCAMHUMPLU
     - Cambio de humedales a B. Pluvioestacional
   * - SUPCAMHUMMON
     - Cambio de humedales a B. Siempre verde andino Montano
   * - SUPCAMHUMPIE
     - Cambio de humedales a B. Siempre verde andino Pie montano
   * - SUPCAMHUMCEJ
     - Cambio de humedales a B. Siempre verde andino de Ceja Andina
   * - SUPCAMHUMAMA
     - Cambio de humedales a B. Siempre verde de tierras bajas de la Amazonía
   * - SUPCAMHUMCHO
     - Cambio de humedales a B. Siempre verde de tierras bajas del Chocó
   * - SUPCAMHUMMAN
     - Cambio de humedales a Manglar
   * - SUPCAMHUMMOR
     - Cambio de humedales a Moretal
   * - SUPCAMHUMPFO
     - Cambio de humedales a Plantación forestal
   * - SUPCAMOTIAND
     - Cambio de otras tierras a B. Seco Andino
   * - SUPCAMOTIPLU
     - Cambio de otras tierras a B. Pluvioestacional
   * - SUPCAMOTIMON
     - Cambio de otras tierras a B. Siempre verde andino Montano
   * - SUPCAMOTIPIE
     - Cambio de otras tierras a B. Siempre verde andino Pie montano
   * - SUPCAMOTICEJ
     - Cambio de otras tierras a B. Siempre verde andino de Ceja Andina
   * - SUPCAMOTIAMA
     - Cambio de otras tierras a B. Siempre verde de tierras bajas de la Amazonía
   * - SUPCAMOTICHO
     - Cambio de otras tierras a B. Siempre verde de tierras bajas del Chocó
   * - SUPCAMOTIMAN
     - Cambio de otras tierras a Manglar
   * - SUPCAMOTIMOR
     - Cambio de otras tierras a Moretal
   * - SUPCAMOTIPFO
     - Cambio de otras tierras a Plantación forestal
   * - SUPCAMANDCRO
     - Cambio B. Seco Andino a tierras de cultivo
   * - SUPCAMPLUCRO
     - Cambio B. Pluvioestacional a tierras de cultivo
   * - SUPCAMMONCRO
     - Cambio B. Siempre verde andino Montano a tierras de cultivo
   * - SUPCAMPIECRO
     - Cambio B. Siempre verde andino Pie montano a tierras de cultivo
   * - SUPCAMCEJCRO
     - Cambio B. Siempre verde andino de Ceja Andina a tierras de cultivo
   * - SUPCAMAMACRO
     - Cambio B. Siempre verde de tierras bajas de la Amazonía a tierras de cultivo
   * - SUPCAMCHOCRO
     - Cambio B. Siempre verde de tierras bajas del Chocó a tierras de cultivo
   * - SUPCAMMANCRO
     - Cambio Manglar a tierras de cultivo
   * - SUPCAMMORCRO
     - Cambio Moretal a tierras de cultivo
   * - SUPCAMPFOCRO
     - Cambio Plantación forestal a tierras de cultivo
   * - SUPCAMGRACRO
     - Cambio Pastizales a tierras de cultivo
   * - SUPCAMHUMCRO
     - Cambio Humedales a tierras de cultivo
   * - SUPCAMASECRO
     - Cambio Asentamientos a tierras de cultivo
   * - SUPCAMOTICRO
     - Cambio Otros usos a tierras de cultivo
   * - SUPCAMANDGRA
     - Cambio B. Seco Andino a pastizales
   * - SUPCAMPLUGRA
     - Cambio B. Pluvioestacional a pastizales
   * - SUPCAMMONGRA
     - Cambio B. Siempre verde andino Montano a pastizales
   * - SUPCAMPIEGRA
     - Cambio B. Siempre verde andino Pie montano a pastizales
   * - SUPCAMCEJGRA
     - Cambio B. Siempre verde andino de Ceja Andina a pastizales
   * - SUPCAMAMAGRA
     - Cambio B. Siempre verde de tierras bajas de la Amazonía a pastizales
   * - SUPCAMCHOGRA
     - Cambio B. Siempre verde de tierras bajas del Chocó a pastizales
   * - SUPCAMMANGRA
     - Cambio Manglar a pastizales
   * - SUPCAMMORGRA
     - Cambio Moretal a pastizales
   * - SUPCAMPFOGRA
     - Cambio Plantación forestal a pastizales
   * - SUPCAMCROGRA
     - Cambio Tierras de cultivo a pastizales
   * - SUPCAMHUMGRA
     - Cambio Humedales a pastizales
   * - SUPCAMOTIGRA
     - Cambio Otros usos a pastizales
   * - SUPCAMANDHUM
     - Cambio B. Seco Andino a humedales
   * - SUPCAMPLUHUM
     - Cambio B. Pluvioestacional a humedales
   * - SUPCAMMONHUM
     - Cambio B. Siempre verde andino Montano a humedales
   * - SUPCAMPIEHUM
     - Cambio B. Siempre verde andino Pie montano a humedales
   * - SUPCAMCEJHUM
     - Cambio B. Siempre verde andino de Ceja Andina a humedales
   * - SUPCAMAMAHUM
     - Cambio B. Siempre verde de tierras bajas de la Amazonía a humedales
   * - SUPCAMCHOHUM
     - Cambio B. Siempre verde de tierras bajas del Chocó a humedales
   * - SUPCAMMANHUM
     - Cambio Manglar a humedales
   * - SUPCAMMORHUM
     - Cambio Moretal a humedales
   * - SUPCAMPFOHUM
     - Cambio Plantación forestal a humedales
   * - SUPCAMCROHUM
     - Cambio Tierras de cultivo a humedales
   * - SUPCAMGRAHUM
     - Cambio Pastizales a humedales
   * - SUPCAMANDASE
     - Cambio B. Seco Andino hacia asentamientos
   * - SUPCAMPLUASE
     - Cambio B. Pluvioestacional hacia asentamientos
   * - SUPCAMMONASE
     - Cambio B. Siempre verde andino Montano hacia asentamientos
   * - SUPCAMPIEASE
     - Cambio B. Siempre verde andino Pie montano hacia asentamientos
   * - SUPCAMCEJASE
     - Cambio B. Siempre verde andino de Ceja Andina hacia asentamientos
   * - SUPCAMAMAASE
     - Cambio B. Siempre verde de tierras bajas de la Amazonía hacia asentamientos
   * - SUPCAMCHOASE
     - Cambio B. Siempre verde de tierras bajas del Chocó hacia asentamientos
   * - SUPCAMMANASE
     - Cambio Manglar hacia asentamientos
   * - SUPCAMMORASE
     - Cambio Moretal hacia asentamientos
   * - SUPCAMPFOASE
     - Cambio Plantación forestal hacia asentamientos
   * - SUPCAMCROASE
     - Cambio Tierras de cultivo a asentamientos
   * - SUPCAMGRAASE
     - Cambio Pastizales a asentamientos
   * - SUPCAMANDOTI
     - Cambio B. Seco Andino a otras tierras
   * - SUPCAMPLUOTI
     - Cambio B. Pluvioestacional a otras tierras
   * - SUPCAMMONOTI
     - Cambio B. Siempre verde andino Montano a otras tierras
   * - SUPCAMPIEOTI
     - Cambio B. Siempre verde andino Pie montano a otras tierras
   * - SUPCAMCEJOTI
     - Cambio B. Siempre verde andino de Ceja Andina a otras tierras
   * - SUPCAMAMAOTI
     - Cambio B. Siempre verde de tierras bajas de la Amazonía a otras tierras
   * - SUPCAMCHOOTI
     - Cambio B. Siempre verde de tierras bajas del Chocó a otras tierras
   * - SUPCAMMANOTI
     - Cambio Manglar a otras tierras
   * - SUPCAMMOROTI
     - Cambio Moretal a otras tierras
   * - SUPCAMPFOOTI
     - Cambio Plantación forestal a otras tierras
   * - SUPCAMCROOTI
     - Cambio Tierras de cultivos a otras tierras
   * - SUPCAMGRAOTI
     - Cambio Pastizales a otras tierras
   * - SUPMEDREST
     - Medida 1. Restauración forestal
   * - SUPMEDRESTMAN
     - Medida 2. Restauración manglar
   * - SUPMEDABAMA
     - Medida 4. Bosques protectores Bosque Siempre Verde de Tierras Bajas de la Amazonía - absorción
   * - SUPMEDABMOR
     - Medida 4. Bosques protectores Moretales - absorción
   * - SUPMEDABPIE
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Pie Montano - absorción
   * - SUPMEDABCHO
     - Medida 4. Bosques protectores Bosque Siempre Verde de Tierras Bajas del Chocó - absorción
   * - SUPMEDABMON
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Montano - absorción
   * - SUPMEDABPIE2
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Pie Montano - absorción
   * - SUPMEDDEFAMA
     - Medida 4. Bosques protectores Bosque Siempre Verde de Tierras Bajas de la Amazonía - deforestación evitada
   * - SUPMEDDEFMOR
     - Medida 4. Bosques protectores Moretales - deforestación evitada
   * - SUPMEDDEFPIE
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Pie Montano - deforestación evitada
   * - SUPMEDDEFCHO
     - Medida 4. Bosques protectores Bosque Siempre Verde de Tierras Bajas del Chocó - deforestación evitada
   * - SUPMEDDEFMON
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Montano - deforestación evitada
   * - SUPMEDDEFPIE2
     - Medida 4. Bosques protectores Bosque Siempre Verde Andino Pie Montano - deforestación evitada
   * - SUPMED5DEFAND
     - Medida 5. Socio bosque B. Seco Andino - deforestación evitada
   * - SUPMED5DEFPLU
     - Medida 5. Socio bosque B. Seco Pluvioestacional - deforestación evitada
   * - SUPMED5DEFMON
     - Medida 5. Socio bosque B. Siempre verde andino Montano - deforestación evitada
   * - SUPMED5DEFPIE
     - Medida 5. Socio bosque B. Siempre verde andino Pie montano - deforestación evitada
   * - SUPMED5DEFCEJ
     - Medida 5. Socio bosque B. Siempre verde andino de Ceja Andina - deforestación evitada
   * - SUPMED5DEFAMA
     - Medida 5. Socio bosque B. Siempre verde de tierras bajas de la Amazonía - deforestación evitada
   * - SUPMED5DEFCHO
     - Medida 5. Socio bosque B. Siempre verde de tierras bajas del Chocó - deforestación evitada
   * - SUPMED5DEFMAN
     - Medida 5. Socio bosque Manglar - deforestación evitada
   * - SUPMED5ABAND
     - Medida 5. Socio bosque B. Seco Andino - absorción
   * - SUPMED5ABPLU
     - Medida 5. Socio bosque B. Seco Pluvioestacional - absorción
   * - SUPMED5ABMON
     - Medida 5. Socio bosque B. Siempre verde andino Montano - absorción
   * - SUPMED5ABPIE
     - Medida 5. Socio bosque B. Siempre verde andino Pie montano - absorción
   * - SUPMED5ABCEJ
     - Medida 5. Socio bosque B. Siempre verde andino de Ceja Andina - absorción
   * - SUPMED5ABAMA
     - Medida 5. Socio bosque B. Siempre verde de tierras bajas de la Amazonía - absorción
   * - SUPMED5ABCHO
     - Medida 5. Socio bosque B. Siempre verde de tierras bajas del Chocó - absorción
   * - SUPMED5ABMAN
     - Medida 5. Socio bosque Manglar - absorción
   * - SUPMED3ABCEJ
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino de Ceja Andina - absorción
   * - SUPMED3ABMON
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino Montano - absorción
   * - SUPMED3ABCEJA
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino de Ceja Andina - absorción
   * - SUPMED3DEFCEJ
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino de Ceja Andina - deforestación evitada
   * - SUPMED3DEFMON
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino Montano - deforestación evitada
   * - SUPMED3DEFCEJA
     - Medida 3. Taita Imbaura Bosque Siempre Verde Andino de Ceja Andina - deforestación evitada
   * - SUPMED6DABAMA
     - Medida 6. WWF Bosque Siempre Verde de Tierras Bajas de la Amazonía - absorción
   * - SUPMED6DEFAMA
     - Medida 6. WWF Bosque Siempre Verde de Tierras Bajas de la Amazonía - deforestación evitada