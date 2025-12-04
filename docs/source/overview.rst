Framework Overview
==================

What is MOMF?
-------------

**MOMF (Multipurpose OSeMOSYS-based Modeling Framework)** is an open-source framework designed for building comprehensive national greenhouse gas (GHG) emission models.

Energy system modeling tools typically use linear and/or non-linear optimization methods to determine least-cost capacity mixes and energy balances across modeled time horizons for given climate and development scenarios. This means that both a reference energy system and alternative scenarios' changes and their expected costs must be expressed through various mathematical parameters that the model uses to configure and calculate the modeled energy system.

MOMF is designed to solve this problem by introducing a programmatic modeling framework that lets the modeler focus on the physics of the energy system through intuitive Excel-based templates, while pre-processing this information into consistent, correctly formatted, dimensionally aligned, and semantically coherent OSeMOSYS model runs that can be used with any of the current solvers available.

MOMF addresses a critical gap in existing modeling tools by providing:

1. **Full IPCC sector coverage** in a single, integrated framework
2. **Direct calibration** to national GHG inventories
3. **Support for both NDC and LTS** policy planning
4. **Open-source accessibility** for Low- and Middle-Income Countries (LMICs)

Why MOMF?
---------

Existing national-level integrated assessment models often face significant limitations:

.. list-table:: Gaps in Existing Tools
   :header-rows: 1
   :widths: 40 60

   * - Gap
     - MOMF Solution
   * - Most models focus only on Energy sector
     - MOMF covers all four IPCC sectors (Energy, AFOLU, IPPU, Waste)
   * - Waste and IPPU are often missing or aggregated
     - Each sector has dedicated, detailed modeling
   * - Models rarely calibrate to national inventories
     - MOMF is designed for direct inventory calibration
   * - Few open-source options for LMICs
     - Fully open-source with documented workflows
   * - Limited support for both NDC and LTS
     - Built for both short-term (NDC) and long-term (LTS) planning

Core Components
---------------

OSeMOSYS Foundation
~~~~~~~~~~~~~~~~~~~

MOMF is built on `OSeMOSYS <http://www.osemosys.org/>`_ (Open Source Energy Modelling System), a linear programming optimization framework. OSeMOSYS provides:

- Technology-based representation of energy systems
- Multi-period optimization (typically 2020-2050)
- Flexibility to model different sectors
- Mathematical formulation in AMPL/GLPK format

IPCC Sectors Modeled
~~~~~~~~~~~~~~~~~~~~

.. list-table:: IPCC Sectors in MOMF
   :header-rows: 1
   :widths: 20 30 50

   * - Sector
     - Code
     - Description
   * - Energy
     - Energy
     - Electricity generation, transport, industry, buildings
   * - Agriculture, Forestry and Other Land Use
     - AFOLU
     - Crops, livestock, land use change, forestry
   * - Industrial Processes and Product Use
     - IPPU
     - Cement, chemicals, metals, F-gases
   * - Waste
     - Waste
     - Solid waste, wastewater, incineration

Framework Versions
------------------

MOMF has evolved through three main versions:

.. list-table:: MOMF Versions
   :header-rows: 1
   :widths: 15 25 60

   * - Version
     - Complexity
     - Characteristics
   * - v1
     - Basic
     - Simple 3-script pipeline, single Excel input, direct GLPK execution
   * - v2
     - Standard
     - 4-stage pipeline (A1->A2->B1->B2), multiple Excel inputs, parallel execution
   * - v3
     - Advanced
     - YAML configuration, scenario creator, multiple solver support, otoole integration

See :doc:`versions` for detailed version comparison.

Modeling Approach
-----------------

Technology Representation
~~~~~~~~~~~~~~~~~~~~~~~~~

MOMF uses a **Reference Energy System (RES)** approach where:

- **Technologies** transform inputs to outputs (e.g., power plants, vehicles, industrial processes)
- **Fuels/Commodities** flow between technologies (e.g., electricity, gasoline, CO2)
- **Emissions** are linked to technology activities

Scenario Framework
~~~~~~~~~~~~~~~~~~

Models typically include multiple scenarios:

- **BAU (Business as Usual)**: Baseline trajectory without additional policies
- **NDC**: Nationally Determined Contribution targets
- **LTS/DDP**: Long-Term Strategy / Deep Decarbonization Pathway

Key Parameters
~~~~~~~~~~~~~~

OSeMOSYS uses ~50 parameters to define the model. Key ones include:

.. list-table:: Core OSeMOSYS Parameters
   :header-rows: 1
   :widths: 35 65

   * - Parameter
     - Description
   * - SpecifiedAnnualDemand
     - Final energy/service demand by fuel
   * - InputActivityRatio
     - Input fuel requirement per unit of activity
   * - OutputActivityRatio
     - Output fuel production per unit of activity
   * - CapitalCost
     - Investment cost per unit of capacity
   * - FixedCost
     - Annual fixed O&M cost per unit of capacity
   * - VariableCost
     - Variable O&M cost per unit of activity
   * - EmissionActivityRatio
     - Emissions per unit of technology activity
   * - ResidualCapacity
     - Existing installed capacity
   * - TotalAnnualMaxCapacity
     - Upper limit on installed capacity
   * - OperationalLife
     - Lifetime of technology in years

Workflow Overview
-----------------

All MOMF versions follow a similar conceptual workflow:

.. code-block:: text

   INPUT DATA     ->  Excel files with technology/fuel definitions,
   (Excel)            costs, efficiencies, demands, emissions
        |
        v
   CSV GENERATION ->  Python scripts transform Excel data
   (Python)           to OSeMOSYS-compatible CSV parameters
        |
        v
   OPTIMIZATION   ->  GLPK/CBC/CPLEX solves the
   (Solver)           linear programming model
        |
        v
   RESULTS        ->  Consolidate outputs across
   PROCESSING         scenarios into analysis-ready CSVs

Country Applications
--------------------

MOMF is currently implemented for:

- **CRI** - Costa Rica
- **DOM** - Dominican Republic
- **ECU** - Ecuador
- **GUA** - Guatemala
- **HND** - Honduras
- **JAM** - Jamaica

Each country model can be customized for local:

- Technology mixes
- Cost structures
- Emission factors
- Policy scenarios
- Temporal resolution

See :doc:`countries` for country-specific details.
