# MOMF - Multipurpose OSeMOSYS-based Modeling Framework

[![Documentation Status](https://readthedocs.org/projects/openmodels-lac/badge/?version=latest)](https://openmodels-lac.readthedocs.io/en/latest/?badge=latest)

MOMF is a framework for building and running OSeMOSYS-based energy and emissions models for Latin American and Caribbean countries. It provides standardized workflows for scenario analysis, GHG emissions projections, and policy evaluation.

## Features

- **Multi-sector modeling**: Energy, AFOLU, IPPU, Waste, Transport
- **Multiple workflow versions**: v1 (basic), v2 (standard), v3 (advanced with YAML)
- **Parallel execution**: Run multiple scenarios simultaneously
- **Flexible solvers**: GLPK, CBC, CPLEX support (v3)
- **Excel-based inputs**: User-friendly parameterization

## Countries

| Country | Code | Sectors |
|---------|------|---------|
| Costa Rica | CRI | Energy, AFOLU, IPPU, Waste |
| Dominican Republic | DOM | Energy, AFOLU, IPPU, Waste |
| Ecuador | ECU | Energy, Agriculture, FOLU, IPPU, Waste |
| Guatemala | GUA | Energy, AFOLU, IPPU, Waste |
| Honduras | HND | Energy, AFOLU |
| Jamaica | JAM | AFOLU, Electricity/Buildings/Industry, Transport, Waste |

## Quick Start

1. Clone the repository
2. Install dependencies: Python 3.9+, pandas, openpyxl, GLPK solver
3. Open Spyder and navigate to a model folder (e.g., `GUA/IPPU`)
4. Run the scripts in order: A1 -> A2 -> B1 -> B2

For detailed instructions, see the [Documentation](https://openmodels-lac.readthedocs.io/).

## Documentation

Full documentation is available at: **https://openmodels-lac.readthedocs.io/**

- [Installation Guide](https://openmodels-lac.readthedocs.io/en/latest/installation.html)
- [Quick Start](https://openmodels-lac.readthedocs.io/en/latest/quickstart.html)
- [Workflow Versions](https://openmodels-lac.readthedocs.io/en/latest/versions.html)
- [Country Models](https://openmodels-lac.readthedocs.io/en/latest/countries.html)

## Vendored Dependencies

| Original Project | Folder | Version | License | Link |
|------------------|--------|---------|---------|------|
| ndc_cr | CRI | 2025-08-06 (`f8157d9`) | MIT | https://github.com/clg-admin/ndc_cr |
| ECU_NDC | ECU | 2025-03-31 (`ea7065d`) | MIT | https://github.com/clg-admin/ECU_NDC |
| GUA_LTS | GUA | 2025-07-22 (`20bfa62`) | MIT | https://github.com/clg-admin/GUA_LTS |
| ENDRCH-HON | HND | 2025-07-22 (`a28533f`) | MIT | https://github.com/clg-admin/ENDRCH-HON |
| JAM-LTS | JAM | 2025-07-22 | MIT | https://github.com/clg-admin/JAM-LTS |
| LTS-RD | DOM | 2025-07-22 (`c971401`) | MIT | https://github.com/clg-admin/LTS-RD |

> **Note:** The code for each model is maintained under its original license. Only data has been modified. See the [`LICENSES/`](./LICENSES) directory for details.

## License

MIT License - See [LICENSE](./LICENSE) for details.
