OpenModelsLAC Documentation
===========================

**Open-Source Models for Latin America and the Caribbean**

OpenModelsLAC is a collection of open-source greenhouse gas (GHG) emission models developed for countries in Latin America and the Caribbean. These models cover all IPCC sectors in a single, integrated tool, designed for Nationally Determined Contribution (NDC) updates and Long-Term Strategy (LTS) pathways.

Countries Currently Modeled
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Code
     - Country
     - Sectors Covered
   * - CRI
     - Costa Rica
     - Energy, AFOLU, IPPU, Waste
   * - DOM
     - Dominican Republic
     - Energy, AFOLU, IPPU, Waste
   * - ECU
     - Ecuador
     - Energy, Agriculture, FOLU, IPPU, Waste
   * - GUA
     - Guatemala
     - Energy, AFOLU, IPPU, Waste
   * - HND
     - Honduras
     - Energy, AFOLU
   * - JAM
     - Jamaica
     - AFOLU, Electricity/Building/Industry, Transport, Waste

What is MOMF?
-------------

All models in OpenModelsLAC are built using **MOMF** (Multipurpose OSeMOSYS-based Modeling Framework). MOMF is the underlying framework that enables rapid development and parameterization of OSeMOSYS models.

**The problem:** Energy system models use optimization methods to find least-cost pathways for capacity expansion and energy balances across future scenarios. However, translating real-world energy systems into the mathematical parameters these models require is time-consuming and error-prone—modelers must manually ensure that data is correctly formatted, units are consistent, and relationships between technologies make physical sense.

**The solution:** MOMF lets you define your energy system using intuitive Excel templates focused on physical relationships (e.g., fuel inputs, efficiencies, emissions factors). The framework then automatically generates properly structured OSeMOSYS input files. MOMF can be used in tandem with `MUIO <https://github.com/OSeMOSYS/MUIO>`_ and `otoole <https://otoole.readthedocs.io/>`_.

Why MOMF?
---------

- **Full IPCC sector coverage**: Energy, IPPU, agriculture, LULUCF, waste
- **Policy-ready**: Designed and built for NDC and LTS policy scenario development
- **Multi-solver**: Compatible with all major OSeMOSYS solvers (GLPK, CBC, CPLEX)
- **Open-source**: Freely available under Apache-2.0 license
- **Proven**: Currently implemented for 6 Latin American and Caribbean countries

.. note::
   This documentation covers MOMF versions 1, 2, and 3, which are used across different country models in this repository.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Framework Overview

   overview
   versions
   countries

.. toctree::
   :maxdepth: 2
   :caption: Workflow by Version

   workflow_v1
   workflow_v2
   workflow_v3

.. toctree::
   :maxdepth: 2
   :caption: Tools

   momf_to_muio

.. toctree::
   :maxdepth: 2
   :caption: Reference

   file_reference
   parameters
   glossary


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
