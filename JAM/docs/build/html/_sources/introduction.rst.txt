====================================
Introducción
====================================

Esta documentación describe el modelo OSeMOSYS-ECU, desarrollado en 
colaboración con el **PNUD y FAO** para evaluar las emisiones de gases de 
efecto invernadero (GEI) en Ecuador entre 2010 y 2035.  

El modelo permite:
- Evaluar las trayectorias de emisiones bajo diferentes escenarios.
- Comparar el escenario tendencial con estrategias de mitigación.
- Desagregar resultados por sector, tipo de gas y año.

El modelado se basa en **OSeMOSYS** y amplía los desarrollos del **PLANMICC**.  

-------------------------------------
Estructura de Carpetas
-------------------------------------

Para facilitar la navegación, la documentación sigue la siguiente estructura 
de archivos:

.. code-block:: none

    docs/
    │── index.rst               # Página principal
    │── introduccion.rst         # Introducción del modelo
    │── metodologia.rst          # Metodología general
    │── energia/                 # Sector Energía
    │   ├── 0_estructura.rst
    │   ├── 1_entradas.rst
    │   ├── 2_escenarios.rst
    │   ├── 3_resultados.rst
    │   ├── 4_referencias.rst
    │── residuos/                # Sector Residuos
    │── procesos/                # Sector Procesos Industriales
    │── agricultura/              # Sector Agricultura
    │── uscuss/                   # Sector Uso del Suelo y Cambio de Uso del Suelo
    │── license.rst               # Información sobre la licencia
    │── authors.rst               # Créditos y autores
    │── source/                   # Carpeta de recursos
    │   ├── _static/              # Recursos estáticos (imágenes, gráficos)
    │   │   ├── _images/          # Imágenes utilizadas en la documentación

