MOMF to MUIO Conversion
=======================

This module enables exporting MOMF scenario models to MUIO (Modelling User Interface for OSeMOSYS) format for visualization and sharing.

Overview
--------

**MOMF** is a scripting-based framework optimized for batch processing multiple scenarios, while **MUIO** provides a graphical user interface for model visualization and interactive exploration. This conversion module bridges both tools.

.. list-table:: MOMF vs MUIO Comparison
   :widths: 25 35 40
   :header-rows: 1

   * - Aspect
     - MOMF
     - MUIO
   * - Type
     - Python script framework
     - Desktop application with UI
   * - Input format
     - Excel + Python scripts
     - Excel workbook
   * - Scenarios
     - Multiple simultaneous
     - Individual
   * - Flexibility
     - High (code-level editing)
     - Medium (guided UI)
   * - Best for
     - Batch analysis, research
     - Teaching, demos, sharing

Prerequisites
-------------

Install otoole (OSeMOSYS Tools for Energy):

.. code-block:: bash

   pip install otoole

otoole is the official OSeMOSYS conversion tool that supports transformations between MathProg datafiles, Excel, and CSV formats.

For more information, see the `otoole documentation <https://otoole.readthedocs.io/>`_.

Module Structure
----------------

.. code-block:: text

   MOMF_to_MUIO/
   ├── momf_to_muio.py      # Main conversion script
   ├── config.yaml          # OSeMOSYS parameter definitions for otoole
   ├── MOMF_models/         # Input folder (MathProg .txt files)
   │   └── BAU_0.txt        # Example: scenario datafile from MOMF
   └── MUIO_models/         # Output folder (Excel .xlsx files)
       └── BAU_0.xlsx       # Converted file for MUIO

Usage
-----

**Step 1: Copy scenario files**

After running a MOMF model (B1 stage), copy the generated MathProg datafiles to the input folder:

.. code-block:: bash

   # Example: copy from CRI/IPPU execution
   cp CRI/IPPU/Executables/BAU_0/BAU_0.txt MOMF_to_MUIO/MOMF_models/

**Step 2: Run the conversion script**

In Spyder, navigate to ``MOMF_to_MUIO/`` and run:

.. code-block:: bash

   python momf_to_muio.py

**Expected output:**

.. code-block:: text

   File modified and saved: BAU_0.txt
   Conversion successful: MUIO_models/BAU_0.xlsx

**Step 3: Open in MUIO**

The generated Excel file can be imported directly into MUIO for visualization and analysis.

How It Works
------------

The script performs two operations:

1. **DiscountRate fix**: MOMF generates MathProg files where ``DiscountRate`` may have only a default value without explicit region assignments. The script adds the required region-value pair:

   .. code-block:: text

      # Before (MOMF output)
      param DiscountRate default 0.05 :=
      ;

      # After (otoole compatible)
      param DiscountRate default 0.05 :=
      CR 0.05
      ;

2. **Format conversion**: Uses otoole to convert MathProg datafile to Excel:

   .. code-block:: bash

      otoole convert datafile excel input.txt output.xlsx config.yaml

Configuration File
------------------

The ``config.yaml`` file defines all OSeMOSYS parameters with their:

- **indices**: Dimensional structure (REGION, TECHNOLOGY, YEAR, etc.)
- **dtype**: Data type (float, int, str)
- **default**: Default value when not specified

This configuration must match the parameters used in your MOMF models. The provided config.yaml covers all standard OSeMOSYS parameters plus result variables.

Batch Conversion
----------------

The script automatically processes all ``.txt`` files in ``MOMF_models/``:

.. code-block:: text

   # Place multiple scenario files
   MOMF_models/
   ├── BAU_0.txt
   ├── NDC_0.txt
   └── LTS_0.txt

   # Run once to convert all
   python momf_to_muio.py

   # Results
   MUIO_models/
   ├── BAU_0.xlsx
   ├── NDC_0.xlsx
   └── LTS_0.xlsx

Troubleshooting
---------------

otoole not found
~~~~~~~~~~~~~~~~

.. code-block:: text

   'otoole' is not recognized as an internal or external command

**Solution:** Install otoole and ensure it's in your PATH:

.. code-block:: bash

   pip install otoole

Parameter not in config
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   KeyError: 'ParameterName' not found in config

**Solution:** Add the missing parameter to ``config.yaml`` with its indices and default value.

Empty output file
~~~~~~~~~~~~~~~~~

If the Excel file is empty or missing sheets, verify that:

1. The input .txt file is a valid MathProg datafile
2. The config.yaml matches your model's parameters
3. The input file uses the correct OSeMOSYS syntax

References
----------

- `otoole Documentation <https://otoole.readthedocs.io/>`_
- `MUIO Documentation <https://muio-modelling-user-interface-for-osemosys.readthedocs.io/>`_
- `MUIO GitHub Repository <https://github.com/OSeMOSYS/MUIO>`_
- `OSeMOSYS Project <http://www.osemosys.org/>`_
