Glossary
========

.. glossary::
   :sorted:

   AFOLU
      Agriculture, Forestry and Other Land Use. One of the four IPCC sectors covering emissions from crops, livestock, land use change, and forestry.

   BAU
      Business As Usual. Baseline scenario representing future emissions without additional climate policies.

   CBC
      COIN-OR Branch and Cut. An open-source linear programming solver alternative to GLPK.

   CLEWs
      Climate, Land, Energy, and Water systems. An integrated modeling approach that MOMF builds upon.

   CPLEX
      IBM's commercial optimization solver. Faster than GLPK for large models but requires a license.

   DDP
      Deep Decarbonization Pathway. Long-term scenario targeting significant emission reductions.

   GLPK
      GNU Linear Programming Kit. The default open-source solver used by MOMF.

   GHG
      Greenhouse Gas. Gases that trap heat in the atmosphere (CO2, CH4, N2O, F-gases).

   IAR
      InputActivityRatio. OSeMOSYS parameter defining fuel input per unit of technology activity.

   IPCC
      Intergovernmental Panel on Climate Change. UN body that provides scientific assessments on climate change.

   IPPU
      Industrial Processes and Product Use. IPCC sector covering emissions from manufacturing and industrial activities.

   LMICs
      Low- and Middle-Income Countries. Target audience for MOMF's open-source approach.

   LTS
      Long-Term Strategy. Climate strategy typically targeting 2050, as required under the Paris Agreement.

   MOMF
      Multipurpose OSeMOSYS-based Modeling Framework. The framework documented in this guide.

   NDC
      Nationally Determined Contribution. Country-level climate commitments under the Paris Agreement.

   NPV
      Net Present Value. Sum of discounted future cash flows.

   OAR
      OutputActivityRatio. OSeMOSYS parameter defining fuel output per unit of technology activity.

   OSeMOSYS
      Open Source Energy Modelling System. The optimization framework underlying MOMF.

   otoole
      OSeMOSYS tools for energy. Python package for OSeMOSYS data management that v3 integrates with.

   PJ
      Petajoule. Energy unit (10^15 joules) commonly used in energy models.

   RES
      Reference Energy System. Diagram showing technology and fuel flows in an energy system.

   Timeslice
      Sub-annual time period used to capture temporal variations in demand and supply.

   v1, v2, v3
      MOMF version designations. v1 is basic, v2 is standard, v3 is advanced.

   YAML
      YAML Ain't Markup Language. Human-readable configuration format used in MOMF v3.

Acronyms
--------

Country Codes
~~~~~~~~~~~~~

- **CRI** - Costa Rica
- **DOM** - Dominican Republic
- **ECU** - Ecuador
- **GUA** - Guatemala
- **HND** - Honduras
- **JAM** - Jamaica

Sector Codes
~~~~~~~~~~~~

- **Energy** - Energy sector (electricity, transport, buildings, industry)
- **AFOLU** - Agriculture, Forestry and Other Land Use
- **IPPU** - Industrial Processes and Product Use
- **Waste** - Waste management sector
- **FOLU** - Forestry and Other Land Use (ECU specific)

Common Technology Prefixes
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **PP** - Power Plant
- **TR** - Transport
- **TRN** - Transport (alternative)
- **DIST** - Distribution
- **PROD** - Production
- **AG** - Agriculture
- **GA** - Livestock (Ganadería)
- **LU** - Land Use

Common Fuel Prefixes
~~~~~~~~~~~~~~~~~~~~

- **DEM** - Demand
- **ELE** - Electricity
- **DSL** - Diesel
- **GSL** - Gasoline
- **NGV** - Natural Gas Vehicle
- **HYD** - Hydrogen
- **BIO** - Biofuel

Emission Codes
~~~~~~~~~~~~~~

- **CO2** - Carbon Dioxide
- **CO2e** - Carbon Dioxide Equivalent
- **CH4** - Methane
- **N2O** - Nitrous Oxide

Units
-----

Energy
~~~~~~

- **PJ** - Petajoule (10^15 J)
- **TJ** - Terajoule (10^12 J)
- **GWh** - Gigawatt-hour
- **ktoe** - Kilotonnes of oil equivalent

Emissions
~~~~~~~~~

- **MtCO2e** - Megatonnes CO2 equivalent
- **ktCO2e** - Kilotonnes CO2 equivalent
- **tCO2e** - Tonnes CO2 equivalent
- **GgCO2e** - Gigagrams CO2 equivalent

Capacity
~~~~~~~~

- **GW** - Gigawatt
- **MW** - Megawatt
- **kW** - Kilowatt
- **units** - Generic capacity units (vehicles, plants)

Cost
~~~~

- **USD** - US Dollars
- **USD/kW** - Dollars per kilowatt (capital cost)
- **USD/GJ** - Dollars per gigajoule (fuel cost)
- **%GDP** - Percentage of Gross Domestic Product

Time
~~~~

- **years** - Model years
- **annual** - Single timeslice (full year)
