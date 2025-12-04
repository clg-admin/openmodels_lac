MOMF Documentation
===================

**Multipurpose OSeMOSYS-based Modeling Framework**

MOMF is an open-source framework for building national greenhouse gas (GHG) emission models that cover all IPCC sectors in a single, integrated tool. It is designed for NDC updates and Long-Term Strategy (LTS) pathways, and has been applied in Latin America and the Caribbean.

**The problem:** Energy system models use optimization methods to find least-cost pathways for capacity expansion and energy balances across future scenarios. However, translating real-world energy systems into the mathematical parameters these models require is time-consuming and error-prone—modelers must manually ensure that data is correctly formatted, units are consistent, and relationships between technologies make physical sense.

**The solution:** MOMF lets you define your energy system using intuitive Excel templates focused on physical relationships (e.g., fuel inputs, efficiencies, emissions factors). The framework then automatically generates properly structured OSeMOSYS input files. MOMF can be used in tandem with `MUIO <https://github.com/OSeMOSYS/MUIO>`_ and `otoole <https://otoole.readthedocs.io/>`_.

.. note::
   This documentation covers MOMF versions 1, 2, and 3, which are used across different country models in this repository.

Key Features
------------

- **Full IPCC sector coverage**: Energy, IPPU, agriculture, LULUCF, waste
- **Policy-ready**: Designed and built for NDC and LTS policy scenario development
- **Multi-solver**: Compatible with all major OSeMOSYS solvers
- **Open-source**: Freely available under Apache-2.0 license
- **Proven**: Currently implemented for 6 Latin American and Caribbean countries

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
