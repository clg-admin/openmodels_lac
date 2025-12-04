Version Comparison
==================

MOMF has evolved through three major versions, each adding capabilities while maintaining backward compatibility with the core OSeMOSYS workflow.

Version Summary
---------------

.. list-table::
   :header-rows: 1
   :widths: 15 28 28 29

   * - Feature
     - v1 (Basic)
     - v2 (Standard)
     - v3 (Advanced)
   * - **Pipeline**
     - 3 scripts
     - 4 stages (A1->A2->B1->B2)
     - 4 stages + scenario creator
   * - **Configuration**
     - Hardcoded
     - Excel-based
     - YAML-based
   * - **Input Files**
     - Single Excel
     - Multiple Excel
     - Excel + YAML + Templates
   * - **Parallel Execution**
     - No
     - Yes
     - Yes (enhanced)
   * - **Solvers**
     - GLPK only
     - GLPK only
     - GLPK, CBC, CPLEX
   * - **Scenario Management**
     - Manual
     - Excel config
     - YAML config
   * - **Otoole Integration**
     - No
     - No
     - Yes

Version Details
---------------

Version 1: Basic
~~~~~~~~~~~~~~~~

**Best for:** Simple models, learning, quick prototyping

**Characteristics:**

- Minimal setup required
- Single Excel file contains all model data
- Direct GLPK execution
- Manual scenario management
- Straightforward 3-script workflow

**Scripts:**

1. 1_csv_generation.py - Generate parameters
2. 2_run_model_mathprog.py - Run solver
3. 3_append.py - Consolidate results

**Used in:**

- GUA/AFOLU

Version 2: Standard
~~~~~~~~~~~~~~~~~~~

**Best for:** Production models, multi-scenario analysis

**Characteristics:**

- Modular input structure
- Automatic projection calculations
- Parallel scenario execution
- Enhanced output processing
- GDP-normalized cost outputs

**Scripts:**

1. A1_Model_Structure.py - Build model structure
2. A2_Compiler.py - Compile parameters
3. B1_Base_Scenarios_Adj_Parallel.py - Run scenarios
4. B2_Results_Creator_f0.py - Extract results

**Used in:**

- CRI: IPPU, Waste
- DOM: Energy, AFOLU, IPPU, Waste
- ECU: Energy, Agriculture, FOLU, IPPU, Waste
- GUA: Energy, IPPU, Waste
- HND: Energy, AFOLU
- JAM: All sectors

Version 3: Advanced
~~~~~~~~~~~~~~~~~~~

**Best for:** Research, uncertainty analysis, complex scenarios

**Characteristics:**

- YAML-based configuration
- Scenario creator (MOMF_T1_A.yaml)
- Multiple solver support
- Otoole integration
- Template-based parameter definition

**Additional Components:**

- MOMF_T1_A.yaml - Configuration for A1 and A2 scripts
- MOMF_B1_exp_manager.yaml - Master configuration
- config/templates/ - Parameter templates
- conversion_format.yaml - Otoole config

**Used in:**

- CRI: Energy, AFOLU

Choosing a Version
------------------

Use **v1** when:

- Building a simple proof-of-concept
- Learning MOMF/OSeMOSYS
- Working with a single scenario
- Quick analysis is needed

Use **v2** when:

- Running production models
- Multiple scenarios are needed
- Parallel execution is beneficial
- Standard sector modeling

Use **v3** when:

- Complex configuration is needed
- Multiple solvers may be used
- Uncertainty analysis is required
- Integration with otoole ecosystem

Migration Path
--------------

**v1 -> v2:**

1. Split single Excel into multiple input files
2. Rename scripts to A1/A2/B1/B2 convention
3. Add B1_Scenario_Config.xlsx
4. Update paths and imports

**v2 -> v3:**

1. Create ndc_{country}_{year} folder structure
2. Create YAML configuration files
3. Move files to t1_confection
4. Create CSV templates
5. Update scripts to read YAML
6. Add otoole config (optional)
