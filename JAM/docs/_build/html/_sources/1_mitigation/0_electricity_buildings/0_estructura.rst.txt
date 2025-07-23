===================================
Model Structure
===================================

The OSeMOSYS model represents the main components of the electricity and building systems,
covering the flow from fuel imports and electricity generation to energy demand. It is a flexible,
open-source tool that promotes transparent use of open data and easy model transferability. Additionally,
the transport sector is included due to its strong connection with the energy system. **Figura 3** shows the structure of the model
and elements represented on the sectoral model.

.. figure:: ../../_static/_images/3_estructuraenergia.png
   :alt: Models used on the cost and benefits analysis
   :width: 100%
   :align: center

   **Figure 3:** Key elements represented for the Electricity and Buildings sectors



**Technologies**

.. list-table:: **Table 1.** Technologies and Descriptions
   :header-rows: 1
   :widths: 22 50 28

   * - **Tech**
     - **Description**
     - **Model component**

   * - DIST_DSL
     - Import / distribution – Diesel
     - Primary supply
   * - DIST_GSL
     - Import / distribution – Gasoline
     - Primary supply
   * - DIST_NGS
     - Import / distribution – Natural gas
     - Primary supply
   * - DIST_LPG
     - Import / distribution – LPG
     - Primary supply
   * - DIST_COK
     - Import / distribution – Coke
     - Primary supply
   * - DIST_KER
     - Import / distribution – Kerosene
     - Primary supply
   * - DIST_JET
     - Import / distribution – Jet fuel
     - Primary supply
   * - DIST_FIR
     - Production – Firewood
     - Primary renewable
   * - DIST_CHA
     - Production – Charcoal
     - Primary renewable
   * - DIST_BIM
     - Production – Biomass
     - Primary renewable
   * - DIST_BGS
     - Production – Biogas
     - Primary renewable
   * - DIST_OPE
     - Import / distribution – Other products
     - Primary supply
   * - EXTT_CRU
     - Extraction / transformation – Crude oil
     - Primary extraction
   * - DIST_COA
     - Import / distribution – Coal
     - Primary supply
   * - DIST_PV
     - Solar resource
     - Primary renewable
   * - DIST_FOI
     - Import / distribution – Fuel oil
     - Primary supply
   * - PPHDAM
     - Hydro power plant (dam)
     - Electricity generation
   * - PPHROR
     - Hydro power plant (run-of-river)
     - Electricity generation
   * - PPGEO
     - Geothermal power plant
     - Electricity generation
   * - PPWNDON
     - On-shore wind
     - Electricity generation
   * - PPWNDONS
     - On-shore wind + storage
     - Electricity generation
   * - PPWNDOFF
     - Off-shore wind
     - Electricity generation
   * - PPPVT
     - Utility-scale solar PV
     - Electricity generation
   * - PPPVTS
     - Utility-scale solar PV + storage
     - Electricity generation
   * - PPPVD
     - Distributed solar PV
     - Electricity generation
   * - PPPVDS
     - Distributed solar PV + storage
     - Electricity generation
   * - ELE_TRANS
     - High-voltage transmission grid
     - Power network
   * - ELE_DIST
     - Medium / low-voltage distribution grid
     - Power network
   * - HYD_G_PROD
     - Green-hydrogen production
     - Secondary conversion
   * - HYD_DIST
     - Hydrogen distribution
     - Secondary conversion
   * - STOELE
     - Battery storage
     - Storage
   * - PPBIM
     - Biomass power plant
     - Electricity generation
   * - PPBGS
     - Biogas power plant
     - Electricity generation
   * - PPNGS
     - Natural-gas power plant
     - Electricity generation
   * - PPDSL
     - Diesel power plant
     - Electricity generation
   * - PPFOI
     - Fuel-oil power plant
     - Electricity generation
   * - REF_DSL
     - Diesel refinery
     - Refining
   * - REF_GSL
     - Gasoline refinery
     - Refining
   * - REF_LPG
     - LPG refinery
     - Refining
   * - REF_FOI
     - Fuel-oil refinery
     - Refining
   * - REF_JET
     - Jet-fuel refinery
     - Refining
   * - REF_OPE
     - Other-products refinery
     - Refining
   * - T5ELECOM
     - Electricity demand – Commercial
     - Final demand
   * - T5ELERES
     - Electricity demand – Residential
     - Final demand
   * - T5ELETMA
     - Electricity demand – Transport (maritime)
     - Final demand
   * - T5ELETRO
     - Electricity demand – Transport (road)
     - Final demand
   * - T5DSLEXP
     - Diesel demand – Exports
     - Final demand
   * - T5JETEXP
     - Jet-fuel demand – Exports
     - Final demand
   * - T5FOIEXP
     - Fuel-oil demand – Exports
     - Final demand