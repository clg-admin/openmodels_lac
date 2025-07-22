===================================
Model Structure
===================================

This part of the model primarily relies on national data, including energy balances,
fuel prices published annually by the Office of Utilities Regulation and the annual production figures for products like cement.
**Figure 6** highlights aspects of cement production, relevant to model the clinker-to-cement ratio reduction targeted by the LTS.

.. figure:: ../_static/_images/6_estructuraindus.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figure 6:** Key elements represented in cement production.


**Technologies**
.. list-table:: **Table 5.** Industry and IPPU Sector Technologies
   :widths: 15 20 20 45
   :header-rows: 1

   * - **Sector**
     - **Subsector**
     - **Technology**
     - **Description**
   * - Industry
     - Cement production
     - T5DSLINDCEM
     - Demand Diesel for Industrial - Cement
   * - Industry
     - Cement production
     - T5GSLINDCEM
     - Demand Gasoline for Industrial - Cement
   * - Industry
     - Cement production
     - T5NGSINDCEM
     - Demand Natural Gas for Industrial - Cement
   * - Industry
     - Cement production
     - T5ELEINDCEM
     - Demand Electric for Industrial - Cement
   * - Industry
     - Cement production
     - T5HYDINDCEM
     - Demand Hydrogen for Industrial - Cement
   * - Industry
     - Cement production
     - T5COKINDCEM
     - Demand Coke for Industrial - Cement
   * - Industry
     - Cement production
     - T5BIMINDCEM
     - Demand Biomass for Industrial - Cement
   * - Industry
     - Cement production
     - T5COAINDCEM
     - Demand Coal for Industrial - Cement
   * - Industry
     - Cement production
     - T5FOIINDCEM
     - Demand Fuel Oil for Industrial - Cement
   * - IPPU
     - Cement production process
     - RAW_MAT_CLK
     - Supply of raw material for clinker
   * - IPPU
     - Cement production process
     - PROD_CLK_TRAD
     - Traditional clinker production
   * - IPPU
     - Lime
     - LIME
     - Lime production
   * - IPPU
     - HFCs
     - IMP_R32
     - R32
   * - IPPU
     - HFCs
     - T5R32IPPU
     - Demand R32 for Industrial Processes
   * - Industry
     - Construction
     - T5DSLCON
     - Demand Diesel for Construction
   * - Industry
     - Industry
     - CCS_FLO
     - Floating Carbon Capture and Storage


