OpenModelsLAC Documentation
===========================

**Open-Source Models for Latin America and the Caribbean**

OpenModelsLAC is a collection of open-source greenhouse gas (GHG) emission models developed for countries in Latin America and the Caribbean. These models cover all IPCC sectors in a single, integrated tool, designed for Nationally Determined Contribution (NDC) updates and Long-Term Strategy (LTS) pathways.

All models are built using the **MOMF** (Multipurpose OSeMOSYS-based Modeling Framework), which enables rapid development and parameterization of OSeMOSYS models. See :doc:`overview` for details about the framework.

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

Key Features
------------

- **Full IPCC sector coverage**: Energy, IPPU, Agriculture, LULUCF, Waste
- **Policy-ready**: Designed for NDC and Long-Term Strategy (LTS) development
- **Multi-solver**: Compatible with GLPK, CBC, and CPLEX
- **Open-source**: Freely available under Apache-2.0 license
- **Reproducible**: Documented workflows for model replication and updates

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
