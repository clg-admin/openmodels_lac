Country Models
==============

MOMF is implemented for six Latin American and Caribbean countries, each with sector-specific models aligned to national GHG inventories.

Country Overview
----------------

.. list-table::
   :header-rows: 1
   :widths: 15 15 40 30

   * - Country
     - Code
     - Sectors
     - MOMF Version
   * - Costa Rica
     - CRI
     - Energy, AFOLU, IPPU, Waste
     - v2 (IPPU, Waste), v3 (Energy, AFOLU)
   * - Dominican Republic
     - DOM
     - Energy, AFOLU, IPPU, Waste
     - v2 (all)
   * - Ecuador
     - ECU
     - Energy, Agriculture, FOLU, IPPU, Waste
     - v2 (all)
   * - Guatemala
     - GUA
     - Energy, AFOLU, IPPU, Waste
     - v2 (all except AFOLU), v1 (AFOLU)
   * - Honduras
     - HND
     - Energy, AFOLU
     - v2 (all)
   * - Jamaica
     - JAM
     - AFOLU, Electricity_Building_Industry, Transport, Waste
     - v2 (all)

Sector-Version Matrix
---------------------

.. list-table::
   :header-rows: 1
   :widths: 20 13 13 13 13 13 15

   * - Sector
     - CRI
     - DOM
     - ECU
     - GUA
     - HND
     - JAM
   * - Energy
     - **v3**
     - v2
     - v2
     - v2
     - v2
     - --
   * - AFOLU
     - **v3**
     - v2
     - --
     - **v1**
     - v2
     - v2
   * - Agriculture
     - --
     - --
     - v2
     - --
     - --
     - --
   * - FOLU
     - --
     - --
     - v2
     - --
     - --
     - --
   * - IPPU
     - v2
     - v2
     - v2
     - v2
     - --
     - --
   * - Waste
     - v2
     - v2
     - v2
     - v2
     - --
     - v2
   * - Transport
     - --
     - --
     - --
     - --
     - --
     - v2
   * - Elec_Build_Ind
     - --
     - --
     - --
     - --
     - --
     - v2

Country Details
---------------

Costa Rica (CRI)
~~~~~~~~~~~~~~~~

**Location:** CRI/

**Sectors:**

.. list-table::
   :widths: 25 15 60

   * - Sector
     - Version
     - Path
   * - Energy
     - v3
     - CRI/Energy/ndc_cr_30/t1_confection/
   * - AFOLU
     - v3
     - CRI/AFOLU/ndc_cr_30/t1_confection/
   * - IPPU
     - v2
     - CRI/IPPU/
   * - Waste
     - v2
     - CRI/Waste/

Dominican Republic (DOM)
~~~~~~~~~~~~~~~~~~~~~~~~

**Location:** DOM/

**Sectors:**

.. list-table::
   :widths: 25 15 60

   * - Sector
     - Version
     - Path
   * - Energy
     - v2
     - DOM/Energy/
   * - AFOLU
     - v2
     - DOM/AFOLU/
   * - IPPU
     - v2
     - DOM/IPPU/
   * - Waste
     - v2
     - DOM/Waste/

Ecuador (ECU)
~~~~~~~~~~~~~

**Location:** ECU/

**Sectors:**

.. list-table::
   :widths: 25 15 60

   * - Sector
     - Version
     - Path
   * - Energy
     - v2
     - ECU/Energy/
   * - Agriculture
     - v2
     - ECU/Agriculture/
   * - FOLU
     - v2
     - ECU/FOLU/
   * - IPPU
     - v2
     - ECU/IPPU/
   * - Waste
     - v2
     - ECU/Waste/

Guatemala (GUA)
~~~~~~~~~~~~~~~

**Location:** GUA/

**Sectors:**

.. list-table::
   :widths: 25 15 60

   * - Sector
     - Version
     - Path
   * - Energy
     - v2
     - GUA/Energy/
   * - AFOLU
     - **v1**
     - GUA/AFOLU/
   * - IPPU
     - v2
     - GUA/IPPU/
   * - Waste
     - v2
     - GUA/Waste/

Honduras (HND)
~~~~~~~~~~~~~~

**Location:** HND/

**Sectors:**

.. list-table::
   :widths: 25 15 60

   * - Sector
     - Version
     - Path
   * - Energy
     - v2
     - HND/Energy/
   * - AFOLU
     - v2
     - HND/AFOLU/

Jamaica (JAM)
~~~~~~~~~~~~~

**Location:** JAM/

**Sectors:**

.. list-table::
   :widths: 30 15 55

   * - Sector
     - Version
     - Path
   * - AFOLU
     - v2
     - JAM/AFOLU/
   * - Electricity_Building_Industry
     - v2
     - JAM/Electricity_Bulding_Industry/
   * - Transport
     - v2
     - JAM/Transport/
   * - Waste
     - v2
     - JAM/Waste/

Adding a New Country
--------------------

1. Create country folder (3-letter code):

   .. code-block:: bash

      mkdir ABC

2. Create sector subfolders:

   .. code-block:: bash

      mkdir ABC/Energy ABC/AFOLU ABC/IPPU ABC/Waste

3. Copy template from existing country (v2 recommended):

   .. code-block:: bash

      cp -r DOM/Energy/* ABC/Energy/

4. Update all A1_Inputs files:

   - A1_Inputs/A-I_Horizon_Configuration.xlsx - Set country code, years
   - A1_Inputs/A-I_Classifier_Modes_Demand.xlsx - Define demand sectors
   - A1_Inputs/A-I_Classifier_Modes_Supply.xlsx - Define technologies

5. Update configuration files:

   - A2_Extra_Inputs/A-Xtra_Scenarios.xlsx - Set region
   - B1_Scenario_Config.xlsx - Configure scenarios

6. Populate input data:

   - Technology definitions
   - Cost parameters
   - Emission factors
   - Demand projections

7. Run and validate:

   .. code-block:: bash

      cd ABC/Energy
      python A1_Model_Structure.py
      # ... continue pipeline
