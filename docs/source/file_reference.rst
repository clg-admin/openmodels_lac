File Reference
==============

This section documents all file types used in MOMF models.

Input Files
-----------

A1 Stage Inputs
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - A-I_Classifier_Modes_Demand.xlsx
     - Demand sector definitions, fuel types, base year demands
   * - A-I_Classifier_Modes_Supply.xlsx
     - Technology definitions, input/output fuels, efficiencies
   * - A-I_Horizon_Configuration.xlsx
     - Time horizon (base year, final year, region, timeslices)

A2 Stage Inputs
~~~~~~~~~~~~~~~

**For IPPU, Waste, AFOLU models:**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - A-Xtra_Emissions.xlsx
     - Emission factors (GHGs sheet) and externalities
   * - A-Xtra_Scenarios.xlsx
     - Scenario configuration (region, timeslice, modes)
   * - A-Xtra_Readme.txt
     - Documentation for extra inputs

**For Energy models (additional files):**

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - A-Xtra_Projections.xlsx
     - External projection data
   * - A-Xtra_Battery_Replacement.xlsx
     - Battery cost projections for EVs

B1 Stage Inputs
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - B1_Model_Structure.xlsx
     - OSeMOSYS sets, parameters, and variables structure
   * - B1_Scenario_Config.xlsx
     - Scenario adjustments (tech adoption, efficiency, etc.)
   * - B1_Default_Param.xlsx
     - Default parameter values

Configuration Files (v3)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - MOMF_T1_A.yaml
     - Configuration for A1 and A2 scripts
   * - MOMF_B1_exp_manager.yaml
     - Master YAML configuration
   * - conversion_format.yaml
     - Otoole parameter definitions

Output Files
------------

A1 Stage Outputs
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - File
     - Description
   * - A-O_AR_Model_Base_Year.xlsx
     - Activity ratios for base year
   * - A-O_AR_Projections.xlsx
     - Activity ratio projection templates
   * - A-O_AR_Projections_COMPLETED.xlsx
     - Completed AR projections
   * - A-O_Demand.xlsx
     - Demand projection templates
   * - A-O_Demand_COMPLETED.xlsx
     - Completed demand projections
   * - A-O_Parametrization.xlsx
     - Technology parameter templates
   * - A-O_Parametrization_COMPLETED.xlsx
     - Completed parameters (OSeMOSYS units)
   * - A-O_Parametrization_Natural_COMPLETED.xlsx
     - Parameters in natural units

B2 Final Outputs
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - File
     - Description
   * - f0_OSMOSYS_{COUNTRY}_Output.csv
     - All scenarios consolidated output
   * - f0_OSMOSYS_{COUNTRY}_Output_{DATE}.csv
     - Dated backup of output
   * - f0_OSMOSYS_{COUNTRY}_Input.csv
     - All scenarios consolidated input
   * - f0_OSMOSYS_{COUNTRY}_Input_{DATE}.csv
     - Dated backup of input

Model Files
-----------

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - OSeMOSYS_Model.txt
     - Mathematical model in AMPL/GLPK format
   * - A2_Structure_Lists.xlsx
     - Generated sets and elements summary

Python Scripts
--------------

v1 Scripts
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Script
     - Purpose
   * - 1_csv_generation.py
     - Generate CSV parameters from Excel
   * - 2_run_model_mathprog.py
     - Execute GLPK solver
   * - 3_append.py
     - Consolidate results

v2/v3 Scripts
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Script
     - Purpose
   * - A1_Model_Structure.py
     - Build model structure from classifiers
   * - A2_Compiler.py
     - Compile parameters to CSV
   * - B1_Base_Scenarios_Adj_Parallel.py
     - Adjust scenarios and run solver
   * - B2_Results_Creator_f0.py
     - Extract and consolidate results
