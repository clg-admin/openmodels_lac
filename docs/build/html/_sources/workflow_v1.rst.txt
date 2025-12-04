MOMF Version 1 Workflow
=======================

Version 1 is the simplest implementation of MOMF, using a streamlined 3-script pipeline with direct Excel input.

.. note::
   **Currently used in:** GUA/AFOLU only

Overview
--------

MOMF v1 uses a straightforward approach:

1. Single Excel file contains all model parameters
2. Python scripts generate OSeMOSYS data files
3. GLPK solver runs the optimization
4. Results are consolidated across scenarios

Directory Structure
-------------------

.. code-block:: text

   SECTOR/
   ├── 0_Ref/                          # Reference files
   │   ├── STRUCTURE_OSEMOSYS_*.xlsx   # OSeMOSYS structure definition
   │   ├── data_land.txt               # Reference data file
   │   └── Long_Model_OG.txt           # Original model template
   │
   ├── 1_Parameters/                   # Generated CSV parameters
   │   ├── BAU/                        # Business As Usual scenario
   │   │   ├── AvailabilityFactor.csv
   │   │   ├── CapitalCost.csv
   │   │   ├── EmissionActivityRatio.csv
   │   │   └── ... (27 parameter files)
   │   └── NDP/                        # NDC scenario
   │       └── ... (27 parameter files)
   │
   ├── 2_Model/                        # Model execution files
   │   ├── BAU/
   │   │   ├── ModeloSuelo_BAU.xlsx    # INPUT: Model in Excel
   │   │   ├── data_land.txt           # Generated GLPK data file
   │   │   ├── data_land_BAU_Input.csv # Consolidated input dataset
   │   │   └── data_land_BAU_Output.csv# Consolidated output dataset
   │   └── NDP/
   │       └── ...
   │
   ├── 1_csv_generation.py             # Stage 1: Excel to CSV
   ├── 2_run_model_mathprog.py         # Stage 2: Run GLPK solver
   ├── 3_append.py                     # Stage 3: Consolidate results
   ├── Auxiliares.py                   # Auxiliary functions
   └── OSeMOSYS_Model.txt              # OSeMOSYS mathematical model

Pipeline Stages
---------------

Stage 1: CSV Generation (1_csv_generation.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Transform Excel model data into OSeMOSYS-compatible CSV files and GLPK data format.

**Running in Spyder:**

1. Open Spyder
2. Navigate to the model folder (e.g., GUA/AFOLU) using the File Browser
3. Set the working directory (right-click on folder > Set as current working directory)
4. Open 1_csv_generation.py and run (F5)

**Input Files:**

- 2_Model/{SCE}/ModeloSuelo_{SCE}.xlsx - Main model Excel file with parameter sheets
- 0_Ref/STRUCTURE_OSEMOSYS_*.xlsx - OSeMOSYS structure definition

**Process:**

1. Read Excel sheets containing OSeMOSYS parameters:
   - Sets_Land (YEAR, TECHNOLOGY, FUEL, EMISSION, etc.)
   - AccumulatedAnnualDemand
   - CapitalCost
   - EmissionActivityRatio
   - And 13 more parameter sheets

2. Transform tabular data to long format (CSV)
3. Generate data_land.txt file for GLPK
4. Create consolidated input dataset

**Output Files:**

- ``1_Parameters/{SCE}/*.csv`` - 27 CSV parameter files
- 2_Model/{SCE}/data_land.txt - GLPK-formatted data file
- 2_Model/{SCE}/data_land_{SCE}_Input.csv - Consolidated inputs

Stage 2: Model Execution (2_run_model_mathprog.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Execute the OSeMOSYS optimization model using GLPK solver.

**Running in Spyder:**

Open 2_run_model_mathprog.py in Spyder.

.. important::
   **Run with External Console:** This script runs the GLPK solver and outputs progress to the console. In Spyder's default IPython console, output is not displayed until the entire process finishes. To see real-time progress:

   1. Go to **Run > Configuration per file** (or press Ctrl+F6)
   2. Select **Execute in an external system terminal**
   3. Check **Interact with the Python console after execution**
   4. Click **Run**

   This allows you to monitor solver progress in real-time.

**Input Files:**

- OSeMOSYS_Model.txt - Mathematical model in AMPL format
- 2_Model/{SCE}/data_land.txt - Parameter data from Stage 1

**Process:**

1. For each scenario (BAU, NDP):

   a. Call GLPK solver with command:

   .. code-block:: bash

      glpsol -m OSeMOSYS_Model.txt -d data_land.txt -o output.txt

   b. Parse solver output file
   c. Extract 43 OSeMOSYS decision variables
   d. Generate output CSV dataset

**Output Files:**

- 2_Model/{SCE}/data_land_output.txt - Raw solver output
- 2_Model/{SCE}/data_land_{SCE}_Output.csv - Parsed results

Stage 3: Results Consolidation (3_append.py)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose:** Combine results from all scenarios into unified datasets.

**Running in Spyder:**

Open 3_append.py and run (F5).

**Output Files:**

- 2_Model/data_land_output.csv - All scenario results
- 2_Model/data_land_input.csv - All scenario inputs

Complete Execution
------------------

To run the full MOMF v1 pipeline in Spyder:

1. Open Spyder and navigate to GUA/AFOLU
2. Set the working directory
3. Open and run 1_csv_generation.py (F5)
4. Open and run 2_run_model_mathprog.py (F5)
5. Open and run 3_append.py (F5)

Limitations of v1
-----------------

- Single Excel file per scenario (manual scenario management)
- No parallel execution support
- Limited scenario manipulation capabilities
- No YAML configuration
- Manual results processing required

For more advanced features, consider using :doc:`workflow_v2` or :doc:`workflow_v3`.
