Installation
============

This guide covers the installation of MOMF and its dependencies on Windows.

System Requirements
-------------------

- Windows 10 or higher
- Python 3.8 or higher
- GLPK solver (GNU Linear Programming Kit)
- Spyder IDE (recommended)
- Git (for version control)

Installing Python and Spyder
----------------------------

We recommend using Anaconda or installing Spyder directly:

**Option 1: Anaconda (Recommended)**

1. Download Anaconda from https://www.anaconda.com/download
2. Install Anaconda (includes Python and Spyder)
3. Open Spyder from the Start Menu or Anaconda Navigator

**Option 2: Standalone Spyder**

1. Install Python from https://www.python.org/downloads/
2. Install Spyder:

.. code-block:: bash

   pip install spyder

3. Launch Spyder from the Start Menu

Installing Python Dependencies
------------------------------

Open a command prompt or Anaconda Prompt and install the required packages:

.. code-block:: bash

   pip install pandas numpy openpyxl xlrd xlsxwriter PyYAML matplotlib numpy-financial

Required Python Packages
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   pandas>=1.3.0
   numpy>=1.20.0
   openpyxl>=3.0.0
   xlrd>=2.0.0
   xlsxwriter>=3.0.0
   PyYAML>=6.0
   matplotlib>=3.4.0
   numpy-financial>=1.0.0

Installing GLPK Solver
----------------------

GLPK is required to solve the OSeMOSYS optimization models.

1. Download GLPK for Windows from https://sourceforge.net/projects/winglpk/
2. Extract to a directory (e.g., ``C:\glpk``)
3. Add the ``w64`` folder to your system PATH:

   - Press ``Win + X`` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select ``Path``, then click "Edit"
   - Click "New" and add ``C:\glpk\w64`` (or your installation path)
   - Click "OK" on all dialogs

4. Open a new command prompt and verify installation:

.. code-block:: bash

   glpsol --version

You should see the GLPK version information.

Alternative Solvers (v3 only)
-----------------------------

MOMF v3 also supports other solvers:

CBC (COIN-OR Branch and Cut)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download from https://github.com/coin-or/Cbc/releases and add to PATH.

CPLEX (Commercial)
~~~~~~~~~~~~~~~~~~

CPLEX requires a license from IBM. Academic licenses are available for free.

1. Download from IBM Academic Initiative
2. Follow IBM's installation instructions
3. Add CPLEX to your system PATH

Verifying Installation
----------------------

Open a command prompt and run:

.. code-block:: bash

   # Check Python version
   python --version

   # Check GLPK
   glpsol --version

   # Check Python packages
   python -c "import pandas; import numpy; import openpyxl; print('All packages installed successfully')"

Cloning the Repository
----------------------

.. code-block:: bash

   git clone https://github.com/clg-admin/openmodels_lac.git
   cd openmodels_lac

Directory Structure
-------------------

After cloning, you will see the following structure:

.. code-block:: text

   openmodels_lac/
   ├── CRI/          # Costa Rica models
   ├── DOM/          # Dominican Republic models
   ├── ECU/          # Ecuador models
   ├── GUA/          # Guatemala models
   ├── HND/          # Honduras models
   ├── JAM/          # Jamaica models
   ├── docs/         # Documentation
   └── README.md

Each country folder contains sector-specific models (Energy, AFOLU, IPPU, Waste).

Configuring Spyder
------------------

1. Open Spyder
2. Go to **Tools > Preferences > Current working directory**
3. Set the working directory to the model folder you want to run
4. Alternatively, use the file browser panel to navigate to the model folder

Troubleshooting
---------------

GLPK Not Found
~~~~~~~~~~~~~~

If you get "glpsol: command not found":

1. Verify GLPK is installed in ``C:\glpk\w64``
2. Check that the path is correctly added to system PATH
3. Open a **new** command prompt (PATH changes require a new session)
4. If using Spyder, restart Spyder after adding to PATH

Python Package Errors
~~~~~~~~~~~~~~~~~~~~~

If you encounter package conflicts:

.. code-block:: bash

   # Upgrade pip first
   python -m pip install --upgrade pip

   # Install packages one by one
   pip install pandas
   pip install numpy
   pip install openpyxl xlrd xlsxwriter
   pip install PyYAML matplotlib numpy-financial

Excel File Errors
~~~~~~~~~~~~~~~~~

If you get errors reading Excel files:

.. code-block:: bash

   pip install openpyxl xlrd --upgrade

Spyder Not Finding Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

If Spyder cannot find installed packages:

1. Check that Spyder is using the correct Python interpreter
2. Go to **Tools > Preferences > Python interpreter**
3. Select the Python installation where you installed the packages
