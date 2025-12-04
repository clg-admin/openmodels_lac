OSeMOSYS Parameters
===================

MOMF uses the standard OSeMOSYS parameter set. This reference documents all parameters, their indices, and default values.

Sets
----

OSeMOSYS models are defined over the following sets:

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Set
     - Symbol
     - Description
   * - REGION
     - r
     - Geographic regions (e.g., GUA, CRI)
   * - YEAR
     - y
     - Model years (e.g., 2021-2050)
   * - TECHNOLOGY
     - t
     - Technologies (power plants, vehicles, processes)
   * - FUEL
     - f
     - Fuels/commodities (electricity, gasoline, CO2)
   * - EMISSION
     - e
     - Emission types (CO2, CH4, N2O)
   * - MODE_OF_OPERATION
     - m
     - Operating modes (typically 1)
   * - TIMESLICE
     - l
     - Time periods within year
   * - SEASON
     - ls
     - Seasons (if sub-annual resolution)
   * - DAYTYPE
     - ld
     - Day types (weekday, weekend)
   * - DAILYTIMEBRACKET
     - lh
     - Hours of day
   * - STORAGE
     - s
     - Storage technologies

Parameters by Category
----------------------

Demand Parameters
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - AccumulatedAnnualDemand
     - r,f,y
     - 0
     - Cumulative demand requirement
   * - SpecifiedAnnualDemand
     - r,f,y
     - 0
     - Annual demand for each fuel [PJ]
   * - SpecifiedDemandProfile
     - r,f,l,y
     - 0
     - Demand distribution across timeslices

Activity Ratios
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - InputActivityRatio
     - r,t,f,m,y
     - 0
     - Fuel input per unit activity
   * - OutputActivityRatio
     - r,t,f,m,y
     - 0
     - Fuel output per unit activity

Capacity Parameters
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - CapacityToActivityUnit
     - r,t
     - 1
     - Converts capacity to activity units
   * - ResidualCapacity
     - r,t,y
     - 0
     - Existing installed capacity
   * - TotalAnnualMaxCapacity
     - r,t,y
     - 99999
     - Maximum installable capacity
   * - TotalAnnualMinCapacity
     - r,t,y
     - 0
     - Minimum required capacity
   * - TotalAnnualMaxCapacityInvestment
     - r,t,y
     - 99999
     - Maximum annual investment
   * - TotalAnnualMinCapacityInvestment
     - r,t,y
     - 0
     - Minimum annual investment

Performance Parameters
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - AvailabilityFactor
     - r,t,y
     - 1
     - Fraction of year available (0-1)
   * - CapacityFactor
     - r,t,l,y
     - 1
     - Capacity utilization factor (0-1)
   * - OperationalLife
     - r,t
     - 1
     - Technology lifetime [years]

Cost Parameters
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - CapitalCost
     - r,t,y
     - 0
     - Investment cost [USD/unit capacity]
   * - FixedCost
     - r,t,y
     - 0
     - Fixed O&M [USD/unit capacity/year]
   * - VariableCost
     - r,t,m,y
     - 0
     - Variable O&M [USD/unit activity]
   * - DiscountRate
     - r
     - 0.05
     - Discount rate (5% default)
   * - DepreciationMethod
     - r
     - 1
     - 1=straight line, 2=sinking fund

Emission Parameters
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - EmissionActivityRatio
     - r,t,e,m,y
     - 0
     - Emissions per unit activity [tCO2/PJ]
   * - EmissionsPenalty
     - r,e,y
     - 0
     - Carbon price [USD/tCO2]
   * - AnnualEmissionLimit
     - r,e,y
     - 99999
     - Annual emission cap
   * - ModelPeriodEmissionLimit
     - r,e
     - 99999
     - Cumulative emission cap
   * - AnnualExogenousEmission
     - r,e,y
     - 0
     - External emissions added to total
   * - ModelPeriodExogenousEmission
     - r,e
     - 0
     - External cumulative emissions

Activity Constraints
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 15 15 30

   * - Parameter
     - Indices
     - Default
     - Description
   * - TotalTechnologyAnnualActivityUpperLimit
     - r,t,y
     - 99999
     - Max annual activity
   * - TotalTechnologyAnnualActivityLowerLimit
     - r,t,y
     - 0
     - Min annual activity
   * - TotalTechnologyModelPeriodActivityUpperLimit
     - r,t
     - 99999
     - Max cumulative activity
   * - TotalTechnologyModelPeriodActivityLowerLimit
     - r,t
     - 0
     - Min cumulative activity

Renewable Energy Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - REMinProductionTarget
     - r,y
     - 0
     - Minimum RE fraction of demand
   * - RETagFuel
     - r,f,y
     - 0
     - 1 if fuel counts as RE demand
   * - RETagTechnology
     - r,t,y
     - 0
     - 1 if technology is renewable

Reserve Margin Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - ReserveMargin
     - r,y
     - 0
     - Required reserve margin
   * - ReserveMarginTagFuel
     - r,f,y
     - 0
     - 1 if fuel requires reserve
   * - ReserveMarginTagTechnology
     - r,t,y
     - 0
     - 1 if tech provides reserve

Storage Parameters
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - CapitalCostStorage
     - r,s,y
     - 0
     - Storage investment cost
   * - OperationalLifeStorage
     - r,s
     - 1
     - Storage lifetime [years]
   * - ResidualStorageCapacity
     - r,s,y
     - 0
     - Existing storage capacity
   * - StorageLevelStart
     - r,s
     - 0
     - Initial storage level
   * - StorageMaxChargeRate
     - r,s
     - 0
     - Max charging rate
   * - StorageMaxDischargeRate
     - r,s
     - 0
     - Max discharging rate
   * - MinStorageCharge
     - r,s,y
     - 0
     - Minimum storage level
   * - TechnologyToStorage
     - r,t,s,m
     - 0
     - Tech-storage charging link
   * - TechnologyFromStorage
     - r,t,s,m
     - 0
     - Tech-storage discharging link

Time Parameters
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - YearSplit
     - l,y
     - 0
     - Fraction of year per timeslice
   * - DaySplit
     - lh,y
     - 0.00137
     - Fraction of day per bracket
   * - DaysInDayType
     - ls,ld,y
     - 7
     - Days per day type
   * - Conversionls
     - l,ls
     - 0
     - Timeslice to season mapping
   * - Conversionld
     - l,ld
     - 0
     - Timeslice to daytype mapping
   * - Conversionlh
     - l,lh
     - 0
     - Timeslice to hour mapping

Trade Parameters
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 35 15 15 35

   * - Parameter
     - Indices
     - Default
     - Description
   * - TradeRoute
     - r,rr,f,y
     - 0
     - 1 if trade allowed between regions

Output Variables
----------------

The solver produces the following output variables:

Capacity Variables
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Variable
     - Description
   * - NewCapacity[r,t,y]
     - New capacity installed
   * - AccumulatedNewCapacity[r,t,y]
     - Cumulative new capacity
   * - TotalCapacityAnnual[r,t,y]
     - Total installed capacity

Activity Variables
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Variable
     - Description
   * - TotalTechnologyAnnualActivity[r,t,y]
     - Total annual activity
   * - ProductionByTechnology[r,l,t,f,y]
     - Production by tech/fuel/timeslice
   * - UseByTechnology[r,l,t,f,y]
     - Fuel use by tech/fuel/timeslice
   * - Demand[r,l,f,y]
     - Demand served by timeslice

Cost Variables
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Variable
     - Description
   * - CapitalInvestment[r,t,y]
     - Annual capital investment
   * - DiscountedCapitalInvestment[r,t,y]
     - NPV of investments
   * - OperatingCost[r,t,y]
     - Total O&M cost
   * - AnnualVariableOperatingCost[r,t,y]
     - Variable O&M cost
   * - AnnualFixedOperatingCost[r,t,y]
     - Fixed O&M cost
   * - DiscountedOperatingCost[r,t,y]
     - NPV of O&M costs
   * - SalvageValue[r,t,y]
     - End-of-horizon salvage value
   * - DiscountedSalvageValue[r,t,y]
     - NPV of salvage
   * - TotalDiscountedCostByTechnology[r,t,y]
     - Total NPV by technology
   * - TotalDiscountedCost[r,y]
     - Total system NPV

Emission Variables
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Variable
     - Description
   * - AnnualTechnologyEmission[r,t,e,y]
     - Emissions by technology
   * - AnnualEmissions[r,e,y]
     - Total emissions by type
   * - AnnualTechnologyEmissionPenaltyByEmission[r,t,e,y]
     - Carbon cost by tech/emission
   * - AnnualTechnologyEmissionsPenalty[r,t,y]
     - Total carbon cost by tech
   * - DiscountedTechnologyEmissionsPenalty[r,t,y]
     - NPV of carbon costs

MOMF-Specific Variables
~~~~~~~~~~~~~~~~~~~~~~~

MOMF adds derived variables for analysis:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Variable
     - Description
   * - Capex{YEAR}
     - Capital costs discounted to reference year
   * - Opex{YEAR}
     - Operating costs discounted to reference year
   * - FixedOpex{YEAR}
     - Fixed O&M discounted
   * - VarOpex{YEAR}
     - Variable O&M discounted
   * - Externalities{YEAR}
     - External costs discounted
   * - Capex_GDP
     - Capital costs as % of GDP
   * - Opex_GDP
     - Operating costs as % of GDP
   * - Fleet
     - Vehicle fleet size (transport)
   * - NewFleet
     - New vehicles added
   * - DistanceDriven
     - Distance traveled
   * - ProducedMobility
     - Mobility produced
