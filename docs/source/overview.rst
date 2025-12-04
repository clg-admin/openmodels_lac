Framework Overview
==================

What is MOMF?
-------------

**MOMF (Multipurpose OSeMOSYS-based Modeling Framework)** is an open-source framework for building national greenhouse gas (GHG) emission models that cover all IPCC sectors in a single, integrated tool.

**The problem:** Energy system models use optimization methods to find least-cost pathways for capacity expansion and energy balances across future scenarios. However, translating real-world energy systems into the mathematical parameters these models require is time-consuming and error-prone—modelers must manually ensure that data is correctly formatted, units are consistent, and relationships between technologies make physical sense.

**The solution:** MOMF lets you define your energy system using intuitive Excel templates focused on physical relationships (e.g., fuel inputs, efficiencies, emissions factors). The framework then automatically generates properly structured OSeMOSYS input files. MOMF can be used in tandem with `MUIO <https://github.com/OSeMOSYS/MUIO>`_ and `otoole <https://otoole.readthedocs.io/>`_.

**Key features:**

- Full IPCC sector coverage (energy, IPPU, agriculture, LULUCF, waste)
- Designed and built for NDC and LTS policy scenario development
- Compatible with all major OSeMOSYS solvers
- Open-source and freely available

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
