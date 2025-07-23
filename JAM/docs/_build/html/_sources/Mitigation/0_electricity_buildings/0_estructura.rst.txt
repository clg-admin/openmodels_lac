===================================
Model Structure
===================================

The OSeMOSYS model represents the main components of the electricity and building systems,
covering the flow from fuel imports and electricity generation to energy demand. It is a flexible,
open-source tool that promotes transparent use of open data and easy model transferability. Additionally,
the transport sector is included due to its strong connection with the energy system. **Figura 3** shows the structure of the model
and elements represented on the sectoral model.

.. figure:: ../_static/_images/3_estructuraenergia.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figure 3:** Key elements represented for the Electricity and Buildings sectors



**Technologies**

.. list-table:: **Table 1.** Technologies and Descriptions
   :header-rows: 1
   :widths: 20 80

   * - **Tech**
     - **Description**
   * - DIST_DSL
     - Primary – Import/Distribution – Diesel
   * - DIST_GSL
     - Primary – Import/Distribution – Gasoline
   * - DIST_NGS
     - Primary – Import/Distribution – Natural Gas
   * - DIST_LPG
     - Primary – Import/Distribution – LPG
   * - DIST_COK
     - Primary – Import/Distribution – Coke
   * - DIST_KER
     - Primary – Import/Distribution – Kerosene
   * - DIST_JET
     - Primary – Import/Distribution – Jet
   * - DIST_FIR
     - Primary – Production – Firewood
   * - DIST_CHA
     - Primary – Production – Charcoal
   * - DIST_BIM
     - Primary – Production – Biomass
   * - DIST_BGS
     - Primary – Production – Biogas
   * - DIST_OPE
     - Primary – Import/Distribution – Other Products
   * - EXTT_CRU
     - Primary Extraction/Transformation – Crude
   * - DIST_COA
     - Primary – Import/Distribution – Coal
   * - DIST_PV
     - Primary – Solar Energy
   * - DIST_FOI
     - Primary – Import/Distribution – Fuel Oil
   * - PPHDAM
     - Primary – Transformation – Hydro Dam
   * - PPHROR
     - Primary – Transformation – Hydro ROR
   * - PPGEO
     - Primary – Transformation – Geothermal
   * - PPWNDON
     - Primary – Transformation – Wind
   * - PPWNDONS
     - Primary – Transformation – Wind with Battery Storage
   * - PPWNDOFF
     - Primary – Transformation – Wind Offshore
   * - PPPVT
     - Primary – Transformation – Transmission Solar
   * - PPPVTS
     - Primary – Transformation – Transmission Solar with battery storage
   * - PPPVD
     - Primary – Transformation – Distributed Solar
   * - PPPVDS
     - Primary – Transformation – Distributed Solar with battery storage
   * - ELE_TRANS
     - Secondary - Power Transmission
   * - ELE_DIST
     - Secondary - Power Distribution
   * - HYD_G_PROD
     - Secondary - Green Hydrogen Production
   * - HYD_DIST
     - Secondary - Distribution of Hydrogen
   * - STOELE
     - Secondary - Storage/Batteries
   * - PPBIM
     - Secondary - Power Plant - Biomass
   * - PPBGS
     - Secondary - Power Plant - Biogas
   * - PPNGS
     - Secondary - Power Plant - Natural Gas
   * - PPDSL
     - Secondary - Power Plant - Diesel
   * - PPFOI
     - Secondary - Power Plant - Fuel Oil
   * - REF_DSL
     - Secondary - Diesel Refinery
   * - REF_GSL
     - Secondary - Gasoline Refinery
   * - REF_LPG
     - Secondary - LPG Refinery
   * - REF_FOI
     - Secondary - Fuel Oil Refinery
   * - REF_JET
     - Secondary - Jet Oil Refinery
   * - REF_OPE
     - Secondary - Other Products Refinery
   * - T5ELECOM
     - Demand Electric for Commercial
   * - T5ELERES
     - Demand Electric for Residential
   * - T5ELETMA
     - Demand Electric for Transport - Maritime
   * - T5ELETRO
     - Demand Electric for Transport - Road
   * - T5DSLEXP
     - Demand Diesel for Exports
   * - T5JETEXP
     - Demand Jet Fuel and others for Exports
   * - T5FOIEXP
     - Demand Fuel Oil for Exports

