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
   **Before running B1:** You must first parameterize the master YAML configuration file (``MOMF_B1_exp_manager.yaml``). This file controls scenario settings, solver selection, and sector toggles.

Multi-solver support: GLPK, CBC, or CPLEX (configured in the master YAML file).

Operation Modes (generator_or_executor)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``generator_or_executor`` variable in the YAML file controls the B1 script behavior:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Mode
     - Description
   * - ``'None'``
     - Only performs calculations without generating files or executing the solver
   * - ``'Generator'``
     - Calculates, generates input files (.txt), and **executes input validation tests**
   * - ``'Executor'``
     - Performs calculations and executes the solver on existing input files
   * - ``'Both'``
     - Combines Generator and Executor: generates files, runs tests, and executes solver

.. tip::
   Use ``'Generator'`` first to create and validate input files, then ``'Executor'`` to run the model. This allows you to verify inputs before committing to a potentially long solver run.

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

YAML Configuration Reference
----------------------------

The master YAML file (``MOMF_B1_exp_manager.yaml``) contains all configuration variables for the B1 script. Below are the most important variables:

.. warning::
   Only change the **values**, not the variable names. Changing variable names will cause the script to fail.

.. list-table:: Key YAML Variables
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``solver``
     - Solver to use: ``'glpk'``, ``'cbc'``, or ``'cplex'``
   * - ``glpk_option``
     - Post-processing method: ``'old'`` (MOMF native) or ``'new'`` (otoole)
   * - ``del_files``
     - Delete intermediate solver files: ``True`` or ``False``
   * - ``max_x_per_iter``
     - Number of scenarios to run per iteration (recommended: 1-4)
   * - ``generator_or_executor``
     - Operation mode: ``'None'``, ``'Generator'``, ``'Executor'``, or ``'Both'``
   * - ``parallel``
     - Enable parallel execution: ``True`` or ``False``
   * - ``coun_initial``
     - Country/region code (e.g., ``'CR'`` for Costa Rica)
   * - ``disc_rate``
     - Discount rate value (e.g., ``0.05`` for 5%)
   * - ``year_apply_discount_rate``
     - Reference year for discounting costs
   * - ``base_year``
     - Model base year (e.g., ``2015``)
   * - ``final_year``
     - Model final year (e.g., ``2050``)
   * - ``change_year_B1``
     - Year when fleet/technology changes begin

Sector Toggles
~~~~~~~~~~~~~~

Sector toggles allow you to enable or disable specific sectors without modifying the Python code:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``Use_Transport_B1``
     - Enable transport sector module: ``True`` or ``False``
   * - ``Use_Waste_B1``
     - Enable waste sector module: ``True`` or ``False``
   * - ``Use_PIUP_B1``
     - Enable IPPU sector module: ``True`` or ``False``

**Example configuration:**

.. code-block:: yaml

   # Solver selection
   solver: 'glpk'
   glpk_option: 'old'

   # Operation mode
   generator_or_executor: 'Both'
   parallel: True
   max_x_per_iter: 3

   # Sector toggles
   Use_Transport_B1: False
   Use_Waste_B1: False
   Use_PIUP_B1: False

   # Time configuration
   base_year: 2015
   final_year: 2050
   year_apply_discount_rate: 2025
   disc_rate: 0.05

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

Input Validation Tests
----------------------

MOMF v3 includes a routine to test model input data, executed by the script ``test_inputs.py`` located in ``config_plots/``. This aims to reduce the likelihood of the solver failing to find an optimal solution.

.. important::
   Input tests are **automatically executed** when ``generator_or_executor`` is set to ``'Generator'``. They run after generating the input files but before solver execution.

The tests compare model constraints like ``TotalTechnologyAnnualActivityUpperLimit``, ``TotalTechnologyAnnualActivityLowerLimit``, ``TotalAnnualMaxCapacity``, and ``ResidualCapacity``; they also use conversion factors like ``AvailabilityFactor`` and ``CapacityFactor`` to detect discrepancies.

**Output Location:**

Results are stored in ``tests_results/comparison_results_{scenario}_{future}.txt`` (e.g., ``comparison_results_BAU_0.txt``).

Test Descriptions
~~~~~~~~~~~~~~~~~

**Test 1: Technology/Sub-technology Differences**

Compares values of transport technologies with their sub-technologies. Calculates the sum of all sub-technology values and compares with the main technology. Records instances where sub-technologies exceed the main technology's capacity.

**Test 2: Yearly Decrease in Technology Capacity**

Verifies if ``TotalAnnualMaxCapacity`` shows unexpected decreases from one year to the next. Values should generally increase or remain constant over time.

**Test 3: Activity Limit Bounds**

Ensures ``TotalTechnologyAnnualActivityLowerLimit`` does not exceed ``TotalTechnologyAnnualActivityUpperLimit`` for each technology.

**Test 4: Residual vs Maximum Capacity**

Ensures ``ResidualCapacity`` values do not surpass ``TotalAnnualMaxCapacity`` for any technology.

**Test 5: Demand vs Capacity Compatibility**

Verifies that ``SpecifiedAnnualDemand`` is less than ``TotalAnnualMaxCapacity × OutputActivityRatio`` for related technologies. Specific to transport sector.

**Test 6: Demand vs Lower Activity Limits**

Examines whether ``SpecifiedAnnualDemand`` is lower than ``TotalTechnologyAnnualActivityLowerLimit × OutputActivityRatio``. Specific to transport sector.

**Test 7: Activity Limit vs Maximum Capacity**

Checks if ``TotalTechnologyAnnualActivityLowerLimit`` is less than ``TotalAnnualMaxCapacity × CapacityFactor × 31.536``.

**Test 8: Activity Limits with Availability Factor**

Determines if ``TotalTechnologyAnnualActivityLowerLimit`` is below ``TotalAnnualMaxCapacity × CapacityFactor × AvailabilityFactor × 31.536``.

**Test 9: Max Capacity vs Lower Limit**

Ensures ``TotalAnnualMaxCapacity`` values do not fall below ``TotalTechnologyAnnualActivityLowerLimit``. Specific to transport sector.

**Test 10: Sub-technology Capacity Sum**

Confirms that the total ``TotalAnnualMaxCapacity`` of all sub-technologies does not exceed the parent technology's capacity. Specific to transport sector.

**Test 11: AFOLU Activity Upper Limit**

Verifies if the combined ``TotalTechnologyAnnualActivityLowerLimit`` of sub-technologies is greater than the parent technology's ``TotalTechnologyAnnualActivityUpperLimit``. Specific to AFOLU sector.

Advantages over v2
------------------

1. **Externalized Configuration:** All settings in YAML (no code changes needed)
2. **Multi-Solver Support:** Use GLPK, CBC, or CPLEX
3. **Otoole Integration:** Standardized OSeMOSYS data handling
4. **Template System:** Consistent parameter structure
5. **Enhanced Parallelization:** Better resource management
6. **Input Validation Tests:** Automated testing to catch errors before solver execution
