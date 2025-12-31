# Betfair Starting Price Data

![Daily Sync](https://github.com/EonHorizons/betfair_sp/actions/workflows/actions.yml/badge.svg)

Historical Betfair Starting Price (BSP) data for horse racing and greyhound racing, suitable for testing betting strategies with historic data.

## Available Data

### Sports
- **Greyhound Racing** - Daily race data from UK and Australia
- **Horse Racing** - Daily race data from multiple countries

### Countries (Horse Racing)
- UK, Australia, Ireland, France, USA, UAE, South Africa

### Data Fields
Each CSV file contains:
- `EVENT_ID` - Unique event identifier
- `MENU_HINT` - Race location and date
- `EVENT_NAME` - Race name and distance
- `EVENT_DT` - Event date/time
- `SELECTION_ID` - Unique selection identifier
- `SELECTION_NAME` - Runner name and number
- `WIN_LOSE` - Outcome (1=Win, 0=Lose)
- `BSP` - Betfair Starting Price
- `PPWAP` / `MORNINGWAP` - Weighted average prices
- `PPMAX` / `PPMIN` / `IPMAX` / `IPMIN` - Price ranges
- `MORNINGTRADEDVOL` / `PPTRADEDVOL` / `IPTRADEDVOL` - Traded volumes

## Data Source

Primary source: https://promo.betfair.com/betfairsp/prices

## Data Download

Full dataset available on Kaggle:
https://www.kaggle.com/datasets/eonsky/betfair-sp

## Repository Structure

```
betfair_sp/
├── data_original/
│   ├── greyhound/YEAR/MONTH/   # Greyhound racing data
│   └── horse/COUNTRY/YEAR/MONTH/  # Horse racing by country
├── main.py                      # Main sync script
├── config.py                    # Centralized configuration
├── get_bsp_files.py            # Fetch available files from source
├── current_data.py             # Scan local data structure
├── compare_json.py             # Find missing files
└── delete_duplicates.py        # Clean up duplicates
```

## Automated Sync

Data is automatically synced daily via GitHub Actions at 1:00 AM UTC.

## Data Quality Notes

### Known Issues Addressed
- **EVENT_NAME column parsing** - Some files between 2017-2024 had extra columns due to commas in the EVENT_NAME string. These have been corrected by merging split columns.
- **Missing MENU_HINT data** - Australian greyhound races missing MENU_HINT details have been filled by cross-referencing with https://www.thegreyhoundrecorder.com.au/ (2017-2024 range updated).

## Usage Example

```python
import pandas as pd

# Load a single day's greyhound data
df = pd.read_csv('data_original/greyhound/2024/01/dwbfgreyhoundwin02012024.csv')

# Filter for winners
winners = df[df['WIN_LOSE'] == 1]

# Calculate average BSP for winners
print(f"Average winning BSP: {winners['BSP'].mean():.2f}")
```

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes.

## License

See [LICENSE](LICENSE) for details.
