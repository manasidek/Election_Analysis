# Election_Analysis

## Overview of Election Audit 

## Purpose of this election audit analysis
- The purpose of the analysis is to help a Board of Elections Employee to provide the audit of a recent local congressional election to the election commission.

## Resources
- Data Source: [Election_Results](https://github.com/manasidek/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.72.2

## Election-Audit Results
The Election Result are referenced in this file [Election_Analysis](https://github.com/manasidek/Election_Analysis/blob/main/analysis/election_analysis.txt)

The Text file output:

![ElectionAnalysisResults](https://github.com/manasidek/Election_Analysis/blob/main/ElectionAnalysisResults.png)

The Terminal Output:

![Terminal_output](https://github.com/manasidek/Election_Analysis/blob/main/TerminalOutput.png)

### The Analysis of the Election Show that:
- The total number of votes casted in this congressional election in the precinct are **369,711**
- The number of votes for each county in the precinct are as follows:

**County Votes**

| County Name | Vote Percentage |  Votes  |
|-------------|-----------------|---------|
| Jefferson   |      10.5%      | 38,855  |
|  Denver     |      82.8%      | 306,055 |
| Arapahoe    |      6.7%       | 24,801  |

	
- The largest number of votes casted are in ***DENVER*** county.


- The number of votes each candidate received are as follows:

| 	Candidate Name     | Vote Percentage |  Votes  |
|--------------------------|-----------------|---------|
| Charles Casper Stockham  |      23.0%      | 85,213  |
| Diana DeGette            |      73.8%      | 272,892 |
| Raymon Anthony Doane     |      3.1%       | 11,606  |



- The **Winning candidate** is ***DIANA DEGETTE***
- The **Winning Vote Count** is **272,892**
- The **Winning Percentage** is **73.8%**


## Election-Audit Summary

The script can be used to obtain the above election results for any other election, as it reads candidate and county names dynamically from the data and aggregates the vote counts accordingly. There will be minor modifications required in case the data for the other elections is in a different file location or format compared to the current. 

The script for the analysis [Pypoll_challenge](https://github.com/manasidek/Election_Analysis/blob/main/Pypoll_Challenge.py)

These modifications are explained below:
- File Name and File Path: The file name and path in the code snippet below will need to be updated to reflect the file name and path of the new election that needs to be analyzed.
```
file_to_load = os.path.join("Resources", "election_results.csv")
```

- Data Format: The current data has 'Ballot ID', 'County Name' and 'Candidate Name' in that order. If this differs in the data for the new election, the script will need to be modified.
![Data_Format]()
```
 # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```

