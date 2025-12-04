MOMF Version 3 Workflow
=======================

Version 3 is the most advanced MOMF implementation, featuring YAML-based configuration, scenario creator functionality, and otoole integration.

.. note::
   **Currently used in:** CRI/Energy and CRI/AFOLU only

Overview
--------

MOMF v3 introduces significant architectural improvements:

1. **YAML Configuration:** All settings externalized to YAML files
2. **Scenario Creator:** Organized scenario generation from MOMF_T1_A.yaml
3. **Otoole Integration:** Standardized OSeMOSYS data handling
4. **Multiple Solver Support:** GLPK, CBC, CPLEX
5. **Template System:** CSV templates for parameters

Pipeline Stages
---------------

The v3 pipeline follows the same A1, A2, B1, B2 stages as v2, but with YAML configuration.

Stage A1: Model Structure
~~~~~~~~~~~~~~~~~~~~~~~~~

Same as v2, but reads configuration from MOMF_T1_A.yaml.

.. warning::
   **A1_Model_Structure.py should only be run when creating a new model from scratch.** Running this script will overwrite any existing parameterization in the A1_Outputs folder. For existing models, skip directly to A2_Compiler.py.

Stage A2: Parameter Compiler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enhanced with YAML-driven settings from MOMF_T1_A.yaml.

Manual Step: Copy Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   After running A2_Compiler.py, you must manually copy the scenario folders from A2_Output_Params/ to B1_Output_Params/.

Stage B1: Scenario Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   **Before running B1:** You must first parameterize the master YAML configuration file (e.g., ``MOMF_B1_config.yaml``). This file controls scenario settings, solver selection, and sector toggles.

Multi-solver support: GLPK, CBC, or CPLEX (configured in the master YAML file).

.. important::
   **Run with External Console:** This script runs the solver and outputs progress to the console. In Spyder's default IPython console, output is not displayed until the entire process finishes. To see real-time progress:

   1. Go to **Run > Configuration per file** (or press Ctrl+F6)
   2. Select **Execute in an external system terminal**
   3. Check **Interact with the Python console after execution**
   4. Click **Run**

Stage B2: Results Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Output Files:**

- Executables/f0_OSMOSYS_{COUNTRY}_Output.csv - Consolidated output results
- Executables/f0_OSMOSYS_{COUNTRY}_Output_{DATE}.csv - Dated backup of output
- Executables/f0_OSMOSYS_{COUNTRY}_Input.csv - Consolidated input data
- Executables/f0_OSMOSYS_{COUNTRY}_Input_{DATE}.csv - Dated backup of input

Sector Toggles (B1)
-------------------

Sector toggles are configured in the master YAML file (e.g., ``MOMF_B1_config.yaml``), along with the solver selection. These settings allow you to enable or disable specific sectors without modifying the Python code.

**Example configuration in master YAML:**

.. code-block:: yaml

   # Solver selection
   Solver: GLPK  # Options: GLPK, CBC, CPLEX

   # Sector toggles
   Use_Transport_B1: True
   Use_Waste_B1: True
   Use_PIUP_B1: True

Complete Execution
------------------

To run the full MOMF v3 pipeline in Spyder:

1. Open Spyder and navigate to CRI/Energy/ndc_cr_30/t1_confection
2. Set the working directory
3. Open and run A1_Model_Structure.py (F5) - **only for new models**
4. Open and run A2_Compiler.py (F5)
5. **Manually copy scenario folders from A2_Output_Params/ to B1_Output_Params/**
6. Open and run B1_Base_Scenarios_Adj_Parallel.py (F5)
7. Open and run B2_Results_Creator_f0.py (F5)

Advantages over v2
------------------

1. **Externalized Configuration:** All settings in YAML (no code changes needed)
2. **Multi-Solver Support:** Use GLPK, CBC, or CPLEX
3. **Otoole Integration:** Standardized OSeMOSYS data handling
4. **Template System:** Consistent parameter structure
5. **Enhanced Parallelization:** Better resource management
