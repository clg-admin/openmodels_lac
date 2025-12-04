Quickstart Guide
================

This guide walks you through running your first MOMF model.

Prerequisites
-------------

Before starting, ensure you have:

1. Python 3.8+ installed
2. GLPK solver installed (see :doc:`installation`)
3. Required Python packages installed
4. The repository cloned locally
5. Spyder IDE installed (recommended)

Quick Setup
-----------

1. Clone the repository:

.. code-block:: bash

   git clone https://github.com/clg-admin/openmodels_lac.git

2. Install Python dependencies:

.. code-block:: bash

   pip install pandas numpy openpyxl xlrd xlsxwriter PyYAML matplotlib numpy-financial

Running Your First Model
------------------------

We'll run the Guatemala IPPU model (v2 workflow) as an example.

**Using Spyder (Recommended):**

1. Open Spyder
2. Navigate to the model folder using the File Browser panel: ``GUA/IPPU``
3. Set the working directory to this folder (right-click > Set as current working directory)
4. Open and run each script in order

**Step 1: Run Stage A1 (Model Structure)**

Open ``A1_Model_Structure.py`` in Spyder and run it (F5 or Run button).

.. warning::
   **A1_Model_Structure.py should only be run when creating a new model from scratch.** Running this script will overwrite any existing parameterization in the A1_Outputs folder. For existing models, skip directly to A2_Compiler.py.

**Expected output:**

.. code-block:: text

   Reading demand classifiers...
   Reading supply classifiers...
   Building activity ratios...
   Generating base year model...
   Done.

**Generated files:**

- ``A1_Outputs/A-O_AR_Model_Base_Year.xlsx``
- ``A1_Outputs/A-O_AR_Projections.xlsx``
- ``A1_Outputs/A-O_Demand.xlsx``
- ``A1_Outputs/A-O_Parametrization.xlsx``

**Step 2: Run Stage A2 (Parameter Compiler)**

Open ``A2_Compiler.py`` in Spyder and run it.

**Expected output:**

.. code-block:: text

   Flat
   Flat
   User defined
   ...
   X.XX seconds / X.XX minutes
   *: For all effects, we have finished the processing tasks...
   *: We just finished the printing of the results.

**Generated files:**

- ``A2_Output_Params/BAU/*.csv`` (20+ parameter files)
- ``A1_Outputs/*_COMPLETED.xlsx``
- ``A2_Structure_Lists.xlsx``

**Step 3: Manual Step - Copy Parameters**

.. important::
   After running A2_Compiler.py, you must manually copy the scenario folders from ``A2_Output_Params/`` to ``B1_Output_Params/``. This step prepares the parameters for the scenario execution stage.

   For example, copy the ``BAU`` folder from ``A2_Output_Params/BAU/`` to ``B1_Output_Params/BAU/``.

**Step 4: Run Stage B1 (Scenario Execution)**

Open ``B1_Base_Scenarios_Adj_Parallel.py`` in Spyder.

.. important::
   **Run with External Console:** This script runs the GLPK solver and outputs progress to the console. In Spyder's default IPython console, output is not displayed until the entire process finishes. To see real-time progress:

   1. Go to **Run > Configuration per file** (or press Ctrl+F6)
   2. Select **Execute in an external system terminal**
   3. Check **Interact with the Python console after execution**
   4. Click **Run**

   This allows you to monitor solver progress in real-time.

**Expected output:**

.. code-block:: text

   Processing scenario BAU...
   Executing GLPK solver...
   glpsol -m OSeMOSYS_Model.txt -d ...
   Model has been successfully processed
   ...

This step may take several minutes depending on model size.

**Generated files:**

- ``Executables/BAU_0/BAU_0.txt``
- ``Executables/BAU_0/BAU_0_Input.csv``
- ``Executables/BAU_0/BAU_0_Output.csv``
- ``B1_Output_Params/BAU/*.csv``

**Step 5: Run Stage B2 (Results Extraction)**

Open ``B2_Results_Creator_f0.py`` in Spyder and run it.

**Generated files:**

- ``Executables/f0_OSMOSYS_{COUNTRY}_Output.csv`` - Consolidated output results
- ``Executables/f0_OSMOSYS_{COUNTRY}_Output_{DATE}.csv`` - Dated backup of output
- ``Executables/f0_OSMOSYS_{COUNTRY}_Input.csv`` - Consolidated input data
- ``Executables/f0_OSMOSYS_{COUNTRY}_Input_{DATE}.csv`` - Dated backup of input

**Step 6: View Results**

Open the results file in Spyder or Excel:

.. code-block:: python

   import pandas as pd
   results = pd.read_csv('Executables/f0_OSMOSYS_GUA_Output.csv')
   print(results.head())
   print(results.columns.tolist())

Key output columns:

- ``Strategy`` - Scenario name (BAU)
- ``Technology`` - Technology code
- ``Year`` - Model year
- ``AnnualTechnologyEmission`` - GHG emissions
- ``TotalCapacityAnnual`` - Installed capacity
- ``CapitalInvestment`` - Investment costs

Quick Analysis Example
----------------------

.. code-block:: python

   import pandas as pd
   import matplotlib.pyplot as plt

   # Load results
   df = pd.read_csv('Executables/f0_OSMOSYS_GUA_Output.csv')

   # Total emissions by scenario and year
   emissions = df.groupby(['Strategy', 'Year'])['AnnualTechnologyEmission'].sum().reset_index()

   # Plot
   for scenario in emissions['Strategy'].unique():
       data = emissions[emissions['Strategy'] == scenario]
       plt.plot(data['Year'], data['AnnualTechnologyEmission'], label=scenario)

   plt.xlabel('Year')
   plt.ylabel('Emissions (Mt CO2e)')
   plt.title('GHG Emissions by Scenario')
   plt.legend()
   plt.savefig('emissions_comparison.png')
   plt.show()

Trying Different Models
-----------------------

v1 Example (GUA/AFOLU)
~~~~~~~~~~~~~~~~~~~~~~

In Spyder, navigate to ``GUA/AFOLU`` and run the scripts in order:

1. Open and run ``1_csv_generation.py``

   This script reads the Excel model file and generates CSV parameters and GLPK data files for each scenario.

2. Open and run ``2_run_model_mathprog.py``

   This script executes the GLPK solver for all scenarios, parsing the output into structured CSV results.

3. Open and run ``3_append.py``

   This script consolidates results from all scenarios into unified datasets for analysis.

**Generated files:**

- ``1_Parameters/{SCE}/*.csv`` - Parameter CSV files
- ``2_Model/{SCE}/data_land.txt`` - GLPK data file
- ``2_Model/{SCE}/data_land_{SCE}_Input.csv`` - Consolidated inputs
- ``2_Model/{SCE}/data_land_{SCE}_Output.csv`` - Consolidated outputs
- ``2_Model/data_land_output.csv`` - All scenarios combined

v3 Example (CRI/Energy)
~~~~~~~~~~~~~~~~~~~~~~~

In Spyder, navigate to ``CRI/Energy/ndc_cr_30/t1_confection`` and run the scripts in order:

1. Open and run ``A1_Model_Structure.py`` (only for new models)
2. Open and run ``A2_Compiler.py``
3. Copy scenario folders from ``A2_Output_Params/`` to ``B1_Output_Params/``
4. Open and run ``B1_Base_Scenarios_Adj_Parallel.py``
5. Open and run ``B2_Results_Creator_f0.py``

Common Issues
-------------

GLPK Not Found
~~~~~~~~~~~~~~

.. code-block:: text

   'glpsol' is not recognized as an internal or external command

**Solution:** Add GLPK to your system PATH (see :doc:`installation`). After updating PATH, restart Spyder.

Missing Python Package
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ModuleNotFoundError: No module named 'pandas'

**Solution:** Install missing package:

.. code-block:: bash

   pip install pandas

Excel File Error
~~~~~~~~~~~~~~~~

.. code-block:: text

   xlrd.biffh.XLRDError: Excel xlsx file; not supported

**Solution:** Update packages:

.. code-block:: bash

   pip install openpyxl xlrd --upgrade

Memory Error
~~~~~~~~~~~~

For large models, increase available memory or reduce parallel workers in B1 script:

.. code-block:: python

   max_x_per_iter = 2  # Reduce from default 4

Next Steps
----------

After completing this quickstart:

1. Read the :doc:`overview` to understand MOMF architecture
2. Explore :doc:`versions` to understand version differences
3. Check :doc:`countries` for available models
4. Review workflow documentation for your version:

   - :doc:`workflow_v1`
   - :doc:`workflow_v2`
   - :doc:`workflow_v3`

5. Modify input Excel files to customize the model
6. Create new scenarios in configuration files
