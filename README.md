# Coming in 2024
- Data for various sports in organised folder structure
- Additional sports data for soccer, cricket and tennis.

## Sports Data 
- Greyhound Racing
- Horse Racing
- Soccer (Coming 2024)
- Tennis (Coming 2024)
- Cricket (Coming 2024)

### Code
Python code to download data from sources @ repo:

## Data sources from
### Horse & Greyhound from 
- https://promo.betfair.com/betfairsp/prices


### Additional data download location
https://www.kaggle.com/datasets/eonsky/betfair-sp


#### Contact
For additional updates or requests contact email: (to follow by February 2024) 


*** Important Update ***
Greyhound race files only.
Corrections made:
A) additional columns found correction
B) missing MENU_HINT data updated

- A - -
Due to additional columns found in column 'EVENT_NAME', when parsing data with pandas, corrections have been made to some of the source files between 2017 - 2024.
Initially the cell in this column was deleted which will result in a missing word in the EVENT_NAME string.

Until it was realised that the extra column was due to the comma in the EVENT_NAME string. Then the split string was merged back together.

The files affected that had the cell contents deleted will be rechecked and corrected at some stage. These affected UK races where the 'MENU_HINT' column string = 'Greyhound Racing / Trap Challenge'

- B - -
For some Australian Greyhound Races, entire race 'MENU_HINT' column string details would be missing.
These have been filled by cross checking race results from https://www.thegreyhoundrecorder.com.au/
Currently 2017 - 2024 date range updated.