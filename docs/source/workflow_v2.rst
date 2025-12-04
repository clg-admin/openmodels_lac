MOMF Version 2 Workflow
=======================

Version 2 is the standard MOMF implementation with a 4-stage pipeline, enhanced scenario management, and parallel execution support.

.. note::
   **Currently used in:** Most country/sector combinations including:

   - CRI: IPPU, Waste
   - DOM: Energy, AFOLU, IPPU, Waste
   - ECU: Energy, Agriculture, FOLU, IPPU, Waste
   - GUA: Energy, AFOLU, IPPU, Waste
   - HND: Energy, AFOLU
   - JAM: AFOLU, Electricity_Building_Industry, Transport, Waste

Overview
--------

MOMF v2 introduces a more sophisticated architecture:

1. **Modular Input Structure:** Separate Excel files for different data types
2. **4-Stage Pipeline:** A1 (Structure) -> A2 (Compile) -> B1 (Scenarios) -> B2 (Results)
3. **Parallel Execution:** Multiple scenarios can run simultaneously
4. **Enhanced Scenario Management:** Flexible scenario configuration via Excel

Pipeline Stages
---------------

Stage A1: Model Structure (A1_Model_Structure.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Build the base model structure from demand and supply classifiers.

.. warning::
   **A1_Model_Structure.py should only be run when creating a new model from scratch.** Running this script will overwrite any existing parameterization in the A1_Outputs folder. For existing models, skip directly to A2_Compiler.py.

**Running in Spyder:**

1. Open Spyder
2. Navigate to the model folder using the File Browser
3. Set the working directory (right-click on folder > Set as current working directory)
4. Open A1_Model_Structure.py and run (F5)

**Input Files (must be parameterized):**

- A1_Inputs/A-I_Classifier_Modes_Demand.xlsx - Demand sector definitions
- A1_Inputs/A-I_Classifier_Modes_Supply.xlsx - Technology/supply definitions
- A1_Inputs/A-I_Horizon_Configuration.xlsx - Time horizon settings

**Output Files:**

- A1_Outputs/A-O_AR_Model_Base_Year.xlsx - Base year activity ratios
- A1_Outputs/A-O_AR_Projections.xlsx - Projection templates
- A1_Outputs/A-O_Demand.xlsx - Demand projections
- A1_Outputs/A-O_Parametrization.xlsx - Technology parameters

Stage A2: Parameter Compiler (A2_Compiler.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Compile all parameters into OSeMOSYS-compatible CSV files.

**Running in Spyder:**

Open A2_Compiler.py and run (F5).

**Input Files (must be parameterized):**

- A1_Outputs/A-O_AR_Model_Base_Year.xlsx - Base year activity ratios
- A1_Outputs/A-O_AR_Projections.xlsx - Projection templates
- A1_Outputs/A-O_Demand.xlsx - Demand projections
- A1_Outputs/A-O_Parametrization.xlsx - Technology parameters
- A2_Extra_Inputs/A-Xtra_Emissions.xlsx - Emission factors
- A2_Extra_Inputs/A-Xtra_Scenarios.xlsx - Scenario settings

**Output Files:**

- ``A2_Output_Params/{SCE}/*.csv`` - Parameter CSVs per scenario
- ``A1_Outputs/*_COMPLETED.xlsx`` - Processed files
- A2_Structure_Lists.xlsx - Sets/elements summary

Manual Step: Copy Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
   After running A2_Compiler.py, you must manually copy the scenario folders from A2_Output_Params/ to B1_Output_Params/. This step prepares the parameters for the scenario execution stage.

   For example, copy the BAU folder from A2_Output_Params/BAU/ to B1_Output_Params/BAU/.

Stage B1: Scenario Adjustment (B1_Base_Scenarios_Adj_Parallel.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Adjust parameters for different scenarios and execute the solver.

**Running in Spyder:**

Open B1_Base_Scenarios_Adj_Parallel.py in Spyder.

.. important::
   **Run with External Console:** This script runs the GLPK solver and outputs progress to the console. In Spyder's default IPython console, output is not displayed until the entire process finishes. To see real-time progress:

   1. Go to **Run > Configuration per file** (or press Ctrl+F6)
   2. Select **Execute in an external system terminal**
   3. Check **Interact with the Python console after execution**
   4. Click **Run**

   This allows you to monitor solver progress in real-time.

**Input Files:**

- OSeMOSYS_Model.txt - Mathematical model in AMPL/GLPK format
- ``B1_Output_Params/{SCE}/*.csv`` - Parameter CSVs (copied from A2_Output_Params)
- B1_Model_Structure.xlsx - OSeMOSYS structure definition
- B1_Scenario_Config.xlsx - Scenario adjustments
- B1_Default_Param.xlsx - Default parameter values

**Output Files:**

- Executables/{SCE}_0/{SCE}_0.txt - Solver data file
- Executables/{SCE}_0/{SCE}_0_Input.csv - Consolidated inputs
- Executables/{SCE}_0/{SCE}_0_Output.csv - Consolidated outputs
- ``B1_Output_Params/{SCE}/*.csv`` - Final adjusted parameters

Stage B2: Results Extraction (B2_Results_Creator_f0.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Consolidate and format final results from all scenarios.

**Running in Spyder:**

Open B2_Results_Creator_f0.py and run (F5).

**Output Files:**

- Executables/f0_OSMOSYS_{COUNTRY}_Output.csv - Consolidated output results
- Executables/f0_OSMOSYS_{COUNTRY}_Output_{DATE}.csv - Dated backup of output
- Executables/f0_OSMOSYS_{COUNTRY}_Input.csv - Consolidated input data
- Executables/f0_OSMOSYS_{COUNTRY}_Input_{DATE}.csv - Dated backup of input

Complete Execution
------------------

To run the full MOMF v2 pipeline in Spyder:

1. Open Spyder and navigate to {COUNTRY}/{SECTOR} (e.g., GUA/IPPU)
2. Set the working directory
3. Open and run A1_Model_Structure.py (F5) - **only for new models**
4. Open and run A2_Compiler.py (F5)
5. **Manually copy scenario folders from A2_Output_Params/ to B1_Output_Params/**
6. Open and run B1_Base_Scenarios_Adj_Parallel.py (F5)
7. Open and run B2_Results_Creator_f0.py (F5)

Scenarios Configuration
-----------------------

The default scenario in v2 is:

- **BAU:** Business As Usual

Additional scenarios can be configured in A-Xtra_Scenarios.xlsx and B1_Scenario_Config.xlsx.

Advantages over v1
------------------

- Modular input structure (easier maintenance)
- Parallel execution support
- Enhanced scenario management
- Automatic projection calculations
- GDP-normalized cost outputs
- Flexible configuration via Excel

Limitations
-----------

- No YAML configuration (hardcoded settings)
- Limited experiment management
- Manual scenario setup required
- No otoole integration

For advanced features, see :doc:`workflow_v3`.
